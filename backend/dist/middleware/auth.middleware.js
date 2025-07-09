"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.optionalAuth = exports.authenticateToken = void 0;
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const client_1 = require("@prisma/client");
const prisma = new client_1.PrismaClient();
const authenticateToken = async (req, res, next) => {
    try {
        const authHeader = req.headers.authorization;
        const token = authHeader && authHeader.split(' ')[1];
        if (!token) {
            return res.status(401).json({
                success: false,
                error: 'Access token required',
            });
        }
        const decoded = jsonwebtoken_1.default.verify(token, process.env.JWT_SECRET);
        const session = await prisma.session.findUnique({
            where: { token },
            include: { user: true },
        });
        if (!session || session.expiresAt < new Date()) {
            return res.status(401).json({
                success: false,
                error: 'Invalid or expired token',
            });
        }
        req.user = {
            id: session.user.id,
            email: session.user.email,
            name: session.user.name,
        };
        next();
    }
    catch (error) {
        return res.status(403).json({
            success: false,
            error: 'Invalid token',
        });
    }
};
exports.authenticateToken = authenticateToken;
const optionalAuth = async (req, res, next) => {
    try {
        const authHeader = req.headers.authorization;
        const token = authHeader && authHeader.split(' ')[1];
        if (token) {
            const decoded = jsonwebtoken_1.default.verify(token, process.env.JWT_SECRET);
            const session = await prisma.session.findUnique({
                where: { token },
                include: { user: true },
            });
            if (session && session.expiresAt >= new Date()) {
                req.user = {
                    id: session.user.id,
                    email: session.user.email,
                    name: session.user.name,
                };
            }
        }
        next();
    }
    catch (error) {
        next();
    }
};
exports.optionalAuth = optionalAuth;
//# sourceMappingURL=auth.middleware.js.map
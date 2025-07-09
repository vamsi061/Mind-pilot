"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthController = void 0;
const bcryptjs_1 = __importDefault(require("bcryptjs"));
const jsonwebtoken_1 = __importDefault(require("jsonwebtoken"));
const database_1 = __importDefault(require("../utils/database"));
const validation_1 = require("../utils/validation");
class AuthController {
    static async register(req, res) {
        try {
            const validatedData = validation_1.registerSchema.parse(req.body);
            const { email, password, name } = validatedData;
            const existingUser = await database_1.default.user.findUnique({
                where: { email },
            });
            if (existingUser) {
                return res.status(400).json({
                    success: false,
                    error: 'User with this email already exists',
                });
            }
            const saltRounds = 12;
            const hashedPassword = await bcryptjs_1.default.hash(password, saltRounds);
            const user = await database_1.default.user.create({
                data: {
                    email,
                    name,
                    password: hashedPassword,
                },
                select: {
                    id: true,
                    email: true,
                    name: true,
                    avatar: true,
                    createdAt: true,
                    updatedAt: true,
                },
            });
            const token = jsonwebtoken_1.default.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: process.env.JWT_EXPIRES_IN || '7d' });
            const expiresAt = new Date();
            expiresAt.setDate(expiresAt.getDate() + 7);
            await database_1.default.session.create({
                data: {
                    userId: user.id,
                    token,
                    expiresAt,
                },
            });
            res.status(201).json({
                success: true,
                data: {
                    user,
                    token,
                    expiresAt: expiresAt.toISOString(),
                },
                message: 'User registered successfully',
            });
        }
        catch (error) {
            console.error('Registration error:', error);
            if (error.code === 'P2002') {
                return res.status(400).json({
                    success: false,
                    error: 'Email already exists',
                });
            }
            if (error.name === 'ZodError') {
                return res.status(400).json({
                    success: false,
                    error: 'Validation failed',
                    details: error.errors,
                });
            }
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async login(req, res) {
        try {
            const validatedData = validation_1.loginSchema.parse(req.body);
            const { email, password } = validatedData;
            const user = await database_1.default.user.findUnique({
                where: { email },
            });
            if (!user) {
                return res.status(401).json({
                    success: false,
                    error: 'Invalid email or password',
                });
            }
            const isPasswordValid = await bcryptjs_1.default.compare(password, user.password);
            if (!isPasswordValid) {
                return res.status(401).json({
                    success: false,
                    error: 'Invalid email or password',
                });
            }
            const token = jsonwebtoken_1.default.sign({ userId: user.id }, process.env.JWT_SECRET, { expiresIn: process.env.JWT_EXPIRES_IN || '7d' });
            const expiresAt = new Date();
            expiresAt.setDate(expiresAt.getDate() + 7);
            await database_1.default.session.create({
                data: {
                    userId: user.id,
                    token,
                    expiresAt,
                },
            });
            const { password: _, ...userWithoutPassword } = user;
            res.status(200).json({
                success: true,
                data: {
                    user: userWithoutPassword,
                    token,
                    expiresAt: expiresAt.toISOString(),
                },
                message: 'Login successful',
            });
        }
        catch (error) {
            console.error('Login error:', error);
            if (error.name === 'ZodError') {
                return res.status(400).json({
                    success: false,
                    error: 'Validation failed',
                    details: error.errors,
                });
            }
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async logout(req, res) {
        try {
            const authHeader = req.headers.authorization;
            const token = authHeader && authHeader.split(' ')[1];
            if (token) {
                await database_1.default.session.deleteMany({
                    where: { token },
                });
            }
            res.status(200).json({
                success: true,
                message: 'Logout successful',
            });
        }
        catch (error) {
            console.error('Logout error:', error);
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async me(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const user = await database_1.default.user.findUnique({
                where: { id: userId },
                select: {
                    id: true,
                    email: true,
                    name: true,
                    avatar: true,
                    createdAt: true,
                    updatedAt: true,
                },
            });
            if (!user) {
                return res.status(404).json({
                    success: false,
                    error: 'User not found',
                });
            }
            res.status(200).json({
                success: true,
                data: { user },
            });
        }
        catch (error) {
            console.error('Get user error:', error);
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async refreshToken(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const token = jsonwebtoken_1.default.sign({ userId }, process.env.JWT_SECRET, { expiresIn: process.env.JWT_EXPIRES_IN || '7d' });
            const expiresAt = new Date();
            expiresAt.setDate(expiresAt.getDate() + 7);
            await database_1.default.session.create({
                data: {
                    userId,
                    token,
                    expiresAt,
                },
            });
            const authHeader = req.headers.authorization;
            const oldToken = authHeader && authHeader.split(' ')[1];
            if (oldToken) {
                await database_1.default.session.deleteMany({
                    where: { token: oldToken },
                });
            }
            res.status(200).json({
                success: true,
                data: {
                    token,
                    expiresAt: expiresAt.toISOString(),
                },
                message: 'Token refreshed successfully',
            });
        }
        catch (error) {
            console.error('Refresh token error:', error);
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
}
exports.AuthController = AuthController;
//# sourceMappingURL=auth.controller.js.map
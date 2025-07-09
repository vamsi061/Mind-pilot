"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.IdeasController = void 0;
const database_1 = __importDefault(require("../utils/database"));
const validation_1 = require("../utils/validation");
const ai_service_1 = require("../services/ai.service");
class IdeasController {
    static async createIdea(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const validatedData = validation_1.createIdeaSchema.parse(req.body);
            const { title, description, category, tags } = validatedData;
            const idea = await database_1.default.idea.create({
                data: {
                    title,
                    description,
                    category,
                    tags: tags || [],
                    userId,
                    status: 'DRAFT',
                },
                include: {
                    tasks: true,
                    mindMap: true,
                },
            });
            ai_service_1.AIService.analyzeIdea(title, description)
                .then(async (analysis) => {
                await database_1.default.idea.update({
                    where: { id: idea.id },
                    data: {
                        aiAnalysis: analysis,
                        status: 'ANALYZING',
                    },
                });
            })
                .catch((error) => {
                console.error('Background AI analysis failed:', error);
            });
            res.status(201).json({
                success: true,
                data: { idea },
                message: 'Idea created successfully',
            });
        }
        catch (error) {
            console.error('Create idea error:', error);
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
    static async getIdeas(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { page, limit, search, category, status, sortBy, sortOrder } = validation_1.paginationSchema.parse(req.query);
            const where = { userId };
            if (search) {
                where.OR = [
                    { title: { contains: search, mode: 'insensitive' } },
                    { description: { contains: search, mode: 'insensitive' } },
                ];
            }
            if (category) {
                where.category = category;
            }
            if (status) {
                where.status = status;
            }
            const orderBy = {};
            if (sortBy === 'title') {
                orderBy.title = sortOrder;
            }
            else if (sortBy === 'category') {
                orderBy.category = sortOrder;
            }
            else if (sortBy === 'status') {
                orderBy.status = sortOrder;
            }
            else {
                orderBy.createdAt = sortOrder;
            }
            const total = await database_1.default.idea.count({ where });
            const ideas = await database_1.default.idea.findMany({
                where,
                orderBy,
                skip: (page - 1) * limit,
                take: limit,
                include: {
                    tasks: {
                        orderBy: { order: 'asc' },
                    },
                    mindMap: true,
                },
            });
            res.status(200).json({
                success: true,
                data: ideas,
                pagination: {
                    page,
                    limit,
                    total,
                    totalPages: Math.ceil(total / limit),
                },
            });
        }
        catch (error) {
            console.error('Get ideas error:', error);
            if (error.name === 'ZodError') {
                return res.status(400).json({
                    success: false,
                    error: 'Invalid query parameters',
                    details: error.errors,
                });
            }
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async getIdeaById(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { id } = req.params;
            const idea = await database_1.default.idea.findFirst({
                where: {
                    id,
                    userId,
                },
                include: {
                    tasks: {
                        include: {
                            children: true,
                        },
                        orderBy: { order: 'asc' },
                    },
                    mindMap: true,
                },
            });
            if (!idea) {
                return res.status(404).json({
                    success: false,
                    error: 'Idea not found',
                });
            }
            res.status(200).json({
                success: true,
                data: { idea },
            });
        }
        catch (error) {
            console.error('Get idea error:', error);
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async updateIdea(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { id } = req.params;
            const existingIdea = await database_1.default.idea.findFirst({
                where: {
                    id,
                    userId,
                },
            });
            if (!existingIdea) {
                return res.status(404).json({
                    success: false,
                    error: 'Idea not found',
                });
            }
            const validatedData = validation_1.updateIdeaSchema.parse(req.body);
            const idea = await database_1.default.idea.update({
                where: { id },
                data: {
                    ...validatedData,
                    updatedAt: new Date(),
                },
                include: {
                    tasks: true,
                    mindMap: true,
                },
            });
            res.status(200).json({
                success: true,
                data: { idea },
                message: 'Idea updated successfully',
            });
        }
        catch (error) {
            console.error('Update idea error:', error);
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
    static async deleteIdea(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { id } = req.params;
            const existingIdea = await database_1.default.idea.findFirst({
                where: {
                    id,
                    userId,
                },
            });
            if (!existingIdea) {
                return res.status(404).json({
                    success: false,
                    error: 'Idea not found',
                });
            }
            await database_1.default.idea.delete({
                where: { id },
            });
            res.status(200).json({
                success: true,
                message: 'Idea deleted successfully',
            });
        }
        catch (error) {
            console.error('Delete idea error:', error);
            res.status(500).json({
                success: false,
                error: 'Internal server error',
            });
        }
    }
    static async analyzeIdea(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { id } = req.params;
            const idea = await database_1.default.idea.findFirst({
                where: {
                    id,
                    userId,
                },
            });
            if (!idea) {
                return res.status(404).json({
                    success: false,
                    error: 'Idea not found',
                });
            }
            await database_1.default.idea.update({
                where: { id },
                data: { status: 'ANALYZING' },
            });
            const analysis = await ai_service_1.AIService.analyzeIdea(idea.title, idea.description);
            const updatedIdea = await database_1.default.idea.update({
                where: { id },
                data: {
                    aiAnalysis: analysis,
                    status: 'STRUCTURED',
                },
                include: {
                    tasks: true,
                    mindMap: true,
                },
            });
            res.status(200).json({
                success: true,
                data: { idea: updatedIdea },
                message: 'AI analysis completed',
            });
        }
        catch (error) {
            console.error('Analyze idea error:', error);
            await database_1.default.idea.update({
                where: { id: req.params.id },
                data: { status: 'DRAFT' },
            }).catch(() => { });
            res.status(500).json({
                success: false,
                error: 'AI analysis failed',
            });
        }
    }
    static async expandIdea(req, res) {
        try {
            const userId = req.user?.id;
            if (!userId) {
                return res.status(401).json({
                    success: false,
                    error: 'Not authenticated',
                });
            }
            const { id } = req.params;
            const idea = await database_1.default.idea.findFirst({
                where: {
                    id,
                    userId,
                },
            });
            if (!idea) {
                return res.status(404).json({
                    success: false,
                    error: 'Idea not found',
                });
            }
            const suggestions = await ai_service_1.AIService.expandIdea(idea.title, idea.description);
            res.status(200).json({
                success: true,
                data: { suggestions },
                message: 'Expansion suggestions generated',
            });
        }
        catch (error) {
            console.error('Expand idea error:', error);
            res.status(500).json({
                success: false,
                error: 'Failed to generate expansion suggestions',
            });
        }
    }
}
exports.IdeasController = IdeasController;
//# sourceMappingURL=ideas.controller.js.map
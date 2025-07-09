"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.paginationSchema = exports.updateMindMapSchema = exports.updateTaskSchema = exports.createTaskSchema = exports.updateIdeaSchema = exports.createIdeaSchema = exports.loginSchema = exports.registerSchema = void 0;
const zod_1 = require("zod");
exports.registerSchema = zod_1.z.object({
    email: zod_1.z.string().email('Invalid email format'),
    password: zod_1.z.string().min(8, 'Password must be at least 8 characters'),
    name: zod_1.z.string().min(2, 'Name must be at least 2 characters'),
});
exports.loginSchema = zod_1.z.object({
    email: zod_1.z.string().email('Invalid email format'),
    password: zod_1.z.string().min(1, 'Password is required'),
});
exports.createIdeaSchema = zod_1.z.object({
    title: zod_1.z.string().min(3, 'Title must be at least 3 characters').max(100, 'Title must be less than 100 characters'),
    description: zod_1.z.string().min(10, 'Description must be at least 10 characters').max(2000, 'Description must be less than 2000 characters'),
    category: zod_1.z.string().optional(),
    tags: zod_1.z.array(zod_1.z.string()).optional().default([]),
});
exports.updateIdeaSchema = zod_1.z.object({
    title: zod_1.z.string().min(3).max(100).optional(),
    description: zod_1.z.string().min(10).max(2000).optional(),
    category: zod_1.z.string().optional(),
    tags: zod_1.z.array(zod_1.z.string()).optional(),
    status: zod_1.z.enum(['DRAFT', 'ANALYZING', 'STRUCTURED', 'PLANNED', 'ARCHIVED']).optional(),
});
exports.createTaskSchema = zod_1.z.object({
    title: zod_1.z.string().min(3, 'Title must be at least 3 characters').max(100),
    description: zod_1.z.string().max(1000).optional(),
    type: zod_1.z.enum(['EPIC', 'STORY', 'TASK', 'BUG', 'SUBTASK']).optional().default('TASK'),
    priority: zod_1.z.enum(['LOW', 'MEDIUM', 'HIGH', 'URGENT']).optional().default('MEDIUM'),
    storyPoints: zod_1.z.number().int().min(1).max(21).optional(),
    acceptanceCriteria: zod_1.z.array(zod_1.z.string()).optional().default([]),
    parentId: zod_1.z.string().optional(),
});
exports.updateTaskSchema = zod_1.z.object({
    title: zod_1.z.string().min(3).max(100).optional(),
    description: zod_1.z.string().max(1000).optional(),
    type: zod_1.z.enum(['EPIC', 'STORY', 'TASK', 'BUG', 'SUBTASK']).optional(),
    priority: zod_1.z.enum(['LOW', 'MEDIUM', 'HIGH', 'URGENT']).optional(),
    status: zod_1.z.enum(['TODO', 'IN_PROGRESS', 'IN_REVIEW', 'DONE', 'BLOCKED']).optional(),
    storyPoints: zod_1.z.number().int().min(1).max(21).optional(),
    acceptanceCriteria: zod_1.z.array(zod_1.z.string()).optional(),
    parentId: zod_1.z.string().optional(),
    order: zod_1.z.number().int().optional(),
});
exports.updateMindMapSchema = zod_1.z.object({
    nodes: zod_1.z.array(zod_1.z.object({
        id: zod_1.z.string(),
        type: zod_1.z.string(),
        position: zod_1.z.object({
            x: zod_1.z.number(),
            y: zod_1.z.number(),
        }),
        data: zod_1.z.object({
            label: zod_1.z.string(),
            description: zod_1.z.string().optional(),
            category: zod_1.z.string().optional(),
            color: zod_1.z.string().optional(),
        }),
    })),
    edges: zod_1.z.array(zod_1.z.object({
        id: zod_1.z.string(),
        source: zod_1.z.string(),
        target: zod_1.z.string(),
        type: zod_1.z.string().optional(),
        animated: zod_1.z.boolean().optional(),
        label: zod_1.z.string().optional(),
    })),
    layout: zod_1.z.record(zod_1.z.any()).optional(),
});
exports.paginationSchema = zod_1.z.object({
    page: zod_1.z.string().transform(val => parseInt(val) || 1),
    limit: zod_1.z.string().transform(val => Math.min(parseInt(val) || 10, 100)),
    search: zod_1.z.string().optional(),
    category: zod_1.z.string().optional(),
    status: zod_1.z.string().optional(),
    sortBy: zod_1.z.string().optional(),
    sortOrder: zod_1.z.enum(['asc', 'desc']).optional().default('desc'),
});
//# sourceMappingURL=validation.js.map
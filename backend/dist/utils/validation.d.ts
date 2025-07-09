import { z } from 'zod';
export declare const registerSchema: z.ZodObject<{
    email: z.ZodString;
    password: z.ZodString;
    name: z.ZodString;
}, "strip", z.ZodTypeAny, {
    email: string;
    password: string;
    name: string;
}, {
    email: string;
    password: string;
    name: string;
}>;
export declare const loginSchema: z.ZodObject<{
    email: z.ZodString;
    password: z.ZodString;
}, "strip", z.ZodTypeAny, {
    email: string;
    password: string;
}, {
    email: string;
    password: string;
}>;
export declare const createIdeaSchema: z.ZodObject<{
    title: z.ZodString;
    description: z.ZodString;
    category: z.ZodOptional<z.ZodString>;
    tags: z.ZodDefault<z.ZodOptional<z.ZodArray<z.ZodString, "many">>>;
}, "strip", z.ZodTypeAny, {
    title: string;
    description: string;
    tags: string[];
    category?: string | undefined;
}, {
    title: string;
    description: string;
    category?: string | undefined;
    tags?: string[] | undefined;
}>;
export declare const updateIdeaSchema: z.ZodObject<{
    title: z.ZodOptional<z.ZodString>;
    description: z.ZodOptional<z.ZodString>;
    category: z.ZodOptional<z.ZodString>;
    tags: z.ZodOptional<z.ZodArray<z.ZodString, "many">>;
    status: z.ZodOptional<z.ZodEnum<["DRAFT", "ANALYZING", "STRUCTURED", "PLANNED", "ARCHIVED"]>>;
}, "strip", z.ZodTypeAny, {
    status?: "DRAFT" | "ANALYZING" | "STRUCTURED" | "PLANNED" | "ARCHIVED" | undefined;
    title?: string | undefined;
    description?: string | undefined;
    category?: string | undefined;
    tags?: string[] | undefined;
}, {
    status?: "DRAFT" | "ANALYZING" | "STRUCTURED" | "PLANNED" | "ARCHIVED" | undefined;
    title?: string | undefined;
    description?: string | undefined;
    category?: string | undefined;
    tags?: string[] | undefined;
}>;
export declare const createTaskSchema: z.ZodObject<{
    title: z.ZodString;
    description: z.ZodOptional<z.ZodString>;
    type: z.ZodDefault<z.ZodOptional<z.ZodEnum<["EPIC", "STORY", "TASK", "BUG", "SUBTASK"]>>>;
    priority: z.ZodDefault<z.ZodOptional<z.ZodEnum<["LOW", "MEDIUM", "HIGH", "URGENT"]>>>;
    storyPoints: z.ZodOptional<z.ZodNumber>;
    acceptanceCriteria: z.ZodDefault<z.ZodOptional<z.ZodArray<z.ZodString, "many">>>;
    parentId: z.ZodOptional<z.ZodString>;
}, "strip", z.ZodTypeAny, {
    type: "EPIC" | "STORY" | "TASK" | "BUG" | "SUBTASK";
    title: string;
    priority: "LOW" | "MEDIUM" | "HIGH" | "URGENT";
    acceptanceCriteria: string[];
    description?: string | undefined;
    storyPoints?: number | undefined;
    parentId?: string | undefined;
}, {
    title: string;
    type?: "EPIC" | "STORY" | "TASK" | "BUG" | "SUBTASK" | undefined;
    description?: string | undefined;
    priority?: "LOW" | "MEDIUM" | "HIGH" | "URGENT" | undefined;
    storyPoints?: number | undefined;
    acceptanceCriteria?: string[] | undefined;
    parentId?: string | undefined;
}>;
export declare const updateTaskSchema: z.ZodObject<{
    title: z.ZodOptional<z.ZodString>;
    description: z.ZodOptional<z.ZodString>;
    type: z.ZodOptional<z.ZodEnum<["EPIC", "STORY", "TASK", "BUG", "SUBTASK"]>>;
    priority: z.ZodOptional<z.ZodEnum<["LOW", "MEDIUM", "HIGH", "URGENT"]>>;
    status: z.ZodOptional<z.ZodEnum<["TODO", "IN_PROGRESS", "IN_REVIEW", "DONE", "BLOCKED"]>>;
    storyPoints: z.ZodOptional<z.ZodNumber>;
    acceptanceCriteria: z.ZodOptional<z.ZodArray<z.ZodString, "many">>;
    parentId: z.ZodOptional<z.ZodString>;
    order: z.ZodOptional<z.ZodNumber>;
}, "strip", z.ZodTypeAny, {
    type?: "EPIC" | "STORY" | "TASK" | "BUG" | "SUBTASK" | undefined;
    status?: "TODO" | "IN_PROGRESS" | "IN_REVIEW" | "DONE" | "BLOCKED" | undefined;
    title?: string | undefined;
    description?: string | undefined;
    priority?: "LOW" | "MEDIUM" | "HIGH" | "URGENT" | undefined;
    storyPoints?: number | undefined;
    acceptanceCriteria?: string[] | undefined;
    parentId?: string | undefined;
    order?: number | undefined;
}, {
    type?: "EPIC" | "STORY" | "TASK" | "BUG" | "SUBTASK" | undefined;
    status?: "TODO" | "IN_PROGRESS" | "IN_REVIEW" | "DONE" | "BLOCKED" | undefined;
    title?: string | undefined;
    description?: string | undefined;
    priority?: "LOW" | "MEDIUM" | "HIGH" | "URGENT" | undefined;
    storyPoints?: number | undefined;
    acceptanceCriteria?: string[] | undefined;
    parentId?: string | undefined;
    order?: number | undefined;
}>;
export declare const updateMindMapSchema: z.ZodObject<{
    nodes: z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        type: z.ZodString;
        position: z.ZodObject<{
            x: z.ZodNumber;
            y: z.ZodNumber;
        }, "strip", z.ZodTypeAny, {
            x: number;
            y: number;
        }, {
            x: number;
            y: number;
        }>;
        data: z.ZodObject<{
            label: z.ZodString;
            description: z.ZodOptional<z.ZodString>;
            category: z.ZodOptional<z.ZodString>;
            color: z.ZodOptional<z.ZodString>;
        }, "strip", z.ZodTypeAny, {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        }, {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        }>;
    }, "strip", z.ZodTypeAny, {
        type: string;
        id: string;
        position: {
            x: number;
            y: number;
        };
        data: {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        };
    }, {
        type: string;
        id: string;
        position: {
            x: number;
            y: number;
        };
        data: {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        };
    }>, "many">;
    edges: z.ZodArray<z.ZodObject<{
        id: z.ZodString;
        source: z.ZodString;
        target: z.ZodString;
        type: z.ZodOptional<z.ZodString>;
        animated: z.ZodOptional<z.ZodBoolean>;
        label: z.ZodOptional<z.ZodString>;
    }, "strip", z.ZodTypeAny, {
        id: string;
        source: string;
        target: string;
        type?: string | undefined;
        label?: string | undefined;
        animated?: boolean | undefined;
    }, {
        id: string;
        source: string;
        target: string;
        type?: string | undefined;
        label?: string | undefined;
        animated?: boolean | undefined;
    }>, "many">;
    layout: z.ZodOptional<z.ZodRecord<z.ZodString, z.ZodAny>>;
}, "strip", z.ZodTypeAny, {
    nodes: {
        type: string;
        id: string;
        position: {
            x: number;
            y: number;
        };
        data: {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        };
    }[];
    edges: {
        id: string;
        source: string;
        target: string;
        type?: string | undefined;
        label?: string | undefined;
        animated?: boolean | undefined;
    }[];
    layout?: Record<string, any> | undefined;
}, {
    nodes: {
        type: string;
        id: string;
        position: {
            x: number;
            y: number;
        };
        data: {
            label: string;
            description?: string | undefined;
            category?: string | undefined;
            color?: string | undefined;
        };
    }[];
    edges: {
        id: string;
        source: string;
        target: string;
        type?: string | undefined;
        label?: string | undefined;
        animated?: boolean | undefined;
    }[];
    layout?: Record<string, any> | undefined;
}>;
export declare const paginationSchema: z.ZodObject<{
    page: z.ZodEffects<z.ZodString, number, string>;
    limit: z.ZodEffects<z.ZodString, number, string>;
    search: z.ZodOptional<z.ZodString>;
    category: z.ZodOptional<z.ZodString>;
    status: z.ZodOptional<z.ZodString>;
    sortBy: z.ZodOptional<z.ZodString>;
    sortOrder: z.ZodDefault<z.ZodOptional<z.ZodEnum<["asc", "desc"]>>>;
}, "strip", z.ZodTypeAny, {
    page: number;
    limit: number;
    sortOrder: "asc" | "desc";
    status?: string | undefined;
    category?: string | undefined;
    search?: string | undefined;
    sortBy?: string | undefined;
}, {
    page: string;
    limit: string;
    status?: string | undefined;
    category?: string | undefined;
    search?: string | undefined;
    sortBy?: string | undefined;
    sortOrder?: "asc" | "desc" | undefined;
}>;
export type RegisterInput = z.infer<typeof registerSchema>;
export type LoginInput = z.infer<typeof loginSchema>;
export type CreateIdeaInput = z.infer<typeof createIdeaSchema>;
export type UpdateIdeaInput = z.infer<typeof updateIdeaSchema>;
export type CreateTaskInput = z.infer<typeof createTaskSchema>;
export type UpdateTaskInput = z.infer<typeof updateTaskSchema>;
export type UpdateMindMapInput = z.infer<typeof updateMindMapSchema>;
export type PaginationInput = z.infer<typeof paginationSchema>;
//# sourceMappingURL=validation.d.ts.map
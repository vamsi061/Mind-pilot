export interface AIAnalysisResult {
    problem: string;
    solution: string;
    targetAudience: string;
    revenueModel: string;
    marketSize?: string;
    competitors?: string[];
    keyFeatures?: string[];
    risks?: string[];
    opportunities?: string[];
    suggestedCategories?: string[];
    confidence: number;
}
export declare class AIService {
    static analyzeIdea(title: string, description: string): Promise<AIAnalysisResult>;
    static expandIdea(title: string, description: string): Promise<string[]>;
    static generateTasksFromMindMap(nodes: any[], edges: any[]): Promise<any[]>;
}
//# sourceMappingURL=ai.service.d.ts.map
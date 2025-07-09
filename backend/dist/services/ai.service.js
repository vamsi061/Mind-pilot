"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AIService = void 0;
const openai_1 = __importDefault(require("openai"));
const openai = new openai_1.default({
    apiKey: process.env.OPENAI_API_KEY,
});
class AIService {
    static async analyzeIdea(title, description) {
        try {
            const prompt = `
Analyze the following startup idea and provide a structured analysis:

Title: "${title}"
Description: "${description}"

Please provide a JSON response with the following structure:
{
  "problem": "What problem does this solve?",
  "solution": "What solution does it provide?",
  "targetAudience": "Who is the target audience?",
  "revenueModel": "What could be the revenue model?",
  "marketSize": "Estimated market size or potential",
  "competitors": ["List of potential competitors"],
  "keyFeatures": ["List of 3-5 key features"],
  "risks": ["List of potential risks"],
  "opportunities": ["List of opportunities"],
  "suggestedCategories": ["List of relevant categories"],
  "confidence": 0.85
}

Be specific, actionable, and realistic. The confidence score should be between 0 and 1.
`;
            const completion = await openai.chat.completions.create({
                model: "gpt-3.5-turbo",
                messages: [
                    {
                        role: "system",
                        content: "You are an expert startup advisor and business analyst. Provide detailed, actionable insights for startup ideas."
                    },
                    {
                        role: "user",
                        content: prompt
                    }
                ],
                temperature: 0.7,
                max_tokens: 1500,
            });
            const content = completion.choices[0]?.message?.content;
            if (!content) {
                throw new Error('No response from AI service');
            }
            const analysis = JSON.parse(content);
            return {
                problem: analysis.problem || 'Problem analysis not available',
                solution: analysis.solution || 'Solution analysis not available',
                targetAudience: analysis.targetAudience || 'Target audience not specified',
                revenueModel: analysis.revenueModel || 'Revenue model not specified',
                marketSize: analysis.marketSize,
                competitors: analysis.competitors || [],
                keyFeatures: analysis.keyFeatures || [],
                risks: analysis.risks || [],
                opportunities: analysis.opportunities || [],
                suggestedCategories: analysis.suggestedCategories || [],
                confidence: analysis.confidence || 0.5,
            };
        }
        catch (error) {
            console.error('AI Analysis Error:', error);
            return {
                problem: 'AI analysis temporarily unavailable',
                solution: 'Please provide manual analysis',
                targetAudience: 'Analysis pending',
                revenueModel: 'Analysis pending',
                confidence: 0,
            };
        }
    }
    static async expandIdea(title, description) {
        try {
            const prompt = `
Given this startup idea:
Title: "${title}"
Description: "${description}"

Suggest 5-7 related concepts, features, or expansion ideas that could complement this startup. 
Provide the response as a JSON array of strings.

Example: ["Feature 1", "Related concept 2", "Expansion idea 3"]
`;
            const completion = await openai.chat.completions.create({
                model: "gpt-3.5-turbo",
                messages: [
                    {
                        role: "system",
                        content: "You are a creative startup ideation expert. Provide innovative and practical expansion ideas."
                    },
                    {
                        role: "user",
                        content: prompt
                    }
                ],
                temperature: 0.8,
                max_tokens: 500,
            });
            const content = completion.choices[0]?.message?.content;
            if (!content) {
                return [];
            }
            const suggestions = JSON.parse(content);
            return Array.isArray(suggestions) ? suggestions : [];
        }
        catch (error) {
            console.error('Idea Expansion Error:', error);
            return [];
        }
    }
    static async generateTasksFromMindMap(nodes, edges) {
        try {
            const prompt = `
Given this mind map structure:
Nodes: ${JSON.stringify(nodes)}
Edges: ${JSON.stringify(edges)}

Generate a structured Jira-style task breakdown with Epics, Stories, and Tasks.
Provide the response as a JSON array with this structure:

[
  {
    "title": "Epic Title",
    "description": "Epic description",
    "type": "EPIC",
    "priority": "HIGH",
    "acceptanceCriteria": ["Criteria 1", "Criteria 2"],
    "storyPoints": null,
    "children": [
      {
        "title": "Story Title",
        "description": "Story description",
        "type": "STORY",
        "priority": "MEDIUM",
        "acceptanceCriteria": ["Criteria 1"],
        "storyPoints": 5,
        "children": [
          {
            "title": "Task Title",
            "description": "Task description",
            "type": "TASK",
            "priority": "MEDIUM",
            "storyPoints": 2,
            "acceptanceCriteria": ["Acceptance criteria"]
          }
        ]
      }
    ]
  }
]
`;
            const completion = await openai.chat.completions.create({
                model: "gpt-3.5-turbo",
                messages: [
                    {
                        role: "system",
                        content: "You are an expert project manager specializing in Agile methodologies and task breakdown."
                    },
                    {
                        role: "user",
                        content: prompt
                    }
                ],
                temperature: 0.6,
                max_tokens: 2000,
            });
            const content = completion.choices[0]?.message?.content;
            if (!content) {
                return [];
            }
            const tasks = JSON.parse(content);
            return Array.isArray(tasks) ? tasks : [];
        }
        catch (error) {
            console.error('Task Generation Error:', error);
            return [];
        }
    }
}
exports.AIService = AIService;
//# sourceMappingURL=ai.service.js.map
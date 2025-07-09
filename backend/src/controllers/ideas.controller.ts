import { Request, Response } from 'express';
import prisma from '../utils/database';
import { createIdeaSchema, updateIdeaSchema, paginationSchema } from '../utils/validation';
import { AuthenticatedRequest } from '../middleware/auth.middleware';
import { AIService } from '../services/ai.service';

export class IdeasController {
  // Create new idea
  static async createIdea(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      // Validate input
      const validatedData = createIdeaSchema.parse(req.body);
      const { title, description, category, tags } = validatedData;

      // Create idea
      const idea = await prisma.idea.create({
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

      // Start AI analysis in background (non-blocking)
      AIService.analyzeIdea(title, description)
        .then(async (analysis) => {
          await prisma.idea.update({
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
    } catch (error: any) {
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

  // Get all ideas for user with pagination
  static async getIdeas(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      // Validate query parameters
      const { page, limit, search, category, status, sortBy, sortOrder } = paginationSchema.parse(req.query);

      // Build where clause
      const where: any = { userId };

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

      // Build order by clause
      const orderBy: any = {};
      if (sortBy === 'title') {
        orderBy.title = sortOrder;
      } else if (sortBy === 'category') {
        orderBy.category = sortOrder;
      } else if (sortBy === 'status') {
        orderBy.status = sortOrder;
      } else {
        orderBy.createdAt = sortOrder;
      }

      // Get total count
      const total = await prisma.idea.count({ where });

      // Get ideas
      const ideas = await prisma.idea.findMany({
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
    } catch (error: any) {
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

  // Get single idea by ID
  static async getIdeaById(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      const { id } = req.params;

      const idea = await prisma.idea.findFirst({
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
    } catch (error) {
      console.error('Get idea error:', error);
      res.status(500).json({
        success: false,
        error: 'Internal server error',
      });
    }
  }

  // Update idea
  static async updateIdea(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      const { id } = req.params;

      // Check if idea exists and belongs to user
      const existingIdea = await prisma.idea.findFirst({
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

      // Validate input
      const validatedData = updateIdeaSchema.parse(req.body);

      // Update idea
      const idea = await prisma.idea.update({
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
    } catch (error: any) {
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

  // Delete idea
  static async deleteIdea(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      const { id } = req.params;

      // Check if idea exists and belongs to user
      const existingIdea = await prisma.idea.findFirst({
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

      // Delete idea (cascades to tasks and mindmap)
      await prisma.idea.delete({
        where: { id },
      });

      res.status(200).json({
        success: true,
        message: 'Idea deleted successfully',
      });
    } catch (error) {
      console.error('Delete idea error:', error);
      res.status(500).json({
        success: false,
        error: 'Internal server error',
      });
    }
  }

  // Trigger AI analysis for idea
  static async analyzeIdea(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      const { id } = req.params;

      // Check if idea exists and belongs to user
      const idea = await prisma.idea.findFirst({
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

      // Update status to analyzing
      await prisma.idea.update({
        where: { id },
        data: { status: 'ANALYZING' },
      });

      // Perform AI analysis
      const analysis = await AIService.analyzeIdea(idea.title, idea.description);

      // Update idea with analysis
      const updatedIdea = await prisma.idea.update({
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
    } catch (error) {
      console.error('Analyze idea error:', error);

      // Reset status on error
      await prisma.idea.update({
        where: { id: req.params.id },
        data: { status: 'DRAFT' },
      }).catch(() => {});

      res.status(500).json({
        success: false,
        error: 'AI analysis failed',
      });
    }
  }

  // Get idea expansion suggestions
  static async expandIdea(req: AuthenticatedRequest, res: Response) {
    try {
      const userId = req.user?.id;
      if (!userId) {
        return res.status(401).json({
          success: false,
          error: 'Not authenticated',
        });
      }

      const { id } = req.params;

      // Check if idea exists and belongs to user
      const idea = await prisma.idea.findFirst({
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

      // Get expansion suggestions
      const suggestions = await AIService.expandIdea(idea.title, idea.description);

      res.status(200).json({
        success: true,
        data: { suggestions },
        message: 'Expansion suggestions generated',
      });
    } catch (error) {
      console.error('Expand idea error:', error);
      res.status(500).json({
        success: false,
        error: 'Failed to generate expansion suggestions',
      });
    }
  }
}
import { Router } from 'express';
import { IdeasController } from '../controllers/ideas.controller';
import { authenticateToken } from '../middleware/auth.middleware';

const router = Router();

// All routes require authentication
router.use(authenticateToken);

/**
 * @route   POST /api/ideas
 * @desc    Create a new idea
 * @access  Private
 */
router.post('/', IdeasController.createIdea);

/**
 * @route   GET /api/ideas
 * @desc    Get all ideas for authenticated user
 * @access  Private
 */
router.get('/', IdeasController.getIdeas);

/**
 * @route   GET /api/ideas/:id
 * @desc    Get idea by ID
 * @access  Private
 */
router.get('/:id', IdeasController.getIdeaById);

/**
 * @route   PUT /api/ideas/:id
 * @desc    Update idea
 * @access  Private
 */
router.put('/:id', IdeasController.updateIdea);

/**
 * @route   DELETE /api/ideas/:id
 * @desc    Delete idea
 * @access  Private
 */
router.delete('/:id', IdeasController.deleteIdea);

/**
 * @route   POST /api/ideas/:id/analyze
 * @desc    Trigger AI analysis for idea
 * @access  Private
 */
router.post('/:id/analyze', IdeasController.analyzeIdea);

/**
 * @route   POST /api/ideas/:id/expand
 * @desc    Get AI expansion suggestions for idea
 * @access  Private
 */
router.post('/:id/expand', IdeasController.expandIdea);

export default router;
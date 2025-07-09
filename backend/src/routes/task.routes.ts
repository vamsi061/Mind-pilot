import { Router } from 'express';
import { authenticateToken } from '../middleware/auth.middleware';

const router = Router();

// All routes require authentication
router.use(authenticateToken);

/**
 * @route   POST /api/tasks
 * @desc    Create task for idea
 * @access  Private
 */
router.post('/', async (req, res) => {
  res.status(200).json({
    success: true,
    message: 'Task routes coming soon',
  });
});

export default router;
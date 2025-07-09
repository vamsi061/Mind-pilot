import { Router } from 'express';
import { authenticateToken } from '../middleware/auth.middleware';

const router = Router();

// All routes require authentication
router.use(authenticateToken);

/**
 * @route   PUT /api/mindmaps/:ideaId
 * @desc    Update mind map for idea
 * @access  Private
 */
router.put('/:ideaId', async (req, res) => {
  res.status(200).json({
    success: true,
    message: 'Mind map routes coming soon',
  });
});

export default router;
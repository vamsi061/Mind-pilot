"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const ideas_controller_1 = require("../controllers/ideas.controller");
const auth_middleware_1 = require("../middleware/auth.middleware");
const router = (0, express_1.Router)();
router.use(auth_middleware_1.authenticateToken);
router.post('/', ideas_controller_1.IdeasController.createIdea);
router.get('/', ideas_controller_1.IdeasController.getIdeas);
router.get('/:id', ideas_controller_1.IdeasController.getIdeaById);
router.put('/:id', ideas_controller_1.IdeasController.updateIdea);
router.delete('/:id', ideas_controller_1.IdeasController.deleteIdea);
router.post('/:id/analyze', ideas_controller_1.IdeasController.analyzeIdea);
router.post('/:id/expand', ideas_controller_1.IdeasController.expandIdea);
exports.default = router;
//# sourceMappingURL=idea.routes.js.map
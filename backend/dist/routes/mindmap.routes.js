"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const auth_middleware_1 = require("../middleware/auth.middleware");
const router = (0, express_1.Router)();
router.use(auth_middleware_1.authenticateToken);
router.put('/:ideaId', async (req, res) => {
    res.status(200).json({
        success: true,
        message: 'Mind map routes coming soon',
    });
});
exports.default = router;
//# sourceMappingURL=mindmap.routes.js.map
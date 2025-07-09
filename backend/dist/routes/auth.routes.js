"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const auth_controller_1 = require("../controllers/auth.controller");
const auth_middleware_1 = require("../middleware/auth.middleware");
const router = (0, express_1.Router)();
router.post('/register', auth_controller_1.AuthController.register);
router.post('/login', auth_controller_1.AuthController.login);
router.post('/logout', auth_middleware_1.authenticateToken, auth_controller_1.AuthController.logout);
router.get('/me', auth_middleware_1.authenticateToken, auth_controller_1.AuthController.me);
router.post('/refresh', auth_middleware_1.authenticateToken, auth_controller_1.AuthController.refreshToken);
exports.default = router;
//# sourceMappingURL=auth.routes.js.map
from fastapi import APIRouter
from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.admin import router as admin_router
from routes.question import router as question_router

router = APIRouter()

router.include_router(auth_router.router)
router.include_router(user_router.router)
router.include_router(admin_router.router)
router.include_router(question_router.router)
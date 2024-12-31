from .users import user_router
from .groups import group_router
from .channels import channel_router

def register_all_handlers(router):
    router.include_router(user_router)
    router.include_router(group_router)
    router.include_router(channel_router)
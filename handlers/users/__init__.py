from .admin import admin_router
from .start import start_router
from .help import help_router
from .echo import echo_router

user_router = admin_router
user_router.include_routers(start_router,help_router, echo_router)

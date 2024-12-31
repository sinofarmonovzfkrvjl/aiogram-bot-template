from .start import start_router
from .help import help_router
from .echo import echo_router

user_router = start_router
user_router.include_routers(help_router, echo_router)
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("BOT_TOKEN")
ADMIN_ID = env.int("ADMIN_ID")
print(ADMIN_ID, "FROM data.py")
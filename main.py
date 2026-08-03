import asyncio

from bot.client import CakeBot
from bot.core.config import settings
from bot.core.logging import setup_logging


async def main():
    setup_logging()
    if settings.TOKEN is None:
        raise Exception("Invalid Token")
    bot = CakeBot()
    async with bot:
        await bot.start(settings.TOKEN)
        
if __name__ == "__main__":
    asyncio.run(main())
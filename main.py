import asyncio

from bot.client import CakeBot
from bot.core.config import settings
from bot.core.logging import setup_logging

async def main():
    setup_logging()
    bot = CakeBot()
    async with bot:
        await bot.start(settings.TOKEN)
        
if __name__ == "__main__":
    asyncio.run(main())
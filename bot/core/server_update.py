import logging

from asyncio.tasks import sleep, create_task
from ..services.api_service import ServerListItem, ServerSummary, getServers

logger = logging.getLogger(__name__)

detailed_servers_cache: list[ServerSummary] = []
servers_cache: list[ServerListItem] = []
async def update_server_cache():
    global servers_cache
    logger.info("Updating Servers cache..")
    data = getServers()
    if data is None:
        logger.exception("Update Servers Failed D;")
        return

    logger.info("Updated Servers cache completed")
    servers_cache = data

async def update_interval(debounce: int):
    while True:
        await update_server_cache()
        await sleep(debounce)
        
interval_task = create_task(update_interval(25))
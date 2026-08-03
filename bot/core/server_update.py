import logging
import threading

from ..services.api_service import ServerListItem, ServerSummary, getServers

logger = logging.getLogger(__name__)

detailed_servers_cache: list[ServerSummary] = []
servers_cache: list[ServerListItem] = []
def update_server_cache():
    global servers_cache
    logger.info("Updating Servers cache..")
    data = getServers()
    if data is None:
        logger.exception("Update Servers Failed D;")
        return

    logger.info("Updated Servers cache completed")
    servers_cache = data
    threading.Timer(25.0, update_server_cache)

update_server_cache()
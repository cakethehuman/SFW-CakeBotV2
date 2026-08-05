import logging

# from concurrent.futures import ThreadPoolExecutor
from typing import TypedDict

import requests

logger = logging.getLogger(__name__)

# Server_id = [85023,85024,85025]
class ServerListItem(TypedDict):
    name: str
    serverId: int
    accountId: int
    maxPlayers: int
    currentPlayers: int

class ServerSummary(TypedDict):
    serverId: int
    accountId: int
    ip: str
    info: str
    port: int
    version: str
    online: bool
    modded: bool
    whitelist: bool
    friendlyFire: bool
    isoCode: int
    players: str
    pastebin: str
    official: int
    distance: int


# def getServerInfo(id):
#     url = f"https://api.scplist.kr/api/v2/servers/{id}"

#     try:
#         response = requests.get(url, timeout = 5)
#         logger.info(f"Fetching Data from id : {id}")
#         if response.status_code == 200:
#             data = response.json()
#             return data['players']
#         return "Failed"
#     except Exception as e:
#         logger.exception(f"Error because of {e}")
#         return None

# def getResultData():
#     with ThreadPoolExecutor(max_workers=3) as executor:
#         results = list(executor.map(getServerInfo, Server_id))
#     return results

def getServers() -> list[ServerListItem] | None:
    url = "https://api.scplist.kr/api/v2/servers"
    params = {
        "country": ( "SG" )
    }
    try:
        logger.info("Requesting data to API Service..")
        response = requests.get(url, params, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as error:
        logger.exception("Exception was raised when trying to request server data", exc_info=error)

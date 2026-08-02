import logging
from concurrent.futures import ThreadPoolExecutor

import requests

logger = logging.getLogger(__name__)

Server_id = [85023,85024,85025]

def getServerInfo(id):
    url = f"https://api.scplist.kr/api/v2/servers/{id}"
    
    try:
        response = requests.get(url, timeout = 5)
        logger.info(f"Fetching Data from id : {id}")
        if response.status_code == 200:
            data = response.json()
            return data['players']
        return "Failed"
    except Exception as e:
        logger.exception(f"Error because of {e}")
        return None
        
def getResultData():
    with ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(getServerInfo, Server_id))
    return results
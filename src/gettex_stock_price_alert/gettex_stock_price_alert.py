import requests
from loguru import logger


def gettex_stock_price_alert(
    url,
):
    """
    Calls a given URL and prints the response status code
    """
    r = requests.get(url)
    logger.info(f"Response: {r.status_code}")
    return r

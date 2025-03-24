#!/usr/bin/env python
import sys

import click
from loguru import logger

from gettex_stock_price_alert.gettex_stock_price_alert import (
    gettex_stock_price_alert,
)


@click.command()
@click.option(
    "--url",
    required=True,
    help="URL, e.g. https://example.com",
)
def cli(
    url,
):
    """
    HTTP Call CLI
    """

    gettex_stock_price_alert(
        url,
    )


if __name__ == "__main__":
    logger.remove(0)
    logger.add(sys.stdout, format='time={time} level={level} msg="{message}"')
    cli()

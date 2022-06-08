"""Simple cli tool to read the kostal piko data."""
import asyncio

from aiohttp import ClientSession
from pykostalpiko import Piko
from pykostalpiko.dxs.current_values import LIST


def main():
    """Run the asyncio main function."""
    asyncio.run(asnyc_main())


async def asnyc_main():
    async with ClientSession() as session:
        async with Piko(session, "192.168.113.1") as piko:
            print(await piko.async_fetch(LIST))


if __name__ == "__main__":
    main()

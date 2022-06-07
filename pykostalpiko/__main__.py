import asyncio
from email.mime import image
from pykostalpiko.dxs.current_values.grid import phase_1


def main():
    asyncio.run(phase_1.POWER)


async def asnyc_main():
    print()
    pass


if __name__ == "__main__":
    main()

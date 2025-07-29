import asyncio
from core.engine import run_game

async def main():
    await run_game()

asyncio.run(main())

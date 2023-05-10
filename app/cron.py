"""
    Cron - постоянное повторение.
"""
import asyncio

import httpx


async def check_status_site(url):
    try:
        async with httpx.AsyncClient() as client:
            print(f"request to {url}")
            r = await client.get(url)
            print(r.status_code)
    except Exception as e:
        print(e)
        print('Site is not available!')


async def running():
    period = 10
    url = "https://rasp.pskgu.ru"
    while True:
        try:
            print(1)
            await check_status_site(url)
        except Exception as e:
            print(e)
        finally:
            await asyncio.sleep(period)


async def run_cron():
    loop = asyncio.get_event_loop()
    loop.create_task(running())
    print("Cron launched.")

import asyncio
import aiohttp
import random

PROXIES = [
    "http://127.0.0.1:8080",
    # 可以添加你的更多代理
]

HEADERS_LIST = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
]

async def fetch(session, url, retries=3):
    for _ in range(retries):
        try:
            proxy = random.choice(PROXIES) if PROXIES else None
            headers = {"User-Agent": random.choice(HEADERS_LIST)}
            async with session.get(url, proxy=proxy, headers=headers, timeout=10) as resp:
                html = await resp.text()
                return {"url": url, "length": len(html)}
        except Exception as e:
            await asyncio.sleep(random.uniform(1, 3))
    return {"url": url, "error": "failed"}

async def crawl(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        return await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     urls = ["https://www.example.com", "https://www.baidu.com"]
#     results = asyncio.run(crawl(urls))
#     print(results)
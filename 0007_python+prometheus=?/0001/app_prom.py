from aiohttp import web
from prometheus_client import Counter, generate_latest


async def fire(request):
    request.app["counter"].labels("fire").inc()
    return web.Response(body=b"Fire!")


async def metrics(request):
    request.app["counter"].labels("metrics").inc()
    return web.Response(body=generate_latest())


async def get_application():
    app = web.Application()
    app.add_routes([
        web.get("/fire", fire),
        web.get("/metrics", metrics),
    ])
    app["counter"] = Counter("reqs", "Reqs counter", ["view"])
    return app


if __name__ == "__main__":
    web.run_app(get_application())

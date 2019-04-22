import aiodogstatsd
from aiohttp import web


async def fire(request):
    request.app["statsd"].increment(
        "reqs_total", tags={"view": "fire"}
    )
    return web.Response(body=b"Fire!")


async def statsd_client(app):
    app["statsd"] = aiodogstatsd.Client(host="0.0.0.0", port=9125)
    await app["statsd"].connect()
    yield
    await app["statsd"].close()


async def get_application():
    app = web.Application()
    app.add_routes([web.get("/fire", fire)])
    app.cleanup_ctx.append(statsd_client)
    return app


if __name__ == "__main__":
    web.run_app(get_application())

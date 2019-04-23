import asyncio

@asyncio.coroutine
def hello():
    print('hello world!')
    yield from asyncio.sleep(10)
    print('hello again!')


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
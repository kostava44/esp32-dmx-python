import asyncio


async def fade(ch, *args):
    """Add fade and wait until it completes."""
    ch.add_fade(*args)
    await ch.wait_till_fade_complete()


async def wait(chs, f):
    """Execute fades and wait until all fades for given channels complete."""
    f()
    await asyncio.gather(*[ch.wait_till_fade_complete() for ch in chs])


async def sleep(delay, *args):
    """Block for delay milliseconds."""
    return await asyncio.sleep(delay / 1000, *args)


async def race(*tasks):
    """Return the result of the first task to finish. Cancel the remaining
    tasks."""

    result = None
    for coro in asyncio.as_completed(tasks):
        result = await coro
        break

    return result


def forever(f):
    async def go(*args, **kwargs):
        while True:
            await f(*args, **kwargs)

    return go

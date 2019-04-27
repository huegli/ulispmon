import aioserial
import asyncio

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        print((await aioserial_instance.read_async()).decode(errors='ignore'), end='', flush=True)

loop=asyncio.get_event_loop()
loop.run_until_complete(read_and_print(aioserial.AioSerial(port='/dev/ttyS1')))

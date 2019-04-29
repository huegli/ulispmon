import aioserial
import asyncio
import datetime

async def read_and_print(aioserial_instance: aioserial.AioSerial):
    while True:
        print((await aioserial_instance.read_async()).decode(errors='ignore'), end='', flush=True)

async def write_out(aioserial_instance: aioserial.AioSerial):
    while True:
        await aioserial_instance.write_async("(+ 2 2)".encode())
        # print('Waiting...')
        await asyncio.sleep(2)
 
#async def display_date(loop):
#    end_time = loop.time() + 10.0
#    while True:
#        print(datetime.datetime.now())
#        if (loop.time() + 1.0) >= end_time:
#            break
#        await asyncio.sleep(1)
        
        
           
loop=asyncio.get_event_loop()
aios=aioserial.AioSerial(port='/dev/ttyS1')

# Blocking call interrupted by loop.stop()
loop.run_until_complete(asyncio.gather(
    read_and_print(aios),
    write_out(aios)))
    
loop.close()


    
 

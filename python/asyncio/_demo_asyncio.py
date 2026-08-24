import asyncio
import requests

async def function1():

    url = 'https://images.pexels.com/photos/30649280/pexels-photo-30649280.jpeg'
    r = requests.get(url, allow_redirects=True)
    open('google1.jpg', 'wb').write(r.content)    
    print("Function 1 completed")
    return "Function 1 result"


async def function2():
    url = 'https://images.pexels.com/photos/4991338/pexels-photo-4991338.jpeg'
    r = requests.get(url, allow_redirects=True)
    open('google2.jpg', 'wb').write(r.content)        
    print("Function 2 completed")

async def function3():

    url = 'https://images.pexels.com/photos/4826377/pexels-photo-4826377.jpeg'
    r = requests.get(url, allow_redirects=True)
    open('google3.jpg', 'wb').write(r.content)        
    print("Function 3 completed")


async def main():
    L = await asyncio.gather(
        function1(), 
        function2(), 
        function3()
    )
                   
    print(L)

asyncio.run(main())    
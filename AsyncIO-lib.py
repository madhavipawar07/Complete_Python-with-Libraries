import asyncio
async def task():
    print("Start")
    await asyncio.sleep(3)
    print("End")

asyncio.run(task())
print("Done")

async def download(name,time):
    print(f"Downloading{name}..")
    await asyncio.sleep(time)
    print(f"{name} downloaded")

async def main():
    await asyncio.gather(
        download("https://www.freepik.com/free-photos-vectors/imag",2),
        download("https://www.freepik.com/free-photos-vectors/landscape",3),
        download("https://www.bucketlistly.blog/posts/best-free-travel-images",1)
    )
asyncio.run(main())
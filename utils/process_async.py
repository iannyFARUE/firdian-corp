import asyncio

from concurrent.futures import ProcessPoolExecutor

def encrypt_data(data):
    # Simulate a CPU-bound encryption task
    import time
    time.sleep(2)  # Simulate time-consuming encryption
    return f"{data[::-1]}"  # Simple encryption by reversing the string

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, encrypt_data, "Sensitive Data")
        print(f"Encrypted data: {result}")


if __name__ == "__main__":
    asyncio.run(main())
    print("Encryption completed successfully.")

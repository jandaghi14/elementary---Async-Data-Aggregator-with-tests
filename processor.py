from fetchers import fetch_all_data
import asyncio


def fetch_multiple_batches(num_batches):
    for i in range(num_batches):
        data = asyncio.run(fetch_all_data())
        yield data
        

if __name__ == "__main__":
    gen = fetch_multiple_batches(3)
    for batch in gen:
        user_name = batch[0]['results'][0]['name']['first']
        joke = batch[1]['value']
        print(f"✅ Batch processed: {user_name}")
        
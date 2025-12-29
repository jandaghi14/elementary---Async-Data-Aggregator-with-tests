import asyncio
import aiohttp
from database import DatabaseConnection

async def fetch_random_user(session, timeout =10):
    url = "https://randomuser.me/api/"
    try:
        async with session.get(url , timeout= aiohttp.ClientTimeout(total = timeout)) as response:
            if response.status != 200:
                print(f"API error: status {response.status}")
                return None 
            data= await response.json()
            return data
    except asyncio.TimeoutError:
        print(f"Timeout: API took longer than {timeout} seconds")
        return None
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")
        return None
        
async def fetch_random_joke(session , timeout = 10):
    url = "https://api.chucknorris.io/jokes/random"
    try:    
        async with session.get(url , timeout = aiohttp.ClientTimeout(total = timeout)) as response:
            if response.status != 200:
                print(f"API error: status {response.status}")
                return None
            data = await response.json()
            return data
    except asyncio.TimeoutError:
        print(f"Timeout: API took longer than {timeout} seconds")
        return None
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")
        return None
    
    
async def fetch_all_data():
    async with aiohttp.ClientSession() as session:
        result= await asyncio.gather(
            fetch_random_user(session),
            fetch_random_joke(session)
        )
        if result[0] is None or result[1] is None:
            print("Error: One or both APIs failed")
            return None
        user_name = result[0]['results'][0]['name']['first']
        joke = result[1]['value']
        print(user_name,joke)
        
        with DatabaseConnection("TESTDATABASE.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS dbCache (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_name TEXT,
                                joke TEXT
                            )
                        """)
            cursor.execute("""
                           INSERT INTO dbCache (user_name, joke)
                           VALUES (?,?)
                           """,(user_name , joke)) 
        
        
        
        return result

if __name__ == "__main__":
    asyncio.run(fetch_all_data())
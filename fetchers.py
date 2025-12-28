import asyncio
import aiohttp
from database import DatabaseConnection

async def fetch_random_user(session):
    url = "https://randomuser.me/api/"
    async with session.get(url) as response:
        data= await response.json()
        return data
    
async def fetch_random_joke(session):
    url = "https://api.chucknorris.io/jokes/random"
    async with session.get(url) as response:
        data = await response.json()
        return data
    
async def fetch_all_data():
    async with aiohttp.ClientSession() as session:
        result= await asyncio.gather(
            fetch_random_user(session),
            fetch_random_joke(session)
        )
        
        user_name = result[0]['results'][0]['name']['first']
        joke = result[1]['value']
        print(user_name,joke)
        
        with DatabaseConnection("TESTDATABASE.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           INSERT INTO dbCache (user_name, joke)
                           VALUES (?,?)
                           """,(user_name , joke)) 
        
        
        
        return result

if __name__ == "__main__":
    asyncio.run(fetch_all_data())
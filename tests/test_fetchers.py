import pytest 
import aiohttp
from aioresponses import aioresponses
from unittest.mock import Mock , patch
import sys
sys.path.append('..')
from fetchers import fetch_all_data , fetch_random_joke , fetch_random_user
from database import DatabaseConnection

@pytest.mark.asyncio
async def test_fetch_user():
    with aioresponses() as mock:
        fake_response = {
            'results': [
                {
                    'name': {'first': 'John', 'last': 'Doe'}
                }
            ]
        }
        mock.get("https://randomuser.me/api/" , payload = fake_response)
        
        async with aiohttp.ClientSession() as session:
            response= await fetch_random_user(session)
        assert response == fake_response
        assert response['results'][0]['name']['first'] == 'John'
        
@pytest.mark.asyncio
async def test_fetch_random_joke():
    with aioresponses() as mock:
        fake_joke = {'value' : "here is a fake joke"}
        mock.get("https://api.chucknorris.io/jokes/random" , payload =fake_joke)
        async with aiohttp.ClientSession() as session:
            response = await fetch_random_joke(session)
        assert response == fake_joke
        assert response['value'] == "here is a fake joke"
        
@pytest.mark.asyncio
@patch('fetchers.DatabaseConnection')
async def test_fetch_all_data(mock_db):
    with aioresponses() as mock:
        fake_user = {'results': [{'name': {'first': 'John', 'last': 'Doe'}}]}
        fake_joke = {'value' : "here is a fake joke"}
        mock.get("https://randomuser.me/api/" , payload = fake_user)
        mock.get("https://api.chucknorris.io/jokes/random" , payload =fake_joke)
        response = await fetch_all_data()
        assert len(response) == 2
        assert response[0] == fake_user
        assert response[1] == fake_joke
        mock_db.assert_called_once_with("TESTDATABASE.db")

             


        
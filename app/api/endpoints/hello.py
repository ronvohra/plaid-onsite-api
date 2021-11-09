from fastapi import APIRouter
from httpx import AsyncClient

from app.core.logger import logger

router = APIRouter()


@router.get('/')
def read_root():
    logger.info('This is an example of logging')
    return {'hello': 'world'}


@router.get('/pokemon')
async def get_pokemon():
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
    client = AsyncClient()
    response = await client.get(pokemon_url)
    return response.json()

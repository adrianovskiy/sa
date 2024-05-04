import asyncio
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
    # pool_size=5,
    # max_overflow=10,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)

# with sync_engine.connect() as conn:
#     res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
#     print(f"{res.first()=}")

async def get_123():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.first()=}")
        
asyncio.run(get_123())
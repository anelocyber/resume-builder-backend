import asyncio
import asyncpg

async def test_connection():
    print("🔍 Attempting to connect to Supabase...")
    try:
        conn = await asyncpg.connect(
            user='postgres',
            password='yhZSkkDU6PCCftFc',
            database='postgres',
            host='db.loisbmkxqfwstglsdgip.supabase.co',
            port=5432,
            timeout=10  # seconds
        )
        print("✅ Connected successfully!")
        await conn.close()
    except Exception as e:
        print("❌ Connection failed:")
        print(repr(e))

asyncio.run(test_connection())
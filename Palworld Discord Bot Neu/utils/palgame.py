import aiosqlite
import os

DATABASE_PATH = os.path.join('data', 'palbot.db')

async def add_experience(user_id, pal_name, experience_gained):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''UPDATE user_pals SET experience = experience + ? WHERE user_id = ? AND pal_name = ?;''', (experience_gained, user_id, pal_name))
        await db.commit()

async def add_pal(user_id, pal_name, experience=0, level=1):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            INSERT INTO user_pals (user_id, pal_name, experience, level)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(user_id, pal_name) DO UPDATE
            SET experience = excluded.experience, level = excluded.level;
        ''', (user_id, pal_name, experience, level))
        await db.commit()

async def get_pals(user_id):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute('''
            SELECT pal_name, level, experience FROM user_pals WHERE user_id = ?
        ''', (user_id,))
        pals = await cursor.fetchall()
        return pals
    
async def level_up(user_id, pal_name):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute('''
            UPDATE user_pals
            SET level = level + 1, experience = 0
            WHERE user_id = ? AND pal_name = ? AND experience >= 1000;
        ''', (user_id, pal_name))
        await db.commit()

async def get_stats(user_id, pal_name):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute('''
            SELECT level, experience FROM user_pals
            WHERE user_id = ? AND pal_name = ?;
        ''', (user_id, pal_name))
        return await cursor.fetchone()

async def check_pal(user_id, pal_name):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute('''
            SELECT 1 FROM user_pals WHERE user_id = ? AND pal_name = ?
        ''', (user_id, pal_name))
        return await cursor.fetchone() is not None

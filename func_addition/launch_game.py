import asyncio
from config import STEAM_PATH
import subprocess
import time


async def dota_start(game_id, game_name):
    process = subprocess.Popen(STEAM_PATH + game_id)
    time.sleep(30)
    try:
        while True:
            if not await is_program_running(game_name):
                break
            time.sleep(2)
    except KeyboardInterrupt:
        print("Программа остановлена пользователем")
    finally:
        if process.poll() is None:
            process.terminate()
            process.wait()


async def is_program_running(program_name):
    try:
        result = await asyncio.create_subprocess_exec(
            'tasklist',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        stdout_decoded = stdout.decode(errors='replace')
        return program_name.lower() in stdout_decoded.lower()
    except Exception as e:
        print(f"Ошибка при проверке запущенных программ: {e}")
        return False


async def close_dota_fun(game_name):
    if await is_program_running(game_name):
        try:
            result = await asyncio.create_subprocess_exec(
                'taskkill', '/f', '/im', game_name,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            await result.communicate()
        except Exception as e:
            print(f"Ошибка при завершении программы {game_name}: {e}")

from typing import NoReturn
import sys

def fatal_error(msg: str) -> NoReturn:
    print(f"Фатальная ошибка: {msg}")
    sys.exit(1)
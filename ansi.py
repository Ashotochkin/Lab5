def ansi(x: str, color: int, format=0):
    return f"\033[{format}m\033[{color}m{x}\033[0m"


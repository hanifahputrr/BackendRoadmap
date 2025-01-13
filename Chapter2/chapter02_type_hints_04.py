def greeting(name: str | None = None) -> str:
    return f"Hello, {name if name else 'Guys'}"


print(greeting())  # "Hello, Anonymous"
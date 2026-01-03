"""Simple Hello World application."""


def greet(name: str = "World") -> str:
    """
    Return a greeting message.
    
    Args:
        name: The name to greet. Defaults to "World".
        
    Returns:
        A greeting message string.
    """
    return f"Hello, {name}!"


def main():
    """Main entry point of the application."""
    print(greet())


if __name__ == "__main__":
    main()

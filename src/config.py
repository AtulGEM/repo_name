def load_config():
    """Load configuration settings from environment variables."""
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    return {
        "GITHUB_APP_ID": os.getenv("GITHUB_APP_ID"),
        "GITHUB_APP_PRIVATE_KEY": os.getenv("GITHUB_APP_PRIVATE_KEY"),
        "GITHUB_API_URL": os.getenv("GITHUB_API_URL", "https://api.github.com"),
    }
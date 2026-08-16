import os
from dotenv import load_dotenv

def load_env():
    """Load variables from the .env file into the environment."""
    load_dotenv()

def get_key(name="API_KEY"):
    """Return the value of an env variable, or None if it isn't set."""
    return os.getenv(name)
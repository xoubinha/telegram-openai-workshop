import os
from dotenv import load_dotenv
load_dotenv()

def get_environment_variable(variable_name: str) -> str:
    """
    Access and handle the value of an environment variable.

    Args:
        variable_name (str): The name of the environment variable to access.

    Returns:
        str: The value of the environment variable.

    Raises:
        ValueError: If the environment variable is not defined or is empty.
    """
    try:
        value = os.environ[variable_name]
        if not value:
            raise ValueError(f"Environment variable {variable_name} is empty.")
    except KeyError:
        raise ValueError(f"Environment variable {variable_name} is not defined.")

    return value

if __name__ == '__main__':
    BOT_TOKEN = get_environment_variable("BOT_TOKEN")
    OPENAI_API_KEY = get_environment_variable("OPENAI_API_KEY")
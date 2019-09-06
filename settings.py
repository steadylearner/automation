from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

webpage = os.getenv("webpage")
x = os.getenv("x")
y = os.getenv("y")




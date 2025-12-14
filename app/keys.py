# pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()


API_DS = str(os.environ.get("key_deepseek"))

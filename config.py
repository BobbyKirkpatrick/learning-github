import os
from dotenv import load_dotenv

load_dotenv()

dev_config = {

    'db': os.getenv("DATABASE"),
    'table': os.getenv("TABLE"),
    'user': os.getenv("USERNAME")
}


stage_config = {
    'db': 'db name',
    'table': 'table',
    'user': 'user1'
}

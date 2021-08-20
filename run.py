import logging
from app import create_app

# Configure logging
logging.basicConfig(level=logging.INFO)

app = create_app()


import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class Settings:
    
    BASE_URL = os.getenv("BASE_URL")
    LOGIN_URL = f"{BASE_URL}/hub/auth/login"
    DASHBOARD_URL = f"{BASE_URL}/dashboard"
    PROJECT_URL = f"{BASE_URL}/projects"

    REPORTS_DIR = Path("reports")
    
    
    
    UI_USERNAME = os.getenv("UI_USERNAME")
    UI_PASSWORD = os.getenv("UI_PASSWORD")
    
    
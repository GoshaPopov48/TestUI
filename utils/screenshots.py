from test_data.factories import generate_unique_name
from playwright.sync_api import Page
from config.settings import Settings




def take_screen(page: str, prefix: str)-> str:
    screenshot_name = generate_unique_name(prefix)
    
    screenshot_path = Settings.REPORTS_DIR / f"{screenshot_name}.png"
    
    page.screenshot(path = str(screenshot_path))
    
    return str(screenshot_path)

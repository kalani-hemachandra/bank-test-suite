import os
from datetime import datetime

def capture_screenshot(driver, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"tests/screenshots/{name}_failure.png"
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)  # Ensure directory exists
    screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GymReservationBot:
    def __init__(self):
        self.url = "http://localhost:5000"  # Your Flask site
        self.username = "test"
        self.password = "1234"
        self.slot = "6:00 PM"
        self.driver = None

    def setup_driver(self):
        """Setup Chrome driver with GUI (visible browser)"""
        options = Options()
    # options.add_argument("--headless")  # ❌ Comment this to see browser
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
    # Use your ChromeDriver path
        service = Service(r"C:\Windows\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        print("[OK] ChromeDriver initialized")


    def login(self):
        """Login to the Flask gym site"""
        self.driver.get(self.url)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        self.driver.find_element(By.NAME, "username").send_keys(self.username)
        self.driver.find_element(By.NAME, "password").send_keys(self.password)
        self.driver.find_element(By.TAG_NAME, "button").click()
        print("[OK] Logged in successfully")

    def make_reservation(self):
        """Book the preferred time slot"""
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Book a Time Slot"))
        ).click()

        slots = self.driver.find_elements(By.TAG_NAME, "li")
        for s in slots:
            if self.slot in s.text and "Already Reserved" not in s.text:
                s.find_element(By.TAG_NAME, "button").click()
                print(f"[ok] Reserved {self.slot}")
                return
        print(" Slot not available")

    def run(self):
        """Run the full bot"""
        self.setup_driver()
        self.login()
        self.make_reservation()
        self.driver.quit()
        print("[ok] Bot finished execution")

if __name__ == "__main__":
    GymReservationBot().run()



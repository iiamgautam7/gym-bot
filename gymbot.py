import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



DB_FILE = "gymbot.db"

def init_db():
    """Initialize SQLite database and create table if not exists"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            slot TEXT NOT NULL,
            status TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_booking(user, slot, status):
    """Log booking info to the database"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO bookings (user, slot, status)
        VALUES (?, ?, ?)
    ''', (user, slot, status))
    conn.commit()
    conn.close()

def show_bookings():
    """Print all bookings from DB"""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('SELECT * FROM bookings')
    rows = c.fetchall()
    conn.close()
    for row in rows:
        print(row)

# Initialize database at the start
init_db()



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
        service = Service(r"C:\Windows\chromedriver.exe")  # Path to your chromedriver
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
                log_booking(user=self.username, slot=self.slot, status="Reserved")  # Log to DB
                return
        print("Slot not available")
        log_booking(user=self.username, slot=self.slot, status="Failed")  # Log failure

    def run(self):
        """Run the full bot"""
        try:
            self.setup_driver()
            self.login()
            self.make_reservation()
        finally:
            if self.driver:
                self.driver.quit()
            print("[ok] Bot finished execution")



if __name__ == "__main__":
    bot = GymReservationBot()
    bot.run()

    # Optional: print all bookings for verification
    print(" All Bookings ")
    show_bookings()

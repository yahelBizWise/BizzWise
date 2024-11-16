print(23)
import yfinance as yf
import time

# הגדר את תדירות המשיכה (במקרה זה, כל דקה)
interval = 60  # שניות

# הגדרת מניית SPY
ticker = "SPY"
stock = yf.Ticker(ticker)

# פונקציה למשיכת הנתונים והצגתם
def get_minute_data():
    data = stock.history(period="1d", interval="1m")  # משיכה של נתוני דקה אחת
    latest_data = data.iloc[-1]  # שורה אחרונה (הכי עדכנית)
    print(f"Time: {latest_data.name}, Close Price: {latest_data['Close']}")

# לולאה אינסופית למשיכת הנתונים כל דקה
while True:
    get_minute_data()
    time.sleep(interval)
import yfinance as yf
import time

# רשימת המניות או הסימולים שאתה רוצה לעקוב אחריהם
tickers = ["AAPL", "GOOG", "SPY","NVDA","TSLA","META","AMZN","MSFT"]

while True:
    for ticker in tickers:
        data = yf.download(ticker, period="1d", interval="1m")
        print(f"Data for {ticker}:")
        print(data.tail(1)) 
    time.sleep(1)  


# שמירת הנתונים לקובץ Excel
    file_path = "stock_data.xlsx"
    try:
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        data.to_excel(writer, sheet_name=ticker)
        print(f"הנתונים נשמרו בהצלחה לקובץ: {file_path}")
    except Exception as e:
    print(f"שגיאה בכתיבת הקובץ ל-Excel: {e}")
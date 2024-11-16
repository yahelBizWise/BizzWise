import yfinance as yf
import pandas as pd
from openpyxl import Workbook

# בחירת סימול המניה והגדרת טווח הזמן
ticker = 'SPY'
data = yf.download(ticker, period='1d', interval='1m')

# שמירת הנתונים לקובץ Excel
file_path = "stock_data.xlsx"  # הנתיב לקובץ ה-Excel

# יצירת או עדכון הקובץ עם הנתונים
with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
    data.to_excel(writer, sheet_name=ticker)
    
print("הנתונים נשמרו בהצלחה לקובץ Excel.")
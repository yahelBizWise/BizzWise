import yfinance as yf
import pandas as pd

# הגדרת הסימול וטווח הזמן
ticker = 'BTC-USD'  # לדוגמה, ביטקוין
try:
    data = yf.download(ticker, period='1d', interval='1m')
except Exception as e:
    print(f"שגיאה בהורדת נתונים מ-yfinance: {e}")
    exit()

# הסרת אזור זמן מהאינדקס
try:
    if data.index.tz is not None:  # בדיקה אם לאינדקס יש אזור זמן
        data.index = data.index.tz_convert(None)  # הסרת אזור זמן
except Exception as e:
    print(f"שגיאה בהסרת אזור זמן מהאינדקס: {e}")
    exit()

# הסרת אזור זמן מעמודות (אם קיימות)
try:
    for col in data.columns:
        if pd.api.types.is_datetime64_any_dtype(data[col]):  # בדיקה אם העמודה היא מסוג datetime
            data[col] = data[col].dt.tz_convert(None)  # הסרת אזור זמן
except Exception as e:
    print(f"שגיאה בהסרת אזור זמן מהעמודות: {e}")
    exit()

# שמירת הנתונים לקובץ Excel
file_path = "stock_data.xlsx"
try:
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        data.to_excel(writer, sheet_name=ticker)
    print(f"הנתונים נשמרו בהצלחה לקובץ: {file_path}")
except Exception as e:
    print(f"שגיאה בכתיבת הקובץ ל-Excel: {e}")
import yfinance as yf
import matplotlib.pyplot as plt

# הורדת נתונים מ-YFinance (במקרה הזה, מניה)
ticker = "AAPL"  # תחליף ב-ticker של המניה שתרצה
data = yf.download(ticker, period="7d", interval="1h")

# יצירת גרף של מחירי הסגירה
plt.plot(data.index, data['Close'], label="מחיר סגירה", color='blue')

# הוספת כותרת ותיוגים
plt.title(f"מחיר סגירה למניה {ticker}")
plt.xlabel("תאריך")
plt.ylabel("מחיר סגירה")

# הוספת מפתח (legend)
plt.legend()

# סיבוב התאריכים בציר ה-X כדי למנוע חפיפות
plt.xticks(rotation=45)

# סידור אוטומטי של התוויות
plt.tight_layout()

# הצגת הגרף
plt.show()
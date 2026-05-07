import requests
import time
import datetime
import pytz

# إعداد توقيت الرياض
def get_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    return datetime.datetime.now(riyadh_tz).strftime("%I:%M:%S %p")

def fetch_market_data():
    """هذا هو رادار الأسعار العالمي الصافي"""
    try:
        # سحب سعر الذهب (PAXG) مقابل الدولار
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            price = float(response.json()['price'])
            return f"🟡 الذهب: ${price:,.2f}"
    except Exception as e:
        return "📡 جارٍ محاولة الاتصال بالسوق..."
    return "⚠️ البيانات غير متوفرة حالياً"

def start_engine():
    print("\n" + "!"*30)
    print("🚀 انطلاق المحرك الصافي (Zero-Telegram)")
    print("📡 رادار الأسعار يعمل بنظام 24/7")
    print("!"*30 + "\n")
    
    while True:
        current_time = get_time()
        market_info = fetch_market_data()
        
        # طباعة النتيجة في الشاشة السوداء مباشرة
        print(f"[{current_time}] {market_info}")
        
        # تحديث كل 30 ثانية لضمان أعلى دقة
        time.sleep(30)

if __name__ == "__main__":
    start_engine()

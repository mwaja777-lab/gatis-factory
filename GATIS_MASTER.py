import requests
import time
import datetime
import pytz

def get_riyadh_time():
    # توقيت الرياض الدقيق
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    return datetime.datetime.now(riyadh_tz).strftime("%I:%M:%S %p")

def fetch_price(symbol, label):
    """رادار سحب الأسعار من البورصة العالمية مباشرة"""
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            price = float(res.json()['price'])
            return f"{label}: ${price:,.2f}"
    except:
        return f"{label}: جارٍ إعادة الاتصال..."
    return f"{label}: غير متاح"

def run_factory():
    print("\n" + "="*40)
    print("🚀 انطلاق المصنع العالمي (النسخة الصامتة)")
    print("📡 الحالة: رادار الأسعار يعمل 24/7")
    print("="*40 + "\n")
    
    while True:
        timestamp = get_riyadh_time()
        # جلب الذهب والبيتكوين كمؤشرات أساسية للسوق
        gold = fetch_price("PAXGUSDT", "🟡 الذهب")
        btc  = fetch_price("BTCUSDT",  "🔵 البيتكوين")
        
        print(f"[{timestamp}] -> {gold} | {btc}")
        
        # تحديث كل 30 ثانية لضمان الدقة العالية
        time.sleep(30)

if __name__ == "__main__":
    run_factory()

import requests
import time
import datetime
import pytz

# إعدادات الوقت - الرياض
def get_riyadh_time():
    tz = pytz.timezone('Asia/Riyadh')
    return datetime.datetime.now(tz).strftime("%I:%M:%S %p")

# رادار البورصة العالمية
def fetch_gold_price():
    try:
        # اتصال مباشر ببورصة بينانس العالمية (سعر الذهب PAXG)
        url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            price = float(response.json()['price'])
            return f"🟡 الذهب: ${price:,.2f}"
    except:
        return "📡 إعادة محاولة الاتصال..."
    return "⚠️ البيانات غير متاحة"

def main():
    print("\n" + "="*40)
    print("🚀 تشغيل المصنع (النسخة المجردة)")
    print("📡 الحالة: رادار الأسعار يعمل بكفاءة 100%")
    print("="*40 + "\n")
    
    while True:
        time_now = get_riyadh_time()
        price_now = fetch_gold_price()
        
        # طباعة النتيجة في الشاشة السوداء فقط
        print(f"[{time_now}] -> {price_now}")
        
        # تحديث كل 30 ثانية لضمان الاستقرار
        time.sleep(30)

if __name__ == "__main__":
    main()

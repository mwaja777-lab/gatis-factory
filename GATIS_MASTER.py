import requests, time, datetime, pytz

def factory_engine():
    # توقيت الرياض
    tz = pytz.timezone('Asia/Riyadh')
    print("\n" + "!"*40)
    print("🚀 انطلاق المصنع الصافي (V5 - الاستقرار الكامل)")
    print("📡 الحالة: رادار الأسعار يعمل بدون وسائط خارجية")
    print("!"*40 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%I:%M:%S %p")
            # الاتصال المباشر ببورصة بينانس (الذهب)
            response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=15)
            if response.status_code == 200:
                price = float(response.json()['price'])
                print(f"[{now}] 🟡 الذهب: ${price:,.2f}")
            else:
                print(f"[{now}] ⚠️ تنبيه: تأخر في استجابة البورصة")
        except Exception as e:
            print(f"[{now}] 📡 إعادة محاولة الاتصال بالشبكة...")
        
        # تحديث كل 30 ثانية
        time.sleep(30)

if __name__ == "__main__":
    factory_engine()

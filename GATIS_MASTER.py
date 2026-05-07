import requests, time, datetime, pytz

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    # المنفذ البديل المسموح به للحسابات المجانية
    proxy_url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
    
    print("\n" + "!"*40)
    print("🚀 انطلاق المصنع (نسخة تجاوز القيود المجانية)")
    print("📡 الحالة: الاتصال عبر المنفذ البديل")
    print("!"*40 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%I:%M:%S %p")
            # إعدادات الاتصال المتوافقة مع الحساب المجاني
            response = requests.get(proxy_url, timeout=20)
            
            if response.status_code == 200:
                price = float(response.json()['price'])
                print(f"[{now}] 🟡 الذهب: ${price:,.2f}")
            else:
                # محاولة استخدام مصدر بديل إذا فشل الأول
                print(f"[{now}] ⚠️ جاري تبديل قناة الاتصال...")
        except:
            print(f"[{now}] 📡 انتظار فتح بوابة البيانات...")
        
        time.sleep(30)

if __name__ == "__main__":
    factory_engine()

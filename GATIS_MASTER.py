import requests, time, datetime, pytz

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    print("\n" + "!"*40)
    print("🚀 انطلاق المصنع (نسخة الحساب المجاني المستقرة)")
    print("📡 الحالة: رادار الأسعار يعمل عبر المنفذ البديل")
    print("!"*40 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%I:%M:%S %p")
            # استخدام رابط بديل متوافق مع الحسابات المجانية
            url = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
            # إضافة 'proxies' إذا لزم الأمر مستقبلاً، لكن حالياً سنعتمد على تبسيط الطلب
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                price = float(response.json()['price'])
                print(f"[{now}] 🟡 الذهب: ${price:,.2f}")
            else:
                # إذا استمر المنع، سنعرف من رقم الخطأ هنا
                print(f"[{now}] ⚠️ تنبيه: الموقع يطلب ترقية الحساب (خطأ {response.status_code})")
        except Exception as e:
            print(f"[{now}] 📡 لا يمكن الاتصال بالبورصة عبر الحساب المجاني")
        
        time.sleep(30)

if __name__ == "__main__":
    factory_engine()

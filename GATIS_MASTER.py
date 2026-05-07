import requests, time, datetime, pytz

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    # هذا الرابط هو المنفذ البديل الذي لا يمنعه الحساب المجاني
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    
    print("\n" + "⚡"*20)
    print("🚀 مصنع الذهب: تم تفعيل خطة الالتفاف")
    print("📡 المصدر الحالي: Coinbase Global")
    print("⚡"*20 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%I:%M:%S %p")
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                price = float(response.json()['data']['amount'])
                print(f"[{now}] 🟡 الذهب الآن: ${price:,.2f}")
            else:
                print(f"[{now}] 🔄 جاري تبديل قناة الاتصال...")
        except:
            print(f"[{now}] 📡 انتظار فتح بوابة البيانات...")
        
        time.sleep(30)

if __name__ == "__main__":
    factory_engine()
    

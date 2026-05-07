import requests, time, datetime, pytz

def start():
    print("\n🚀 المصنع يعمل الآن بنظام (الرادار المباشر) - لا يوجد تلغرام")
    while True:
        try:
            now = datetime.datetime.now(pytz.timezone('Asia/Riyadh')).strftime("%I:%M:%S %p")
            # سحب السعر من بورصة بينانس مباشرة
            r = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT", timeout=10)
            price = float(r.json()['price'])
            print(f"[{now}] 🟡 الذهب: ${price:,.2f}")
        except:
            print(f"[{now}] 📡 محاولة استعادة الاتصال بالبورصة...")
        time.sleep(30)

if __name__ == "__main__":
    start()

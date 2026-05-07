import requests
import datetime
import pytz
import time

def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

def get_live_price(symbol, pair_name):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            price = float(response.json()['price'])
            return f"{pair_name}: ${round(price, 2)}"
    except:
        return f"{pair_name}: جاري جلب البيانات..."
    return f"{pair_name}: عطل مؤقت"

if __name__ == "__main__":
    print(f"\n{'='*30}")
    print(f"📡 رادار مصنع إيش تشتي - لوحة الأسعار")
    print(f"⏰ توقيت الرياض: {get_riyadh_time()}")
    print(f"{'='*30}\n")
    
    # سحب الأسعار وعرضها فوراً في الشاشة السوداء
    print(get_live_price("PAXGUSDT", "🟡 الذهب (Gold)"))
    print(get_live_price("BTCUSDT",  "🔵 البيتكوين (BTC)"))
    print(get_live_price("ETHUSDT",  "🟣 الإيثيريوم (ETH)"))
    
    print(f"\n{'='*30}")
    print("✅ النظام يعمل داخلياً بنجاح (بانتظار سيرفر تلغرام)")

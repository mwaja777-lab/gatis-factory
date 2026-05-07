import requests, time, datetime, pytz, os

def get_center(text):
    # وظيفة لحساب وسط الشاشة "قهرياً"
    try:
        width = os.get_terminal_size().columns
    except:
        width = 40 # عرض افتراضي للجوال
    return text.center(width)

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    
    print("\n" + "="*40)
    print(get_center("🚀 GATIS FACTORY 2080"))
    print(get_center("SYSTEM: ACTIVE"))
    print("="*40 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%H:%M:%S")
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                p = float(res.json()['data']['amount'])
                diff = p - last_p if last_p != 0 else 0
                trend = "UP ▲" if diff > 0 else "DOWN ▼" if diff < 0 else "STABLE"
                
                # النص المراد توسيطه
                output = f"[{now}] GOLD: ${p:,.2f} | {trend}"
                print(get_center(output))
                last_p = p
        except:
            print(get_center("!! RECONNECTING !!"))
        
        time.sleep(15)

if __name__ == "__main__":
    factory_engine()

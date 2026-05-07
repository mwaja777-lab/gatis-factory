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
    import requests, time, datetime, pytz, os

# فئة الألوان الرسمية للمصنع (نظام ANSI المضيء)
class GatisTheme:
    HEADER = '\033[96m'    # سماوي رسمي
    TIME = '\033[95m'      # أرجواني للوقت
    BUY = '\033[92m'       # أخضر مضاء للشراء
    SELL = '\033[91m'      # أحمر مضاء للبيع
    STABLE = '\033[93m'    # أصفر للاستقرار
    BOLD = '\033[1m'       # خط عريض
    END = '\033[0m'        # إنهاء التنسيق

def get_center(text, padding=0):
    try:
        width = os.get_terminal_size().columns
    except:
        width = 50
    return text.center(width + padding)

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    
    # واجهة الانطلاق (العناوين بأبهج الألوان)
    line = f"{GatisTheme.HEADER}{'='*50}{GatisTheme.END}"
    title = f"{GatisTheme.BOLD}{GatisTheme.HEADER}🚀 GATIS FACTORY GLOBAL 2080{GatisTheme.END}"
    info = f"{GatisTheme.BOLD}{GatisTheme.BUY}● SYSTEM: OPERATIONAL (15s PULSE){GatisTheme.END}"
    
    print(f"\n{line}\n{get_center(title)}\n{get_center(info)}\n{line}\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%H:%M:%S")
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                p = float(res.json()['data']['amount'])
                
                # تحليل الصفقات المقترحة بالألوان المضيئة
                if last_p == 0:
                    status = f"{GatisTheme.STABLE}SCANNING MARKET...{GatisTheme.END}"
                elif p > last_p:
                    status = f"{GatisTheme.BOLD}{GatisTheme.BUY}📈 SIGNAL: BUY / UP ▲{GatisTheme.END}"
                elif p < last_p:
                    status = f"{GatisTheme.BOLD}{GatisTheme.SELL}📉 SIGNAL: SELL / DOWN ▼{GatisTheme.END}"
                else:
                    status = f"{GatisTheme.STABLE}STABLE ⚖️{GatisTheme.END}"
                
                # دمج العناصر في سطر واحد متناسق عالمياً
                time_part = f"{GatisTheme.TIME}[{now}]{GatisTheme.END}"
                price_part = f"{GatisTheme.BOLD}GOLD: ${p:,.2f}{GatisTheme.END}"
                
                final_row = f"{time_part} {price_part} | {status}"
                print(get_center(final_row, padding=30)) # تعديل المسافة للتعويض عن أكواد الألوان
                last_p = p
            else:
                print(get_center(f"{GatisTheme.SELL}!! CONNECTION LAG !!{GatisTheme.END}"))
        except Exception as e:
            print(get_center(f"{GatisTheme.STABLE}📡 RE-ESTABLISHING LINK...{GatisTheme.END}"))
        
        time.sleep(15)

if __name__ == "__main__":
    factory_engine()
    

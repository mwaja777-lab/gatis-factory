import requests, time, datetime, pytz, os

# مصفوفة التنسيق العالمي - هوية "ايش تشتي"
class UI:
    GOLD = '\033[48;5;220m'  # ذهبي ماكينة
    GREY = '\033[48;5;250m'  # رصاصي ملكي
    RED  = '\033[48;5;196m'  # أحمر تداول
    GRN  = '\033[48;5;46m'   # أخضر تداول
    BLK  = '\033[30m'        # خط أسود
    WHT  = '\033[37m'        # خط أبيض
    BOLD = '\033[1m'
    END  = '\033[0m'

def get_width():
    try: return os.get_terminal_size().columns
    except: return 45

def start_factory():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    w = get_width()
    
    # تثبيت الشاشة ومنع الانزلاق
    os.system('clear')
    
    while True:
        try:
            res = requests.get(url, timeout=5).json()
            p = float(res['data']['amount'])
            now = datetime.datetime.now(tz).strftime("%H:%M:%S")
            
            # معالجة "ايش تشتي" بتقنية التباعد لضمان عدم الانعكاس
            # تم كتابتها بحروف مفردة مرتبة لتقرأها الشاشة بشكل سليم
            logo_label = f"{UI.GOLD}{UI.BLK}{UI.BOLD}  ا ي ش   ت ش ت ي  {UI.END}"
            title = "ا ل م ص ن ع   ا ل ع ا ل م ي"
            
            print(f"{UI.GREY}{UI.BLK}", end="") # تفعيل الرصاصي الملكي
            print("\n" + " " * w)
            print(logo_label.center(w + 15))
            print(f"{UI.BOLD}{title}".center(w))
            print("-" * w)
            
            # منطق الأسعار والنبض
            color = UI.GRN if p >= last_p else UI.RED
            trend = "▲" if p >= last_p else "▼"
            
            price_row = f" GOLD: ${p:,.2f} | {color}{UI.WHT} {trend} {UI.END}{UI.GREY}{UI.BLK} "
            print(price_row.center(w + 15))
            
            # التوقيت والموقع
            footer = f" {now} | RIYADH "
            print("\n" + footer.center(w))
            print(" " * w + UI.END)
            
            last_p = p
            time.sleep(15)
            os.system('clear') # إعادة الرسم للتثبيت الكامل
            
        except:
            time.sleep(5)

if __name__ == "__main__":
    start_factory()

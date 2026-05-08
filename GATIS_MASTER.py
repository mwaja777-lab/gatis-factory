import requests, time, datetime, pytz, os

# --- الهوية البصرية العالمية للمصنع ---
class Brand:
    GOLD_BG   = '\033[48;5;220m' # ذهبي لماع
    ROYAL_GRY = '\033[48;5;250m' # رصاصي ملكي
    RED_ZONE  = '\033[48;5;196m' # أحمر تداول
    GRN_ZONE  = '\033[48;5;46m'  # أخضر تداول
    ORNG_ZONE = '\033[48;5;208m' # برتقالي منسجم
    TEXT_BLK  = '\033[30m'       # خط أسود عريض
    TEXT_WHT  = '\033[37m'       # خط أبيض
    BOLD      = '\033[1m'
    END       = '\033[0m'

def get_screen_width():
    try: return os.get_terminal_size().columns
    except: return 50

def factory_prime_engine():
    # الإعدادات الزمنية والمكانية
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    w = get_screen_width()
    
    # تثبيت المصفوفات (مسح شامل للشاشة)
    os.system('clear' if os.name == 'posix' else 'cls')
    
    while True:
        try:
            res = requests.get(url, timeout=10).json()
            p = float(res['data']['amount'])
            now = datetime.datetime.now(tz)
            time_stamp = now.strftime("%H:%M:%S")
            date_stamp = now.strftime("%Y/%m/%d")
            
            # --- رسم الواجهة الديناميكية المطاطة ---
            print(f"{Brand.ROYAL_GRY}{Brand.TEXT_BLK}", end="")
            print("\n" + " " * w)
            
            # 1. اللوجو الذهبي "ايش تشتي"
            logo = f"{Brand.GOLD_BG}{Brand.TEXT_BLK}{Brand.BOLD}  ا ي ش   ت ش ت ي  {Brand.END}{Brand.ROYAL_GRY}{Brand.TEXT_BLK}"
            print(logo.center(w + 20))
            
            # 2. اسم المصنع والسياسة الاستراتيجية
            factory_title = "ا ل م ص ن ع   ا ل ع ا ل م ي   ل ل ت د ا و ل"
            vision = "GLOBAL STANDARDS: 2080 AD"
            print(f"{Brand.BOLD}{factory_title}".center(w))
            print(f"{vision}".center(w))
            print("-" * w)
            
            # 3. جدول البيانات (بدون خطوط لضمان الوضوح)
            status_color = Brand.GRN_ZONE if p >= last_p else Brand.RED_ZONE
            trend_icon = "▲" if p >= last_p else "▼"
            trend_text = "ا ر ت ف ا ع" if p >= last_p else "ه ب و ط"
            
            # عرض سعر الذهب
            price_line = f" GOLD: ${p:,.2f}  |  {status_color}{Brand.TEXT_WHT} {trend_icon} {trend_text} {Brand.END}{Brand.ROYAL_GRY}{Brand.TEXT_BLK}"
            print(price_line.center(w + 20))
            
            # 4. منطقة الفارق (الاسبريد) بالبرتقالي
            spread_label = f"{Brand.ORNG_ZONE}  S P R E A D :  1.00  {Brand.END}{Brand.ROYAL_GRY}{Brand.TEXT_BLK}"
            print("\n" + spread_label.center(w + 20))
            
            # 5. منطقة الصفقات المرشحة (عزل تام)
            print("\n" + "=" * w)
            target_text = "ا ل ص ف ق ا ت   ا ل م ر ش ح ة"
            print(f"{Brand.BOLD}{target_text}".center(w))
            print("TARGET: 2450.00 | 48H".center(w))
            
            # 6. التذييل الزمني (الرياض)
            footer = f" {date_stamp} | {time_stamp} | RIYADH "
            print("\n" + footer.center(w))
            print(" " * w + f"{Brand.END}")
            
            last_p = p
            time.sleep(15) # نبضة المصنع المعتمدة
            os.system('clear' if os.name == 'posix' else 'cls') # إعادة التثبيت المغناطيسي
            
        except Exception as e:
            time.sleep(5)

if __name__ == "__main__":
    factory_prime_engine()

  

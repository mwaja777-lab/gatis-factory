import requests, time, datetime, pytz, os
from arabic_reshaper import reshape
from bidi.algorithm import get_display

# --- محرك التنسيق العالمي "ايش تشتي" ---
class GlobalUI:
    # ألوان الخلفيات (الملكية)
    BG_GREY = '\033[48;5;250m'    # رصاصي ملكي
    BG_GOLD = '\033[48;5;220m'    # ذهبي ماكينة
    BG_RED  = '\033[48;5;196m'    # أحمر فاتح
    BG_GREEN = '\033[48;5;46m'    # أخضر زمردي
    BG_ORANGE = '\033[48;5;208m'  # برتقالي منسجم
    
    # ألوان الخطوط
    TEXT_BLACK = '\033[38;5;16m'
    TEXT_WHITE = '\033[38;5;15m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def fix_ar(text):
    try:
        return get_display(reshape(text))
    except: return text

def get_width():
    try: return os.get_terminal_size().columns
    except: return 60

def draw_ui():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    w = get_width()
    
    # تنظيف الشاشة وتثبيتها
    os.system('clear' if os.name == 'posix' else 'cls')
    
    while True:
        try:
            res = requests.get(url, timeout=5).json()
            p = float(res['data']['amount'])
            now = datetime.datetime.now(tz)
            
            # 1. شعار المصنع (اللوجو الذهبي)
            logo_text = fix_ar(" ايش تشتي ")
            logo = f"{GlobalUI.BG_GOLD}{GlobalUI.TEXT_BLACK}{GlobalUI.BOLD}  {logo_text}  {GlobalUI.RESET}"
            
            # 2. معلومات الجلسة والوقت
            time_str = now.strftime("%H:%M:%S")
            date_str = fix_ar(now.strftime("%Y/%m/%d"))
            session = fix_ar("الجلسة: الآسيوية/الأوروبية")
            
            # بناء العرض
            print(f"{GlobalUI.BG_GREY}{GlobalUI.TEXT_BLACK}", end="") # تفعيل الخلفية الرصاصية
            print("\n" + " " * w) 
            print(logo.center(w + 20))
            print(f"{GlobalUI.BOLD}{fix_ar('المصنع العالمي للتداول الذكي')}".center(w))
            print("-" * w)
            
            # 3. جدول البيانات الأساسي (بدون خطوط خلايا - بنظام المسافات الثابتة)
            headers = f"{fix_ar('السلعة')} | {fix_ar('السعر')} | {fix_ar('شراء')} | {fix_ar('بيع')} | {fix_ar('الحالة')}"
            print(headers.center(w))
            
            # منطق الألوان والحالة
            color_buy = GlobalUI.BG_GREEN
            color_sell = GlobalUI.BG_RED
            trend_icon = "⚪"
            trend_text = fix_ar("مستقر")
            
            if last_p != 0:
                if p > last_p:
                    trend_icon = "▲"
                    trend_text = fix_ar("ارتفاع")
                elif p < last_p:
                    trend_icon = "▼"
                    trend_text = fix_ar("هبوط")

            data_row = f"{fix_ar('الذهب')} | {p:,.2f} | {color_buy} {p+0.5:,.2f} {GlobalUI.RESET}{GlobalUI.BG_GREY} | {color_sell} {p-0.5:,.2f} {GlobalUI.RESET}{GlobalUI.BG_GREY} | {trend_icon} {trend_text}"
            print(data_row.center(w + 20))
            
            # 4. الفرق (الاسبريد) بالبرتقالي
            spread = f"{GlobalUI.BG_ORANGE}{GlobalUI.TEXT_BLACK} {fix_ar('الفرق بين البيع والشراء')}: 1.00 {GlobalUI.RESET}{GlobalUI.BG_GREY}"
            print("\n" + spread.center(w + 20))
            
            # 5. قسم الصفقات المرشحة
            print("\n" + "=" * w)
            print(f"{GlobalUI.BOLD}{fix_ar('--- الصفقات المرشحة للأيام القادمة ---')}".center(w))
            print(f"{fix_ar('هدف متوسط: 2450.00 | المدة: 48 ساعة')}".center(w))
            
            # 6. التذييل (الوقت والرياض)
            footer = f"{date_str} | {fix_ar('الرياض')} | {time_str}"
            print("\n" + footer.center(w))
            print(" " * w + f"{GlobalUI.RESET}")
            
            last_p = p
            time.sleep(15)
            os.system('clear' if os.name == 'posix' else 'cls') # إعادة المسح للتثبيت
            
        except Exception as e:
            print(fix_ar("جاري إعادة الاتصال بالنظام..."))
            time.sleep(5)

if __name__ == "__main__":
    draw_ui()

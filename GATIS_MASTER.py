import requests, time, datetime, pytz, os

class GlobalUI:
    BG_GREY = '\033[48;5;250m'
    BG_GOLD = '\033[48;5;220m'
    BG_RED  = '\033[48;5;196m'
    BG_GREEN = '\033[48;5;46m'
    BG_ORANGE = '\033[48;5;208m'
    TEXT_BLACK = '\033[30m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def reverse_fix(text):
    # خدعة عكس العكس لضمان القراءة الصحيحة في شاشات الجوال
    return text[::-1]

def get_width():
    try: return os.get_terminal_size().columns
    except: return 45

def draw_ui():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    last_p = 0
    w = get_width()
    
    while True:
        try:
            os.system('clear')
            res = requests.get(url, timeout=5).json()
            p = float(res['data']['amount'])
            now = datetime.datetime.now(tz).strftime("%H:%M:%S")
            
            # اللوجو الذهبي - معكوس يدوياً ليظهر صحيحاً عندك
            name = " ي ت ش ت   ش ي ا " # مسافات لضمان عدم الالتصاق
            logo = f"{GlobalUI.BG_GOLD}{GlobalUI.TEXT_BLACK}{GlobalUI.BOLD} {name} {GlobalUI.RESET}"
            
            print(f"{GlobalUI.BG_GREY}{GlobalUI.TEXT_BLACK}")
            print("\n" + " " * w)
            print(logo.center(w + 15))
            print(f"{GlobalUI.BOLD}{reverse_fix('المصنع العالمي للتداول الذكي')}".center(w))
            print("-" * w)
            
            # البيانات
            status = "عافترم" if p > last_p else "طوبهه"
            color = GlobalUI.BG_GREEN if p > last_p else GlobalUI.BG_RED
            
            row = f"{p:,.2f} | {color} {status} {GlobalUI.RESET}{GlobalUI.BG_GREY}"
            print(row.center(w + 10))
            
            print("\n" + f"{now} | {reverse_fix('الرياض')}".center(w))
            print(" " * w + GlobalUI.RESET)
            
            last_p = p
            time.sleep(15)
        except:
            time.sleep(5)

if __name__ == "__main__":
    draw_ui()
            

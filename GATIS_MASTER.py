import requests, time, datetime, pytz, os

# محرك الألوان المتقدم لرؤية 2080
class GatisUI:
    GOLD_BG = '\033[43m'    # خلفية ذهبية
    BLACK_TEXT = '\033[30m' # خط أسود
    BOLD = '\033[1m'        # خط غليظ
    CYAN = '\033[96m'       # سماوي للعناوين
    PURPLE = '\033[95m'     # أرجواني للوقت
    GREEN = '\033[92m'      # أخضر مضاء (شراء)
    RED = '\033[91m'        # أحمر مضاء (بيع)
    YELLOW = '\033[93m'     # أصفر (استقرار)
    END = '\033[0m'         # إنهاء التنسيق

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
    
    # اعتماد اسم المصنع بالخلفية الذهبية والخط الأسود
    # تم تغليظ "ايش تشتي" برمجياً
    factory_name = f"{GatisUI.GOLD_BG}{GatisUI.BLACK_TEXT} المصنع العالمي للتداول الذكي \"{GatisUI.BOLD}ايش تشتي{GatisUI.END}{GatisUI.GOLD_BG}{GatisUI.BLACK_TEXT}\" {GatisUI.END}"
    
    status_tag = f"{GatisUI.BOLD}{GatisUI.CYAN}● GLOBAL STANDARDS: 2080 AD{GatisUI.END}"
    line = f"{GatisUI.CYAN}{'='*55}{GatisUI.END}"

    print(f"\n{line}")
    print(get_center(factory_name, padding=20))
    print(get_center(status_tag))
    print(f"{line}\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%H:%M:%S")
            res = requests.get(url, timeout=10)
            if res.status_code == 200:
                p = float(res.json()['data']['amount'])
                
                # منطق الألوان المضاءة للنبضات
                if last_p == 0:
                    signal = f"{GatisUI.YELLOW}SCANNING...{GatisUI.END}"
                elif p > last_p:
                    signal = f"{GatisUI.BOLD}{GatisUI.GREEN}📈 BUY / UP ▲{GatisUI.END}"
                elif p < last_p:
                    signal = f"{GatisUI.BOLD}{GatisUI.RED}📉 SELL / DOWN ▼{GatisUI.END}"
                else:
                    signal = f"{GatisUI.YELLOW}STABLE{GatisUI.END}"
                
                time_str = f"{GatisUI.PURPLE}[{now}]{GatisUI.END}"
                price_str = f"{GatisUI.BOLD}GOLD: ${p:,.2f}{GatisUI.END}"
                
                output = f"{time_str} {price_str} | {signal}"
                print(get_center(output, padding=30))
                last_p = p
        except:
            print(get_center(f"{GatisUI.YELLOW}>> RE-CONNECTING...{GatisUI.END}"))
        
        time.sleep(15)

if __name__ == "__main__":
    factory_engine()

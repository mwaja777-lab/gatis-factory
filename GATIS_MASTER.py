import requests, time, datetime, pytz, os

class Theme:
    GOLD = '\033[38;5;220m'
    GRY_L = '\033[48;5;252m' # لامع
    GRY_D = '\033[48;5;245m' # مطفي
    RED = '\033[38;5;196m'
    GRN = '\033[38;5;46m'
    ORG = '\033[38;5;208m'
    BLK = '\033[30m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def draw_ui():
    tz = pytz.timezone('Asia/Riyadh')
    data = {
        "الذهب": [2324.49, 2325.10, "▲", 2323.80, "صعود: جيوسياسي"],
        "الفضة": [29.15, 29.22, "▼", 29.10, "منطقة توقف"],
        "النفط": [82.14, 82.30, "⚪", 82.00, "مستقر: عرض"],
        "داو جونز": [39120, 39155, "▲", 39085, "صعود: تقني"],
        "بيتكوين": [64210, 64310, "▼", 64115, "هبوط: تصحيح"]
    }
    
    while True:
        os.system('clear')
        now = datetime.datetime.now(tz)
        
        # 1. الشعار الذهبي (كتلة واحدة)
        print(f"{Theme.GOLD}{Theme.BOLD}   ⚜️  ايش تشتي  ⚜️   {Theme.RESET}".center(50))
        
        # 2. برواز الصفقات المرشحة
        print(f"\n{Theme.BOLD}┌── رادار الصفقات ──┐{Theme.RESET}")
        print(f"│ الذهب   | شراء    │\n│ بيتكوين | بيع     │\n└───────────────────┘")

        # 3. ترويسة الجدول (الأعمدة السبعة)
        head = f"{'ت':<2} | {'السلعة':<8} | {'السعر':<8} | {'شراء':<8} | {'ح':<2} | {'بيع':<8} | {'التحليل'}"
        print(f"\n{Theme.BOLD}{head}{Theme.RESET}")
        print("-" * 65)

        # 4. الأسطر (كل سلعة سطر واحد فقط)
        for i, (name, v) in enumerate(data.items(), 1):
            bg = Theme.GRY_L if i % 2 != 0 else Theme.GRY_D
            # تلوين الحالة
            c = Theme.GRN if v[2] == "▲" else Theme.RED if v[2] == "▼" else Theme.RESET
            
            # بناء السطر بدقة الخلايا
            row = f"{bg}{Theme.BLK}{i:<2} | {name:<8} | {v[0]:<8,.2f} | {Theme.GRN}{v[1]:<8,.2f}{Theme.RESET}{bg}{Theme.BLK} | {c}{v[2]:<2}{Theme.RESET}{bg}{Theme.BLK} | {Theme.RED}{v[3]:<8,.2f}{Theme.RESET}{bg}{Theme.BLK} | {v[4]}{Theme.RESET}"
            print(row)

        print(f"\n{now.strftime('%H:%M:%S')} | RIYADH".center(65))
        time.sleep(15)

if __name__ == "__main__":
    draw_ui()

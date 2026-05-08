import requests, time, datetime, pytz, os

# --- الهوية البصرية العالمية (ANSI 256-Color) ---
class Theme:
    GOLD_TEXT = '\033[38;5;220m'
    GOLD_BG   = '\033[48;5;220m'
    ROYAL_GRY_L = '\033[48;5;252m' # رصاصي لامع
    ROYAL_GRY_D = '\033[48;5;245m' # رصاصي مطفي
    RED_LIT   = '\033[38;5;196m'
    GRN_LIT   = '\033[38;5;46m'
    ORG_LIT   = '\033[38;5;208m'
    BLK       = '\033[30m'
    WHT       = '\033[37m'
    BOLD      = '\033[1m'
    RESET     = '\033[0m'

def get_w():
    try: return os.get_terminal_size().columns
    except: return 60

def fetch_data():
    # محاكاة لجلب البيانات لضمان عدم توقف الكود (سيتم ربطها بـ API لاحقاً)
    return {
        "الذهب": [2324.49, 2325.10, "▲", 2323.80, "صعود: توترات جيوسياسية"],
        "الفضة": [29.15, 29.22, "▼", 29.10, "منطقة توقف (ضبابية)"],
        "النفط": [82.14, 82.30, "⚪", 82.00, "مستقر: توازن العرض"],
        "داو جونز": [39120, 39155, "▲", 39085, "صعود: مؤشرات نمو تقني"],
        "بيتكوين": [64210, 64310, "▼", 64115, "هبوط: تصحيح سعري"]
    }

def draw_factory():
    tz = pytz.timezone('Asia/Riyadh')
    w = get_w()
    
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        data = fetch_data()
        now = datetime.datetime.now(tz)
        
        # 1. الشعار الذهبي المنحوت (ايش تشتي)
        logo = f"{Theme.GOLD_TEXT}{Theme.BOLD}╔══════════════════════════════════════╗\n║        ⚜️  ايش تشتي  ⚜️         ║\n╚══════════════════════════════════════╝{Theme.RESET}"
        print(logo.center(w + 10))

        # 2. برواز الصفقات المرشحة (أعلى اليمين برمجياً)
        print(f"\n{Theme.BOLD}┌─ رادار الصفقات ────────┐{Theme.RESET}")
        print(f"│ الذهب   | 2324 | شراء  │")
        print(f"│ بيتكوين | 6421 | بيع   │")
        print(f"└────────────────────────┘")

        # 3. ترويسة الجدول الشامل
        header = f"{Theme.BOLD}{'ت':<3} {'السلعة':<10} {'السعر الآن':<12} {'شراء':<10} {'ح':<3} {'بيع':<10} {'التحليل الجيوسياسي'}"
        print(f"\n{Theme.WHT}{header}{Theme.RESET}")
        print("-" * w)

        # 4. بناء الأسطر (رصاصي لامع/مطفي)
        for i, (name, vals) in enumerate(data.items(), 1):
            bg = Theme.ROYAL_GRY_L if i % 2 != 0 else Theme.ROYAL_GRY_D
            status_clr = Theme.GRN_LIT if vals[2] == "▲" else Theme.RED_LIT if vals[2] == "▼" else Theme.WHT
            
            # عمود التوقع مع منطق "توقف"
            analysis = vals[4]
            if "توقف" in analysis: analysis = f"{Theme.ORG_LIT}{analysis}{Theme.RESET}{bg}{Theme.BLK}"

            row = f"{bg}{Theme.BLK}{i:<3} {name:<10} {vals[0]:<12,.2f} {Theme.GRN_LIT}{vals[1]:<10,.2f}{Theme.RESET}{bg}{Theme.BLK} {status_clr}{vals[2]:<3}{Theme.RESET}{bg}{Theme.BLK} {Theme.RED_LIT}{vals[3]:<10,.2f}{Theme.RESET}{bg}{Theme.BLK} {analysis}{' ' * (w-len(str(vals)))}{Theme.RESET}"
            print(row)

        # 5. شريط الحالة السفلي
        footer = f"\n{Theme.BOLD}[ {now.strftime('%Y/%m/%d')} ] | [ {now.strftime('%H:%M:%S')} ] | [ الرياض ]{Theme.RESET}"
        print(footer.center(w))

        time.sleep(15)

if __name__ == "__main__":
    draw_factory()
      

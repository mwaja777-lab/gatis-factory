import requests
import datetime
import time
import pytz

# --- [1] بيانات الهوية الرقمية ---
TELEGRAM_TOKEN = "8728845103:AAGFndJW78WXNfAfNSXOiOanyqU-ItqqmiA"
CHAT_ID = "6586845943"

# --- [2] محرك الوقت (توقيت الرياض الصارم 12H) ---
def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

# --- [3] قناة الاتصال المؤمنة ---
def send_telegram_report(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.status_code == 200
    except Exception as e:
        print(f"Connection Error: {e}")
        return False

# --- [4] الوظيفة التشغيلية (الرادار) ---
def run_master_radar():
    riyadh_now = get_riyadh_time()
    msg = (
        f"🚀 *مصنع إيش تشتي - ملف الماستر*\n"
        f"━━━━━━━━━━━━━━━\n"
        f"✅ النظام: متصل وجاهز\n"
        f"⏰ التوقيت: {riyadh_now}\n"
        f"🌍 الموقع: الرياض (المقر الرئيسي)\n"
        f"━━━━━━━━━━━━━━━\n"
        f"📡 *الحالة:* بانتظار ربط بيانات كابيتال الحية..."
    )
    send_telegram_report(msg)

if __name__ == "__main__":
    print(f"--- [MASTER] Started at {get_riyadh_time()} ---")
    run_master_radar()

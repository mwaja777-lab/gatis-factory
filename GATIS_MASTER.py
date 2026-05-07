import requests
import datetime
import pytz

# --- [1] الهوية الرقمية (تأكد من وجود الشرطة قبل حرف A) ---
TELEGRAM_TOKEN = "8728845103:AAGFndJW78WXNfAfNSXOiOanyqU-Itqqmi-A"
CHAT_ID = "6586845943"

def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

def send_telegram_signal():
    riyadh_now = get_riyadh_time()
    text = f"🚀 *مصنع إيش تشتي*\n✅ تم الربط بنجاح\n⏰ الوقت: {riyadh_now}"
    
    proxies = {'http': 'http://proxy.server:3128', 'https': 'http://proxy.server:3128'}
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    try:
        res = requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}, proxies=proxies, timeout=15)
        if res.status_code == 200:
            print(f"✅ تم الإرسال بنجاح في {riyadh_now}")
        else:
            print(f"❌ خطأ {res.status_code}: تأكد من التوكن")
    except Exception as e:
        print(f"⚠️ عطل في الشبكة: {e}")

if __name__ == "__main__":
    print(f"--- {get_riyadh_time()} بدء التشغيل ---")
    send_telegram_signal()

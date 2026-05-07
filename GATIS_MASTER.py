import requests
import datetime
import pytz
import time

# --- إعدادات الهوية ---
TELEGRAM_TOKEN = "8728845103:AAGFndJW78WXNfAfNSXOiOanyqU-Itqqmi-A"
CHAT_ID = "6586845943"

def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

def send_telegram_signal():
    riyadh_now = get_riyadh_time()
    text = f"🚀 *مصنع إيش تشتي*\n⏰ الوقت: {riyadh_now}\n✅ النبضة تعمل بنجاح!"
    
    # إعدادات الوسيط الإلزامية للحساب المجاني
    proxies = {
        'http': 'http://proxy.server:3128',
        'https': 'http://proxy.server:3128'
    }
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    try:
        response = requests.post(
            url, 
            json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}, 
            proxies=proxies, 
            timeout=15
        )
        if response.status_code == 200:
            print(f"✅ تم الإرسال بنجاح في {riyadh_now}")
        else:
            print(f"❌ خطأ من تلغرام: {response.status_code}")
    except Exception as e:
        print(f"⚠️ فشل الاتصال بالسيرفر: {e}")

if __name__ == "__main__":
    print(f"--- بدء التشغيل: {get_riyadh_time()} ---")
    send_telegram_signal()

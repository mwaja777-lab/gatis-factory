import requests
import datetime
import pytz

# --- [1] الهوية الرقمية ---
TELEGRAM_TOKEN = "8728845103:AAGFndJW78WXNfAfNSXOiOanyqU-ItqqmiA"
CHAT_ID = "6586845943"

# --- [2] محرك الوقت (الرياض 12H) ---
def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

# --- [3] جندي المراسلة (مع كسر الحجب للحسابات المجانية) ---
def send_telegram_signal():
    riyadh_now = get_riyadh_time()
    text = f"🚀 *مصنع إيش تشتي - نداء الماستر*\n\n✅ تم كسر جدار الحماية بنجاح\n⏰ التوقيت: {riyadh_now}\n📡 الحالة: متصل بالسحاب"
    
    # إعدادات الوسيط (Proxy) للحسابات المجانية
    proxies = {
        'http': 'http://proxy.server:3128',
        'https': 'http://proxy.server:3128',
    }
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    
    try:
        # محاولة الإرسال عبر الوسيط
        response = requests.post(url, json=payload, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"✅ Success! Message sent at {riyadh_now}")
        else:
            print(f"❌ Failed! Status Code: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    send_telegram_signal()

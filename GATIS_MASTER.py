import requests
import datetime
import pytz

# --- [1] الهوية الرقمية (تأكد من عدم وجود مسافات) ---
TELEGRAM_TOKEN = "8728845103:AAGFndJW78WXNfAfNSXOiOanyqU-Itqqmi-A"
CHAT_ID = "6586845943"

def get_riyadh_time():
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz)
    return now.strftime("%I:%M:%S %p")

def send_telegram_signal():
    riyadh_now = get_riyadh_time()
    text = f"🚀 *نداء الماستر*\n✅ تم تشغيل المصنع بنجاح\n⏰ الوقت: {riyadh_now}"
    
    # إعدادات الوسيط (Proxy)
    proxies = {'http': 'http://proxy.server:3128', 'https': 'http://proxy.server:3128'}
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    try:
        res = requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}, proxies=proxies, timeout=15)
        if res.status_code == 200:
            print(f"✅ مبروك! وصلت الرسالة في {riyadh_now}")
        else:
            print(f"❌ خطأ {res.status_code}: هناك مشكلة في رقم الهوية (Token)")
    except Exception as e:
        print(f"⚠️ السيرفر مشغول، حاول مجدداً: {e}")

if __name__ == "__main__":
    print(f"--- محاولة إرسال النبضة: {get_riyadh_time()} ---")
    send_telegram_signal()

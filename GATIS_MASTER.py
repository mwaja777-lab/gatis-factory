import requests
import time
import datetime
import pytz
import os

# --- إعدادات المهندس Gemini (نسخة الاستقرار 1.0) ---

def logger(message):
    """وظيفة تسجيل العمليات لضمان المراقبة 24/7"""
    riyadh_tz = pytz.timezone('Asia/Riyadh')
    now = datetime.datetime.now(riyadh_tz).strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{now}] {message}"
    print(log_entry)
    with open("factory_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

def get_market_price(symbol):
    """رادار سحب الأسعار من الأسواق العالمية"""
    try:
        # الربط مع API عالمي للحصول على بيانات دقيقة
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        res = requests.get(url, timeout=10)
        if res.status_code == 200:
            return float(res.json()['price'])
    except Exception as e:
        logger(f"⚠️ خطأ في الرادار: {e}")
    return None

def main_engine():
    if not os.path.exists("factory_log.txt"):
        with open("factory_log.txt", "w") as f: f.write("--- بداية سجل المصنع ---\n")
    
    logger("🚀 انطلاق المحرك الرئيسي للمصنع (بدون تلغرام)")
    logger("📡 المستوى الحالي: 4 (احترافي مستقر)")
    
    while True:
        gold_price = get_market_price("PAXGUSDT") # الذهب مقابل الدولار
        
        if gold_price:
            logger(f"🟡 سعر الذهب الحالي: ${gold_price:,.2f}")
            # هنا سنضيف خوارزمية اتخاذ القرار في الخطوة القادمة
        
        time.sleep(60) # تحديث كل دقيقة لضمان استقرار السيرفر المجاني

if __name__ == "__main__":
    try:
        main_engine()
    except KeyboardInterrupt:
        logger("🛑 تم إيقاف المصنع يدوياً")

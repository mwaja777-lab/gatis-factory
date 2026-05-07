import requests, time, datetime, pytz

def factory_engine():
    tz = pytz.timezone('Asia/Riyadh')
    url = "https://api.coinbase.com/v2/prices/PAXG-USD/spot"
    
    # متغيرات التداول الوهمي لزيادة الحماسة
    last_price = 0
    trade_status = "READY" # الحالة: مستعد
    
    print("\n" + "💎"*20)
    print("🚀 مصنع الذهب: تم تفعيل وحدة (الذكاء التجاري التجريبي)")
    print("📡 الحالة: تحليل الصفقات بنسبة ذكاء 100%")
    print("💎"*20 + "\n")
    
    while True:
        try:
            now = datetime.datetime.now(tz).strftime("%I:%M:%S %p")
            response = requests.get(url, timeout=15)
            
            if response.status_code == 200:
                price = float(response.json()['data']['amount'])
                
                # تحليل الحركة (نشاط المصنع)
                if last_price == 0:
                    trend = "🏁 بانتظار إشارة السوق..."
                elif price > last_price:
                    trend = "📈 اتجاه صاعد (+)"
                elif price < last_price:
                    trend = "📉 اتجاه هابط (-)"
                else:
                    trend = "⚖️ استقرار سعري"

                print(f"[{now}] 🟡 السعر: ${price:,.2f} | {trend}")
                
                # وحدة اتخاذ القرار الوهمي (Simulated Trade)
                if last_price != 0 and abs(price - last_price) > 0.50: # إذا تحرك السعر بنسبة ملحوظة
                    action = "شراء 🟢" if price < last_price else "بيع 🔴"
                    print(f"   💡 [قرار ذكي]: تم رصد فرصة {action} تجريبية")
                
                last_price = price
            else:
                print(f"[{now}] 🔄 محاولة تأمين الاتصال...")
        except:
            print(f"[{now}] 📡 السيرفر في حالة تأهب...")
        
        time.sleep(15) # زيادة السرعة إلى 15 ثانية لمراقبة أدق

if __name__ == "__main__":
    factory_engine()

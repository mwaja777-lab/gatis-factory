import os, datetime, time, threading, random

ENV = os.environ.get("ENV", "DEMO")
API_KEY = os.environ.get("API_KEY", "zcSppmualzfGe8l")
API_PASSWORD = os.environ.get("API_PASSWORD", "Mllyar$7")
BASE_URL = "https://demo-api-capital.backend-capital.com/api/v2/" if ENV == "DEMO" else "https://api-capital.backend-capital.com/api/v2/"
ACCOUNTS = ["Master", "Sub-1", "Sub-2", "Sub-3", "Sub-4", "Sub-5", "Sub-6", "Sub-7", "Sub-8", "Sub-9"]

class DecisionEngine:
    def decide(self, price, rsi):
        s1 = 1 if rsi < 30 else (-1 if rsi > 70 else 0)
        s2 = 1 if price > 4600 else (-1 if price < 4580 else 0)
        s3 = 1 if rsi > 50 else (-1 if rsi < 40 else 0)
        total = s1 + s2 + s3
        if total >= 2: return "BUY"
        if total <= -2: return "SELL"
        return "HOLD"

class SingleBot:
    def __init__(self, label):
        self.label = label
        self.decision = DecisionEngine()
        self.balance = 10000.0
        self.position = None
        self.daily_start_balance = self.balance
        self.is_cooling_down = False
        self.cooldown_end_time = None

    def check_risk(self, required_margin):
        max_margin = self.balance * 0.2
        if required_margin > max_margin:
            return False, f"Margin {required_margin:.2f} > Limit {max_margin:.2f}"
        return True, "OK"

    def check_cooldown(self):
        if self.is_cooling_down:
            if datetime.datetime.now() < self.cooldown_end_time:
                return True
            self.is_cooling_down = False
            self.daily_start_balance = self.balance
        daily_loss = ((self.daily_start_balance - self.balance) / self.daily_start_balance) * 100
        if daily_loss >= 10.0:
            self.is_cooling_down = True
            self.cooldown_end_time = datetime.datetime.now() + datetime.timedelta(hours=24)
            print(f"[{self.label}] COOLING DOWN. Loss: {daily_loss:.2f}%")
            return True
        return False

    def run(self):
        print(f"[{self.label}] Bot started.")
        while True:
            if self.check_cooldown():
                time.sleep(60)
                continue
            price = 4600 + random.uniform(-20, 20)
            rsi = random.randint(20, 80)
            signal = self.decision.decide(price, rsi)
            print(f"[{self.label}] Price={price:.2f} RSI={rsi} Signal={signal}")
            if signal == "BUY" and self.position is None:
                margin_required = price * 0.1 / 10.0
                safe, msg = self.check_risk(margin_required)
                if safe:
                    self.position = {"price": price, "size": 0.1}
                    print(f">>> {self.label} OPEN BUY")
                else:
                    print(f"[{self.label}] BLOCKED: {msg}")
            elif signal == "SELL" and self.position is not None:
                pnl = (price - self.position["price"]) * self.position["size"]
                self.balance += pnl
                print(f"<<< {self.label} CLOSE PnL={pnl:.2f}")
                self.position = None
            time.sleep(5)

if __name__ == "__main__":
    print(f"GATIS UNIFIED | ENV={ENV} | Accounts: {len(ACCOUNTS)}")
    threads = []
    for acc in ACCOUNTS:
        bot = SingleBot(acc)
        t = threading.Thread(target=bot.run)
        t.start()
        threads.append(t)
    try:
        for t in threads: t.join()
    except KeyboardInterrupt:
        print("GATIS Stopped.")

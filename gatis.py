import os, datetime, time, threading, random

API_KEY = os.environ.get("API_KEY", "zcSppmualzfGe8l")
API_PASSWORD = os.environ.get("API_PASSWORD", "Mllyar$7")
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

    def run(self):
        print(f"[{self.label}] Bot started.")
        while True:
            price = 4600 + random.uniform(-20, 20)
            rsi = random.randint(20, 80)
            signal = self.decision.decide(price, rsi)
            print(f"[{self.label}] Price={price:.2f} RSI={rsi} Signal={signal}")
            if signal == "BUY" and self.position is None:
                self.position = {"price": price, "size": 0.1}
                print(f">>> {self.label} OPEN BUY")
            elif signal == "SELL" and self.position is not None:
                pnl = (price - self.position["price"]) * self.position["size"]
                self.balance += pnl
                print(f"<<< {self.label} CLOSE PnL={pnl:.2f}")
                self.position = None
            time.sleep(5)

if __name__ == "__main__":
    print(f"GATIS UNIFIED | Accounts: {len(ACCOUNTS)}")
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

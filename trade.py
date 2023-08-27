class Trade:
    def __init__(self) -> None:
        pass
    
    def price_limit(self, now_price):
        if now_price >= 50000000:            
            return {
                "up": now_price + 10000000,
                "down": now_price - 10000000
            }
        
        calc_price = now_price
        count = 0
        while calc_price >= 700:
            calc_price = calc_price / 10
            count += 1
        
        time = 10 ** count

        if now_price < 100 * time:
            if now_price < 100:
                return {
                    "up": now_price + 30,
                    "down": now_price - 30
                }
            return {
                "up": now_price + 15 * time,
                "down": now_price - 15 * time
            }
        elif time > 0 and now_price < 150 * time:
            return {
                "up": now_price + 30 * time,
                "down": now_price - 30 * time
            }
        elif now_price < 200 * time:
            if now_price < 200:
                return {
                    "up": now_price + 50 ,
                    "down": now_price - 50
                }
            return {
                "up": now_price + 40 * time,
                "down": now_price - 40 * time
            }
        elif time != 0 and now_price < 300 * time:
            return {
                "up": now_price + 50 * time,
                "down": now_price - 50 * time
            }
        elif now_price < 500 * time:
            if now_price < 500:
                return {
                    "up": now_price + 80 ,
                    "down": now_price - 80
                }
            return {
                "up": now_price + 70 * time,
                "down": now_price - 70 * time
            }
        elif now_price < 700 * time:
            return {
                "up": now_price + 100 * time,
                "down": now_price - 100 * time
            }
        else:
            return None

    def add(self, a,b):
        return a + b
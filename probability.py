class Probability:

    def __init__(self) -> None:
        pass
    
    def calc_kelly(self, odds, winning_probabillity) -> float:
        return (winning_probabillity * (odds + 1) - 1) / winning_probabillity
    
    def calc_edge(self, winning_probabillity: float, profit: int, loss: int) -> float:
        return profit * winning_probabillity - loss * (1 - winning_probabillity)
    
    def calc_odds(self, upper_price: int, now_price: int) -> float:
        return (upper_price - now_price) / now_price
    
    def calc_other_kelly(self, odds: float, edge: float) -> float:
        return edge / odds
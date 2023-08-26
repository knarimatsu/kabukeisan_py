EXPENSIVE = "Expensive"
VALUE = "Value"

class Corporation():
        
    def __init__(self) -> None:
        pass
    
    def calc_deep_value(self, current_asset: int, liability: int, market_cap: int) -> str:
        deep_value = (current_asset - liability) / 3 * 2
        
        if market_cap > deep_value:
            return EXPENSIVE
        return VALUE
        
    def calc_detail_deep_value(
        self,
        cash: int,
        accounts_receivable: int,
        inventories: int,
        trade_security: int,
        land: int,
        investment_securities: int,
        long_term_loans: int,
        liabilities: int,
        market_cap: int
    ) -> str:
        asset = cash + accounts_receivable * 0.8 + (inventories + long_term_loans ) * 0.6 + land / 2 + (trade_security + investment_securities) * 0.75
        value = asset - liabilities
        if value > market_cap:
            return EXPENSIVE
        return VALUE
class Macro:

    def __init__(self) -> None:
        pass
    
    def buffet_index(self, total_market_cap, nominal_gdp) -> str:
        """
        バフェット指数
        引数
            該当国総時価総額: int
            該当国の名目GDP: int
        戻り値
            割高/割安: String
        """
        
        try:
            result = total_market_cap / nominal_gdp
            if result >= 1:
                return "割高"
            else:
                return "割安"
        except ZeroDivisionError:
            result = "nominal_gdp should be over 0"
            return result
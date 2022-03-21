from typer import Typer
from config import settings
from rules import (
    validate_dafiti_dom, 
    validate_kanui_dom, 
    validate_shop2gether_dom,
    validate_artwalk_adidas_dom,
    validate_gdlp_dom,
    validate_maze_dom, 
    validate_yourid_dom,
    validate_kings_dom,
    validate_authenticfeet_adidas_dom,
    validate_farfetch_dom,
    validate_pineapple_dom
)

app = Typer()


@app.command()
def start_crawl_validation(store: str = ""):
    map_validators = {
        "dafiti": validate_dafiti_dom, 
        'kanui' : validate_kanui_dom, 
        'shop2gether' : validate_shop2gether_dom,
        'artwalk' : validate_artwalk_adidas_dom,
        'gdlp' : validate_gdlp_dom,
        'maze' : validate_maze_dom,
        'yourid' : validate_yourid_dom,
        'kings' : validate_kings_dom,
        "authenticfeet" : validate_authenticfeet_adidas_dom,
        "farfetch" : validate_farfetch_dom,
        "pineapple" : validate_pineapple_dom
    }
    if store not in settings.get("validators.stores"):
        raise ValueError(f"{store} is not a valid store.")
    map_validators[store]()


if __name__ == "__main__":
    app()

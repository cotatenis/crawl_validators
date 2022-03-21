from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_farfetch_dom():
    main_url = [
        "https://www.farfetch.com/br/shopping/men/jordan/items.aspx?view=90&scale=285&rootCategory=Men&category=135968",
        "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?view=90&scale=276&rootCategory=Women&designer=1693960",
        "https://www.farfetch.com/br/shopping/women/trainers-1/items.aspx?page=2&view=90&scale=276&rootCategory=Women&designer=4968477",
        "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?page=4&view=90&scale=285&rootCategory=Men&designer=1664",
        "https://www.farfetch.com/br/shopping/men/trainers-2/items.aspx?view=90&scale=285&rootCategory=Men&designer=6110351"
    ]
    main_url = main_url[random.choice(range(len([main_url])))]
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }
    r = requests.get(main_url, headers=headers)
    if not r.ok:
        logger.error(f"A página {main_url} retornou um status code {r.status_code}.")
        sys.exit(1)
    else:
        dom = Selector(text=r.text)
        # check for product datails
        product_details = dom.xpath(
            "//div[@data-testid='productArea']//a[@data-component='ProductCardLink']"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        logger.info("Teste concluído.")
        return None

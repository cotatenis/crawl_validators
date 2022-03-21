from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_kings_dom():
    main_url = "https://www.lojakings.com.br/collections/tenis-masculino?constraint=adidas"
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
            "//div[@class='product-image-area']/a/@href"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://www.lojakings.com.br/products/tenis-adidas-zx-2k-boost-preto-2.js",
            "https://www.lojakings.com.br/products/tenis-adidas-superstar-preto-2.js",
            "https://www.lojakings.com.br/products/tenis-adidas-superstar-foundation-branco.js",
            "https://www.lojakings.com.br/products/tenis-forum-low-adidas-masculino.js"
        ]
        product_url = products_urls[random.choice(range(len([products_urls])))]
        r = requests.get(product_url, headers=headers)
        if not r.ok:
            logger.error(
                f"A página {product_url} retornou um status code {r.status_code}."
            )
            sys.exit(1)
        response = r.json()
        price = response['price']
        if not price:
            logger.error(
                f"Não foi identificado o ProductId no payload {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None
from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_kanui_dom():
    main_url = "https://www.kanui.com.br/calcados-masculinos/tenis/adidas?segment=masculino"
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
            "//div[@class='product-box']/div/a"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check pagination links
        pagination_links = dom.xpath(
            "//li[normalize-space(@class) = 'page']|//li[normalize-space(@class) = 'page next']"
        ).getall()
        if not pagination_links:
            logger.error("Não foram encontrados links para paginação.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://www.kanui.com.br/Tenis-Adidas-Duramo-SL-Marinho-e-Branco-8476955.html"
            "https://www.kanui.com.br/Tenis-Adidas-Lite-Racer-2.0-Preto-e-Vermelho-7989391.html",
            "https://www.kanui.com.br/Adidas-Tenis-Marathon-Tech-5380257.html",
            "https://www.kanui.com.br/Tenis-Adidas-Advantage-Base-Branco-e-Off-White-8275561.html",
            "https://www.kanui.com.br/Tenis-ASWEEMOVE-8520077.html",
            "https://www.kanui.com.br/Tenis-Adidas-Advantage-Base-Masculino-8543175.html"
        ]
        product_url = products_urls[random.choice(range(len([products_urls])))]
        r = requests.get(product_url, headers=headers)
        if not r.ok:
            logger.error(
                f"A página {product_url} retornou um status code {r.status_code}."
            )
            sys.exit(1)
        product_dom = Selector(text=r.text)
        feature_product_detail = product_dom.xpath(
            "//h1[@class='product-name']"
        ).getall()
        if not feature_product_detail:
            logger.error(
                f"Não foi identificado o product name na página {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None

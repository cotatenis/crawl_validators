from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


def validate_yourid_dom():
    main_url = "https://youridstore.com.br/tenis/tenis-adidas.html"
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
            "//div[@class='product-image-wrapper']"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check pagination links
        pagination_links = dom.xpath(
            "//div[@class='pager']//ol//a"
        ).getall()
        if not pagination_links:
            logger.error("Não foram encontrados links para paginação.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://youridstore.com.br/tenis-adidas-x-disney-stan-smith-groot-and-gamora.html",
            "https://youridstore.com.br/tenis-adidas-retropy-e5-core-black.html",
            "https://youridstore.com.br/tenis-adidas-retropy-e5-white-silver.html",
            "https://youridstore.com.br/tenis-adidas-forum-84-low-core-black.html"
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
            "//div[@class='product-name']/h1"
        ).getall()
        if not feature_product_detail:
            logger.error(
                f"Não foi identificado o product name na página {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None

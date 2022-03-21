from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


def validate_gdlp_dom():
    main_url = "https://gdlp.com.br/calcados/adidas/g%C3%AAnero/masculino"
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
            "//li[@class='item last']/a"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check pagination links
        pagination_links = dom.xpath(
            "//div[@class='pages']//li/a"
        ).getall()
        if not pagination_links:
            logger.error("Não foram encontrados links para paginação.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://gdlp.com.br/calcados/adidas/t-nis-adidas-nite-jogger-24741",
            "https://gdlp.com.br/calcados/adidas/t-nis-adidas-4d-fusio-aluminium",
            "https://gdlp.com.br/calcados/adidas/t-nis-adidas-superstar-x-lego",
            "https://gdlp.com.br/calcados/adidas/t-nis-adidas-marathon-86-spzl"
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
            "//div[starts-with(@class, 'product-name')]/span"
        ).getall()
        if not feature_product_detail:
            logger.error(
                f"Não foi identificado o product name na página {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None

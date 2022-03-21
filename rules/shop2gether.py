from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()


def validate_shop2gether_dom():
    main_url = "https://www.shop2gether.com.br/catalog/category/view/id/108260/?marca=1565"
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
            "//div[starts-with(@class, 'product-brand')]/a"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        #number of product listed in the page
        num_products_listed = dom.xpath("//p[@class='amount amount--no-pages']/strong").re(r"\d+")
        #maximum product listed per page
        max_num_products_per_page = dom.xpath("//select[@title='Results per page']//option[@selected='selected']/text()").re(r"\d+")
        if num_products_listed:
            num_products_listed = int(num_products_listed[0])
            if not max_num_products_per_page:
                logger.error("Não foi encontrado o elemento que informa o número máximo de produtos por página.")
                sys.exit(1)
            max_num_products_per_page = int(max_num_products_per_page[0])
            if num_products_listed > max_num_products_per_page:
                # check pagination links
                pagination_links = dom.xpath(
                    "//div[starts-with(@class, 'pages')]//li/a"
                ).getall()
                if not pagination_links:
                    logger.error("Não foram encontrados links para paginação.")
                    sys.exit(1)
        # check product page
        products_urls = [
            "https://www.shop2gether.com.br/tenis-multix.html",
            "https://www.shop2gether.com.br/tenis-zx-500-22.html",
            "https://www.shop2gether.com.br/tenis-zx-1000-c.html",
            "https://www.shop2gether.com.br/tenis-ny-90.html"
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

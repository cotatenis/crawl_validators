from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_artwalk_adidas_dom():
    main_url = [
        "https://www.artwalk.com.br/adidas-originals?PS=24&amp;O=OrderByReleaseDateDESC",
        "https://www.artwalk.com.br/T%C3%AAnis/811?O=OrderByPriceDESC&PS=24&map=specificationFilter_16,productClusterIds",
        "https://www.artwalk.com.br/adidas-stan-smith?O=OrderByPriceASC&PS=24",
        "https://www.artwalk.com.br/adidas-superstar-feminino?O=OrderByPriceASC&PS=24",
        "https://www.artwalk.com.br/masculino/calcados/adidas%20ZX?O=OrderByReleaseDateDESC&PS=24"
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
            "//h3[@class='product-item__title']"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check pagination links
        pagination_links = dom.xpath(
            "//span[@class='ns-button__text']"
        ).getall()
        if not pagination_links:
            logger.error("Não foram encontrados links para paginação.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:2127878",
            "https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:2082654",
            "https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:2097655",
            "https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:2063770",
            "https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:2078811"
        ]
        product_url = products_urls[random.choice(range(len([products_urls])))]
        headers = {
            "authority": "www.artwalk.com.br",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "accept": "*/*",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
        }       
        r = requests.get(product_url, headers=headers)
        if not r.ok:
            logger.error(
                f"A página {product_url} retornou um status code {r.status_code}."
            )
            sys.exit(1)
        response = r.json()[0]
        productId = response.get("productId")
        if not productId:
            logger.error(
                f"Não foi identificado o ProductId no payload {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None

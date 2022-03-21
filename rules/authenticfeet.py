from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_authenticfeet_adidas_dom():
    main_url = [
        "https://www.authenticfeet.com.br/masculino/adidas/T%C3%AAnis",
        "https://www.authenticfeet.com.br/feminino/adidas/T%C3%AAnis",
        "https://www.authenticfeet.com.br/infantil/adidas/T%C3%AAnis"
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
        # check for product details
        product_details = dom.xpath(
            "//div[@class='ns-product-item']//a[@class='ns-product-item-cover']"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        products_urls = [
                "https://www.authenticfeet.com.br/api/catalog_system/pub/products/search?&fq=skuId:2098318",
                "https://www.authenticfeet.com.br/api/catalog_system/pub/products/search?&fq=skuId:2097672",
                "https://www.authenticfeet.com.br/api/catalog_system/pub/products/search?&fq=skuId:98583",
                "https://www.authenticfeet.com.br/api/catalog_system/pub/products/search?&fq=skuId:98387"

        ]
        product_url = products_urls[random.choice(range(len([products_urls])))]
        headers = {
            "authority": "www.authenticfeet.com.br",
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
        try:
            response = r.json()[0]
        except IndexError:
            logger.error(
                f"A página {product_url} retornou um payload vazio."
            )
            sys.exit(1)
        else:
            productId = response.get("productId")
            if not productId:
                logger.error(
                    f"Não foi identificado o ProductId no payload {product_url}."
                )
                sys.exit(1)
            else:
                logger.info("Teste concluído.")
                return None

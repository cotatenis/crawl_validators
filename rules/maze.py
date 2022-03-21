from parsel import Selector
import requests
import sys
import random
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger()

def validate_maze_dom():
    main_url = "https://www.maze.com.br/categoria/adidas/superstar"
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
            "//a[@class='ui image fluid attached']"
        ).getall()
        if not product_details:
            logger.error("Não foram encontrados produtos na página de resultados.")
            sys.exit(1)
        # check product page
        products_urls = [
            "https://www.maze.com.br/produto/tenis-adidas-yeezy-quantum-onyx-preto/4931654",
            "https://www.maze.com.br/produto/tenis-adidas-superstar-branco/4748877",
            "https://www.maze.com.br/produto/tenis-adidas-superstar-slip-on-preto/4510523",
            "https://www.maze.com.br/produto/tenis-adidas-falcon-feminino-branco/4510486"
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
            "//h1[@class='nomeProduto']"
        ).getall()
        if not feature_product_detail:
            logger.error(
                f"Não foi identificado o product name na página {product_url}."
            )
            sys.exit(1)
        else:
            logger.info("Teste concluído.")
            return None

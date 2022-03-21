
░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------


# Web Scraping Validators

Several scripts to run in our DAGs before our spiders in order to make a validation process in the DOM of each page.

## 1. Stores

- [dafiti](https://www.dafiti.com.br/)
- [kanui](https://www.kanui.com.br/)
- [shop2gether](https://shop2gether.com.br)
- [artwalk](https://www.artwalk.com.br/)
- [gdlp](https://gdlp.com.br/)
- [maze](https://www.maze.com.br)
- [yourid](https://youridstore.com.br/)
- [kings](https://www.lojakings.com.br/)
- [authenticfeet](https://www.authenticfeet.com.br/)
- [farfetch](https://www.farfetch.com/br/)
- [pineapple](https://www.shop-pineapple.co/)


## 2. Build
```shell
make docker-build-production
```

## 3. Publish
```shell
docker-publish-production
```

## 4. Uso
- The parameter `store` could receive one of the following values: [`dafiti`, `kanui`, `shop2gether`, `artwalk`, `gdlp`, `maze`, `yourid`, `kings`, `authenticfeet`, `farfetch`, `pineapple`]

```shell
docker run gcr.io/cotatenis/cotatenis-crawl-validators:0.14.0 --store=dafiti
```
<p align="center">
  <img src="VigilantOnion/media/img/logo.png">
</p>

<h1 align="center">VililantOnion</h1>
<p align="center">
  <a href="https://python.org/">
    <img src="https://img.shields.io/pypi/pyversions/3.svg">
  </a>
    <a href="https://opensource.org">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

<p align="center">
  CRAWLER em sites da rede tor, em busca de keywords.
</p>


## Intro

VigilantOnion é um crawler em sites da rede tor, que tem por objetivo encontrar o maior número de sites indexados na surface/tor e realizar crawler em todos eles, buscando por keywords. Tudo isso é possível gerenciar em uma aplicação Web feita com Django e Mysql, como a imagem à baixo:

![Dashboard](/VigilantOnion/media/img/Captura.png)

## Utilização

Primeiro de tudo, verifique o arquivo de configuração e edite com suas informações.

Para executar:

```
python observer.py [options]
```

Utilização simples:

```
python observer.py -Su --url dsohsdodsids.onion
```

opções:

```
usage: observer.py [-h] [-Sg] [-Sl] [-Si] [-Sc] [-So] [-Su] [-u URL]
                   [-i IMPUT] [-l LIST] [-f FRAMEWORK] [-d] [-c]
                   [--ignoredate] [--initial] [-o ORDER] [--infinite]

VigilantOnion is a script to collect as many sites as possible from the onion
network, and add to a database. With all possible sites collected, a crawler
will be made, so we can monitor, searching for keywords defined by you.

optional arguments:
  -h, --help            show this help message and exit
  -Sg                   Start Get: Start the web site crawler tor through a
                        list. Available frameworks: google/altonion/danwin/dis
                        coverydarkweb/donion/fresnonions/gist/github/securityn
                        ews/underdir,torch
  -Sl                   Start Get: Function to do crawler on websites and get
                        urls onions. Ex: -Sl [-l/--list] /path/file.txt
  -Si                   Start Import: Make the import of urls onions and a
                        file.
  -Sc                   Start Crawler: Start the crawler process on all URLs
                        in the database. This process is very time consuming,
                        I recommend that you use screen (Linux) to accomplish
                        this task. Ex: -Sc
  -So                   Start crawler by order by jumping one quantity at a
                        time. This option should be used to start more than
                        one screen to perform the crawler, preventing it from
                        passing the same urls in other sessions. Ex: -So
                        [-d/--desc] 3
  -Su                   Start Crawler URL: Make the crawler a single url Ex:
                        -Su --url
  -u URL, --url URL     Tell the url that you want to crawl without http: //
                        or https: // Ex: -Su [-u/--url] diodishsdidds.onion
  -i IMPUT, --imput IMPUT
                        Enter the directory where the file you want to import
                        into the database is located. Ex: -Si [-i/--imput]
                        /home/root/Downloads/list.txt
  -l LIST, --list LIST  Enter the directory of the list of sites on the onion
                        network. Ex: -Sl [-l/--list] /path/file.txt If you
                        want to ignore the last time, add --ignoredate. Ex:
                        -Sl [-l/--list] /path/file.txt --ignoredate
  -f FRAMEWORK, --framework FRAMEWORK
                        Enter the framework you want to use to get URLs
                        onions. Available frameworks: alt/danwin/discover/doni
                        on/fresh/gist/github/security/underdir. Always use
                        commas to separate frameworks Ex: -Sg [-f/--framework]
                        alt,github,security
  -d, --debug           If you want to view all the action logs in the script,
                        use debug mode in any order.
  -c, --clear           Perform cleanup on the database, removing line breaks,
                        space and tab.
  --ignoredate          Skip last view.
  --initial             First adjust the database by adding new information.
  -o ORDER, --order ORDER
                        This option is to be used along with -So, to determine
                        how many urls you would like to skip.
  --infinite            It keeps the script always running in an infinite
                        loop. Ex: python observer.py -Sg --framework google
                        --infinite

You can also develop new framework so that the database has more urls onions.

```

## Wiki

[Utilização/Instalação](https://github.com/andreyglauzer/VigilantOnion/wiki)

## TO DO

- Criar uma imagem no docker para a instalação de toda a aplicação.
- Especificar a URI onde a palavra chave foi encontrada.

## SIEM

Query para enviar os dados ao seu SIEM

```
SELECT companyname.name, companyterm.term, company.companyterm_id, category.categorie, url.*
FROM
     django_onion.dashcategoryoard_namecategories category,
   django_onion.dashcategoryoard_urlonion url LEFT JOIN
   django_onion.dashcategoryoard_urlonion_company company ON company.urlonion_id = url.id
   LEFT JOIN   django_onion.dashcategoryoard_companyterm companyterm ON companyterm.id = company.companyterm_id
   LEFT JOIN django_onion.dashcategoryoard_companyname companyname ON companyname.id = companyterm.name_id
WHERE url.categorie_id = category.id     
AND url.status = 1;
```
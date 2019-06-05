# Get-ADUser -Filter {(AdminCount -eq "1") -and (Enabled -eq "True")}

# Resolver erro google chrome screenshot

53tae27o6zd27rvf.onion

# Exercises - p. 13

# PARA FAZER

1 - Criar template para adiconar novos sources via frond-end | Feito

# 10.1.0.73

## cdvuvwn35uwd7r22.onion

## Replace mysql

UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, ' ', ''), '\r', ''), '\s', ''), '\n', ''); UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'irc://', ''), '\r', ''), '\s', ''); UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http//', ''), '\r', ''), '\s', ''); UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'http://', ''), '\r', ''), '\s', ''); UPDATE dashboard_urlonion SET url= REPLACE(REPLACE(REPLACE(url, 'https://', ''), '\r', ''), '\s', '');

## Buscar onde tenha o termo

select * from dashboard_urlonion where url LIKE "%\s%";

## Obter duplicados

SELECT url, COUNT(url) FROM dashboard_urlonion GROUP BY url HAVING COUNT(url) > 1;

## Deletar diplicados

delete from dashboard_urlonion using dashboard_urlonion, dashboard_urlonion e1 where dashboard_urlonion.id > e1.id and dashboard_urlonion.url = e1.url;

## Deletar com /s

delete from dashboard_urlonion where url LIKE "%\s%";

UPDATE dashboard_urlonion SET url= TRIM(REPLACE(REPLACE(url, CHAR(13), "), CHAR(10),"))

# Migrate MySQL

```
python3.5 manager.py migrate auth
python3.5 manager.py migrate --run-syncdb
```

## ERROS

Erro: failed (13: Permission denied) Soluçaõ: chcon -Rt httpd_sys_content_t /username/test/static

Erro: mysql não retorna os itens pelo mes "UrlOnion.objects.filter(last_date__month=month)" Solução: mudar o time_zone do mysql - > mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -u root -p mysql

Permissão de arquivos estáticos: Erro: 403 Solução: chcon -Rt httpd_sys_content_t /var/www/static/

## Novos crwalers

1 - <https://pastebin.com/u/cybersecuritynews/1> <http://deeplinkdeatbml7.onion/?search=onion&type=verified> <http://depastedihrn3jtw.onion/show.php>

## COmmand screenshot

google-chrome --headless --disable-gpu --proxy-server=socks://127.0.0.1:9050 --screenshot <http://m6su7s3ir7dxggwg.onion/explore/repos?q=&tab=>

# API

<https://medium.com/juntos-somos-mais/graphql-simples-e-test%C3%A1vel-com-django-e-graphene-d8c50c9fa089?sk=45a177c845b0174090af5304a7e7d4e7>

SELECT * FROM dashboard_urlonion url, INNER JOIN dashboard_namecategories categoria ON categoria.id = url.categorie_id INNER JOIN dashboard_urlonion_company keyword ON keyword.urlonion_id = url.id

Query

SELECT * FROM django_onion.dashboard_urlonion x, django_onion.dashboard_companyterm y, django_onion.dashboard_companyname k, django_onion.dashboard_urlonion_company z WHERE x.id = z.urlonion_id OR x.status=1;

SELECT * FROM dashboard_urlonion url INNER JOIN dashboard_namecategories category ON category.id = url.categorie_id INNER JOIN dashboard_urlonion_company keyword ON keyword.urlonion_id = url.id ;

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

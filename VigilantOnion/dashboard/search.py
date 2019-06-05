import re
from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    """
         Divide a cadeia de consulta em palavras-chave inviduais, se livrando de espaços não necessários
         e agrupar as palavras citadas.
         Exemplo:

         >>> normalize_query ("algumas palavras aleatórias" com aspas e espaços)
         ['alguns', 'aleatório', 'palavras', 'com citações', 'e', 'espaços']

    """
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    """
        Retorna uma consulta, que é uma combinação de objetos Q. Essa combinação
        visa pesquisar palavras-chave dentro de um modelo testando os campos de pesquisa fornecidos.

    """
    query = None
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

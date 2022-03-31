'''
Modelo de datos
'''
#Genera una consulta sparql con los datos suministrados
def gen_query(title, author, year, publisher, typeResource, language, keywords):
  query = 'SELECT ?s WHERE {?x creator ?creator . FILTER(contains(ucase(?creator),'+author+'))}'
  return query
#Realiza una peticion al servidor Fuseki con la consulta correspondiente
def query_data(query):
  return requests.post('http://localhost:puerto/fuseki', data={'query': query})

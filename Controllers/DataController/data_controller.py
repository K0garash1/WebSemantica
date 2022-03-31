'''
Controlador de datos
Se encarga de administrar la consulta sparql a Fuseki y su respuesta
'''
import sys
sys.path.insert(1, 'Model/DataModel')
from data_model import gen_query, query_data

'''
Recibe los datos del formulario e identifica los campos, genera una consulta sparql mediante el modelo
y hace una peticion al servidor fuseki
'''
def send_query(form):
    title = form['title']
    author = form['author']
    year = form['year']
    publisher = form['publisher']
    typeResource = form['type']
    language = form['language']
    keywords = form['keywords']
    #Genera consulta sparql
    query = gen_query(title, author, year, publisher, typeResource, language, keywords)
    #Obtiene una respuesta del servidor
    response = query_data(query)
    return response.json()

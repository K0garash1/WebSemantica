import requests
def send_query(form):
    title = form['title']
    author = form['author']
    year = form['year']
    publisher = form['publisher']
    type = form['type']
    language = form['language']
    keywords = form['keywords']
    query = 'SELECT ?s WHERE {?x creator ?creator . FILTER(contains(ucase(?creator),'+author+'))}'
    response = requests.post('http://localhost:puerto/fuseki',
       data={'query': query})
    return response.json()
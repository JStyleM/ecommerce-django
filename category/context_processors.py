from .models import Category


# Los context processor son variables añadidas al contexto de cada vista , en este caso
# se obtiene la lista de categorias y se retorna como diccionario.
# Los context procesors se pasan como parametro en la llave context processors en la variable TEMPLATES
# del Settings.py 

def menu_links(request):
    links = Category.objects.all() # Obtiene la lista de categorias 
    return dict(links=links) # retorna un diccionario con la consulta 
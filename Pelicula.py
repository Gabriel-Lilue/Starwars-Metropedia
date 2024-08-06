class Pelicula:
    def __init__(self, id, title, episode_id, release_date, opening_crawl, director, producer):
        self.id = id
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director 
        self.producer = producer

    # Para mostrar las variables de manera amigable
    def show(self):
        return f'''{self.id}. --------
TITULO: {self.title}
NUMERO DE EPISODIO: {self.episode_id}
FECHA DE LANZAMIENTO: {self.release_date}
"OPENING CRAWL": {self.opening_crawl}
DIRECTOR: {self.director}
PRODUCTOR: {self.producer}
--------
'''
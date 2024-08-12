class Pelicula:
    def __init__(self, id, title, episode_id, release_date, opening_crawl, director, producer):
        """
        Constructor de la clase Película

        Args:
            id (int): ID de la película (identificador)
            title (string): Título de la película
            episode_id (int): ID de la película
            release_date (string): Fecha de lanzamiento de la película
            opening_crawl (string): Texto al inicio de la película
            director (string): Director de la película
            producer (string): Productor de la película
        """
        self.id = id
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director 
        self.producer = producer

    # Para mostrar las variables de manera amigable
    def show(self):
        """
        Metodo para mostrar las variables de manera amigable
        Returns:
            string: Mensaje con las variables del objeto
        """
        return f'''{self.id}. --------
TITULO: {self.title}
NUMERO DE EPISODIO: {self.episode_id}
FECHA DE LANZAMIENTO: {self.release_date}
"OPENING CRAWL": {self.opening_crawl}
DIRECTOR: {self.director}
PRODUCTOR: {self.producer}
--------
'''
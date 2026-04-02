from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Inicializamos el tiempo, que se usará como timestamp para ordenar los tweets cronológicamente.
        self.time = 0
        
        # Diccionario que almacena los usuarios que cada usuario sigue.
        # Clave: followerId (usuario que sigue)
        # Valor: conjunto de followeeIds (usuarios seguidos por ese usuario)
        self.followMap = defaultdict(set)
        
        # Diccionario que almacena los tweets de cada usuario.
        # Clave: userId
        # Valor: lista de tuplas (time, tweetId), donde 'time' es el timestamp y 'tweetId' es el identificador del tweet.
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Publica un tweet para un usuario.
        :param userId: ID del usuario que publica el tweet.
        :param tweetId: ID del tweet.
        """
        # Agregamos el tweet con su timestamp actual al tweetMap del usuario.
        self.tweetMap[userId].append((self.time, tweetId))
        
        # Incrementamos el tiempo para garantizar que el próximo tweet tenga un timestamp único.
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Obtiene el feed de noticias para un usuario.
        Combina los tweets propios y de los usuarios que sigue, ordenados por tiempo.
        Devuelve los 10 tweets más recientes.
        :param userId: ID del usuario que solicita el feed.
        :return: Lista con los IDs de los tweets más recientes.
        """
        # Inicializamos el feed con los tweets del propio usuario.
        feed = self.tweetMap[userId][:]
        
        # Agregamos los tweets de cada usuario que sigue.
        for followeeId in self.followMap[userId]:
            feed.extend(self.tweetMap[followeeId])
        
        # Ordenamos todos los tweets por tiempo en orden descendente (más reciente primero).
        feed.sort(key=lambda x: -x[0])  # x[0] es el timestamp.
        
        # Retornamos solo los IDs de los 10 tweets más recientes.
        return [tweetId for _, tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Permite que un usuario siga a otro.
        :param followerId: ID del usuario que sigue.
        :param followeeId: ID del usuario a seguir.
        """
        # Un usuario no puede seguirse a sí mismo.
        if followerId != followeeId:
            # Agregamos el followeeId al conjunto de usuarios seguidos por el followerId.
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Permite que un usuario deje de seguir a otro.
        :param followerId: ID del usuario que deja de seguir.
        :param followeeId: ID del usuario al que deja de seguir.
        """
        # Eliminamos el followeeId del conjunto de usuarios seguidos por el followerId.
        self.followMap[followerId].discard(followeeId)  # 'discard' no lanza error si el followeeId no existe.

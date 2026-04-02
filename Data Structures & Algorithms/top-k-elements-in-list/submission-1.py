class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Paso 1: Contar frecuencias
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        # Convertir el diccionario a una lista de tuplas y ordenarlo por el valor en orden descendente
        sorted_freq_map = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
        
        # Extraer los k elementos más frecuentes
        lista = []
        for i in range(k):
            lista.append(sorted_freq_map[i][0])
        
        return lista
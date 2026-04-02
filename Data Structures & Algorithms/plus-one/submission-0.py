from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        
        # Convertir lista de dígitos a string
        letter = ''.join(str(i) for i in digits)  # O(n)
        
        # Convertir a entero, sumar 1
        letter = int(letter) + 1  # O(n)
        
        # Convertir de nuevo a lista de dígitos
        lista = [int(c) for c in str(letter)]  # O(n)
        return lista

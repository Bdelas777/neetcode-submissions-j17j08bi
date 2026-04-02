class Solution:
    def reverse(self, x: int) -> int:
        # Convertimos el número a string y lo invertimos
        reversed_str = str(abs(x))[::-1]
        
        # Convertimos de nuevo a entero
        reversed_int = int(reversed_str)
        
        # Restauramos el signo del número original
        if x < 0:
            reversed_int = -reversed_int
        
        # Verificamos si está dentro del rango de enteros de 32 bits
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        
        return reversed_int

        
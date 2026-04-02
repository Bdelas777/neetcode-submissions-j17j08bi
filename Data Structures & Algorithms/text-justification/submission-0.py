class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines = []
        i = 0

        # ── Paso 1: Agrupar palabras en líneas (enfoque greedy) ──────────────
        while i < len(words):
            line_len = len(words[i])
            j = i + 1

            while j < len(words):
                # +1 representa el espacio mínimo entre palabras
                if line_len + 1 + len(words[j]) > maxWidth:
                    break
                line_len += 1 + len(words[j])
                j += 1

            lines.append(words[i:j])
            i = j

        # ── Paso 2: Construir cada línea justificada ─────────────────────────
        result = []

        for idx, line in enumerate(lines):
            is_last   = (idx == len(lines) - 1)
            total_chars  = sum(len(w) for w in line)
            total_spaces = maxWidth - total_chars
            gaps      = len(line) - 1

            # Última línea O línea con una sola palabra: justificar a la izquierda
            if is_last or gaps == 0:
                text = " ".join(line)
                result.append(text + " " * (maxWidth - len(text)))
                continue

            # Distribuir espacios entre los huecos
            space_width, extra = divmod(total_spaces, gaps)

            line_str = ""
            for k, word in enumerate(line[:-1]):
                line_str += word
                # Los huecos de la izquierda reciben un espacio extra si no divide exacto
                line_str += " " * (space_width + (1 if k < extra else 0))
            line_str += line[-1]

            result.append(line_str)

        return result

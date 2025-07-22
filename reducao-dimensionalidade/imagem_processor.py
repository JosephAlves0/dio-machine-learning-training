class Imagem:
    def __init__(self, dados_pixels, largura, altura):
        self.dados_pixels = dados_pixels
        self.largura = largura
        self.altura = altura

    def obter_pixel(self, x, y):
        if 0 <= x < self.largura and 0 <= y < self.altura:
            return self.dados_pixels[y][x]
        else:
            raise IndexError("Coordenadas fora dos limites da imagem")
        
    def definir_pixel(self, x, y, valor):
        if 0 <= x < self.largura and 0 <= y < self.altura:
            self.dados_pixels[y][x] = valor
        else:
            raise IndexError("Coordenadas fora dos limites da imagem")
        
    def to_string(self):
        s = ""
        for y in range(self.altura):
            s += str(self.dados_pixels[y]) + "\n"
        return s
    
    def converter_para_cinza(self):
        if not isinstance(self.dados_pixels[0][0], tuple):
            print("Os dados dos pixels já estão em escala de cinza")
            return None
        
        novos_pixels = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

        for y in range(self.altura):
            for x in range(self.largura):
                r, g, b = self.obter_pixel(x, y)
                pixel_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)
                novos_pixels[y][x] = max(0, min(255, pixel_cinza))

        return Imagem(novos_pixels, self.largura, self.altura)
    
    def binarizar(self, limiar):

        if isinstance(self.dados_pixels[0][0], tuple):
            print("Para binarizar, a imagem deve estar em escala de cinza primeiro.")
            return None

        novos_pixels = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

        for y in range(self.altura):
            for x in range(self.largura):
                pixel_cinza = self.obter_pixel(x, y)
                
                if pixel_cinza < limiar:
                    novos_pixels[y][x] = 0
                else:
                    novos_pixels[y][x] = 255

        return Imagem(novos_pixels, self.largura, self.altura)
    
    def obter_pixels_para_pillow(self):
        pixels_flat = []
        for y in range(self.altura):
            for x in range(self.largura):
                pixels_flat.append(self.dados_pixels[y][x])
        return pixels_flat
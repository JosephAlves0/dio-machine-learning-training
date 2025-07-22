from PIL import Image as PILImage
from imagem_processor import Imagem

def ler_imagem(caminho_imagem):
    try:
        pil_image = PILImage.open(caminho_imagem)
        pil_image = pil_image.convert("RGB")
        largura, altura = pil_image.size
        
        pixels_flat = list(pil_image.getdata())

        dados_pixels = []
        for y in range(altura):
            linha = []
            for x in range(largura):
                linha.append(pixels_flat[y * largura + x])
            dados_pixels.append(linha)

        return dados_pixels, largura, altura
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_imagem} não foi encontrado.")
        return None, None, None
    except Exception as e:
        print(f"Erro ao ler a imagem: {e}")
        return None, None, None

def salvar_imagem(imagem_obj, caminho_saida, modo= "RGB"):
    try:
        pixels_para_pillow = imagem_obj.obter_pixels_para_pillow()
        pil_image_saida = PILImage.new(modo, (imagem_obj.largura, imagem_obj.altura))
        pil_image_saida.putdata(pixels_para_pillow)

        pil_image_saida.save(caminho_saida)
        print(f"Imagem salva em {caminho_saida}")
    except ValueError as ve:
        print(f"Erro ao salvar a imagem. Verifique se as dimensões ({imagem_obj.largura}x{imagem_obj.altura}) "
              f"e o formato dos pixels na lista correspondem ao 'modo' '{modo}'. Detalhe: {ve}")
    except Exception as e:
        print(f"Erro ao salvar a imagem: {e}")



if __name__ == "__main__":
    caminho_imagem_jpg = "paisagem.jpg"

    print("Iniciando processamento da imagem...")

    dados_originais, largura_img, altura_img = ler_imagem(caminho_imagem_jpg)

    if dados_originais:
        imagem_original = Imagem(dados_originais, largura_img, altura_img)
        print("Convertendo imagem para escala de cinza...")
        imagem_cinza = imagem_original.converter_para_cinza()

        if imagem_cinza:
            print(f"Imagem em Níveis de cinza criada (Dimensões: {largura_img}x{altura_img})")
            caminho_saida_cinza = "paisagem_cinza.png"
            salvar_imagem(imagem_cinza, caminho_saida_cinza, modo="L")
            #print(imagem_cinza.to_string())

            print("Binarizando imagem com limiar 128...")
            limiar_binarizacao = 128
            imagem_binarizada = imagem_cinza.binarizar(limiar_binarizacao)

            if imagem_binarizada:
                print(f"Imagem binarizada criada (Dimensões: {imagem_binarizada.largura}x{imagem_binarizada.altura})")
                caminho_saida_binarizada = "paisagem_binarizada.png"
                salvar_imagem(imagem_binarizada, caminho_saida_binarizada, modo="L")
                #print(imagem_binarizada.to_string())
        else:
            print("A imagem já estava em escala de cinza ou ocorreu um erro na conversão.")
    else:
        print("Não foi possível processar a imagem devido a um erro na leitura.")
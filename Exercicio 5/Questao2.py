
import re


def verificaPalindromo(texto: str) -> str:
  
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"



frase = input("Digite uma palavra ou frase: ")
print("É palíndromo?", verificaPalindromo(frase))
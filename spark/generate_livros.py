from pathlib import Path
import random

OUT = Path(__file__).parent / "livros_10000.txt"
random.seed(42)

adjetivos = [
    "Pequeno", "Grande", "Antigo", "Novo", "Perdido", "Oculto", "Brilhante",
    "Sombrio", "Doce", "Amargo", "Silencioso", "Ruidoso", "Misterioso",
    "Eterno", "Efêmero", "Veloz", "Lento", "Profundo", "Raso", "Sagrado"
]
substantivos = [
    "Segredo", "Caminho", "Mar", "Cidade", "Jardim", "Livro", "Destino",
    "Memória", "Noite", "Luz", "Sombra", "Vento", "Tempo", "Voz", "Mundo",
    "História", "Alma", "Praia", "Montanha", "Porta"
]
verbos = [
    "Encontrar", "Perder", "Descobrir", "Guardar", "Romper", "Construir",
    "Viajar", "Amar", "Odiar", "Lembrar", "Esquecer", "Seguir", "Fugir"
]
conectores = ["do", "da", "dos", "das", "em", "por", "sobre", "além de"]

padroes = [
    "{adj} {subst}",
    "{subst} {con} {subst2}",
    "O {subst} {verbo}",
    "{adj} {subst}: {subst2}",
    "A {subst} de {subst2}",
    "{subst} e {subst2}",
    "{adj} {subst} - Uma {subst2} História",
    "{subst} {con} {adj} {subst2}"
]

def gera_titulo():
    pattern = random.choice(padroes)
    return pattern.format(
        adj=random.choice(adjetivos),
        subst=random.choice(substantivos),
        subst2=random.choice(substantivos),
        verbo=random.choice(verbos),
        con=random.choice(conectores)
    )

titulos = set()
while len(titulos) < 10000:
    titulos.add(gera_titulo())

OUT.write_text("\n".join(sorted(titulos)), encoding="utf-8")
print(f"Arquivo gerado: {OUT} ({len(titulos)} linhas)")
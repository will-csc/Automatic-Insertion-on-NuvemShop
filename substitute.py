import os
import re
from pathlib import Path

# Lista COMPLETA dos nomes originais (da imagem anterior)
nomes_antigos = [
    "24-25 Bahia Especial S-XXL",
    "24-25 Botafogo com adicional PAICHS",
    "24-25 Corinthians Away +PATROCINADORES",
    "24-25 Corinthians Home +PATROCINADORES",
    "24-25 Cruzeiro Home +PATROCINADORES",
    "24-25 Flamengo +PATROCINADORES",
    "24-25 Fluminense Rosa S-XXL",
    "24-25 Fortaleza Home +PATROCINADORES",
    "24-25 Palmeiras Especial S-3XL",
    "24-25 PLAYER Palmeiras Home +PATROCINADORES",
    "24-25 Santos Away +PATROCINADORES",
    "24-25 Santos Away S-4XL",
    "24-25 Santos Charlie Brown S-4XL",
    "24-25 Santos Home +PATROCINADORES",
    "24-25 Santos Home S-4XL",
    "24-25 Sao Paulo Away +PATROCINADORES",
    "24-25 Sport Recife Pink S-4XL",
    "24-25 Vasco Third +PATROCINADORES",
    "24-25 Windbreaker Corinthians S-XXL",
    "25-26 Bahia Especial S-XXL",
    "25-26 Corinthians Treino Roxa S-4XL",
    "25-26 Cruzeiro Training Blue S-4XL",
    "25-26 Cruzeiro Training Jersey S-4XL",
    "25-26 Flamengo Especial S-XXL",
    "25-26 Fluminense Home + TODOS OS PATROCINADORES",
    "25-26 PLAYER Palmeiras Away +PATROCINADORES",
    "25-26 PLAYER Palmeiras Home +PATROCINADORES",
    "25-26 Volta Redonda Away S-XXL",
    "2024-25 Corinthians Training Wear S-XXXXL",
    "2024-25 França Fora",
    "Retró 92-93 Flamengo Home S-XXL",
    "Retró 1980 Palmeiras S-XXL",
    "Retró 1988 Vasco Away S-XXL",
    "Retró 1994 Flamengo Away S-XXL",
    "Retró 1994-95 Gremio S-XXL",
    "Retró 1995-96 Corinthians S-XXL",
    "Retró 1995-96 Flamengo S-XXL",
    "Retró 1995-96 Gremio S-XXL",
    "Retró 1996 Away Palmeiras S-XXL",
    "Retró 1996 Palmeiras S-XXL",
    "Retró 2001-02 Flamengo Away S-XXL",
    "Retró 2010 Flamengo Home S-XXL",
    "Retro Corinthians 1994 home S-XXL",
    "Retro Corinthians 1997 home S-XXL",
    "Retro Corinthians 1999 III S-XXL",
    "Retro Flamengo 1986 Away S-XXL",
    "Retro Palmeiras 1997 white S-XXL",
    "Retro Santos 1998 away S-XXL",
    "Retró Vasco 2000 S-XXL",
    "Retro Vasco da Gama 1997 White S-XXXXL"
]

def formatar_nome(nome_antigo):
    # Remove termos de tamanho (S-XXL, S-4XL, etc.)
    nome_novo = re.sub(r'(?i)\s*S-\w+\s*$', '', nome_antigo.strip())
    # Remove "Retró/Retro" completamente
    nome_novo = re.sub(r'(?i)\bretr[óo]\b\s*', '', nome_novo)
    # Substitui termos técnicos
    nome_novo = re.sub(r'(?i)\baway\b', 'Visitante', nome_novo)
    nome_novo = re.sub(r'(?i)\bhome\b', 'Casa', nome_novo)
    nome_novo = re.sub(r'(?i)\bplayer\b', 'Jogador', nome_novo)
    nome_novo = re.sub(r'(?i)\btraining\b', 'Treino', nome_novo)
    nome_novo = re.sub(r'(?i)\bwear\b', '', nome_novo)
    nome_novo = re.sub(r'(?i)\biii\b', 'Third', nome_novo)
    # Padroniza patrocínios
    nome_novo = re.sub(r'(?i)\+PATROCINADORES\b', 'Patrocinada', nome_novo)
    nome_novo = re.sub(r'(?i)\+ TODOS OS PATROCINADORES\b', 'Patrocinada', nome_novo)
    # Corrige anos (24-25 -> 2024-25)
    nome_novo = re.sub(r'(?<!\d)(\d{2})-(\d{2})(?!\d)', r'20\1-\2', nome_novo)
    # Remove espaços duplicados e ajusta hifens
    nome_novo = ' '.join(nome_novo.split())
    return nome_novo

# Renomeia as pastas
for nome_antigo in nomes_antigos:
    nome_novo = formatar_nome(nome_antigo)
    caminho_antigo = Path(nome_antigo)
    caminho_novo = Path(nome_novo)
    
    if caminho_antigo.exists():
        try:
            os.rename(str(caminho_antigo), str(caminho_novo))
            print(f"Renomeado: '{nome_antigo}' -> '{nome_novo}'")
        except Exception as e:
            print(f"ERRO ao renomear '{nome_antigo}': {e}")
    else:
        print(f"Pasta não encontrada: '{nome_antigo}'")
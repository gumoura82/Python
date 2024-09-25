import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
arquivo_excel = 'Formula_E.xlsx'

# Função para ler os dados da planilha selecionada
def ler_dados(planilha):
    df = pd.read_excel(arquivo_excel, sheet_name=planilha)
    df = df.rename(columns={"Unnamed: 2": "Piloto", "Best Lap": "Tempo"})
    return df

# Função para converter tempo no formato 'MM:SS.sss' para segundos
def converter_tempo(tempo):
    try:
        minutos, segundos = tempo.split(':')
        return int(minutos) * 60 + float(segundos)
    except ValueError:
        return None

# Função para calcular a média dos tempos de volta de cada piloto
def calcular_media_tempos(df):
    pilotos = df['Piloto'].dropna().unique()
    medias = {}
    for piloto in pilotos:
        tempos = df[df['Piloto'] == piloto]['Tempo'].dropna()
        tempos_convertidos = [converter_tempo(tempo) for tempo in tempos if converter_tempo(tempo) is not None]
        if tempos_convertidos:
            medias[piloto] = sum(tempos_convertidos) / len(tempos_convertidos)
    return medias

# Função para encontrar o piloto com o menor tempo médio
def encontrar_menor_tempo(medias):
    menor_tempo_piloto = min(medias, key=medias.get)
    menor_tempo = medias[menor_tempo_piloto]
    return menor_tempo_piloto, menor_tempo

# Função para encontrar o piloto com o maior tempo médio
def encontrar_maior_tempo(medias):
    maior_tempo_piloto = max(medias, key=medias.get)
    maior_tempo = medias[maior_tempo_piloto]
    return maior_tempo_piloto, maior_tempo

# Função para listar as planilhas disponíveis e perguntar ao usuário qual ele quer acessar
def listar_planilhas():
    excel = pd.ExcelFile(arquivo_excel)
    planilhas = excel.sheet_names
    print("Corridas disponíveis:")
    for ind, planilha in enumerate(planilhas):
        print(f"{ind}. {planilha}")
    return planilhas

# Função para perguntar ao usuário qual dado ele deseja acessar
def escolher_analise():
    print("\nQual dado você quer acessar dessa corrida?")
    print("A. Melhor volta")
    print("B. Pior volta")
    escolha = input("Escolha (A/B): ").strip().upper()
    return escolha

# Função principal para executar as tarefas
def main():
    planilhas = listar_planilhas()
    
    # Pergunta ao usuário qual planilha ele quer acessar
    try:
        usuario_tabela = int(input("\nIndique o índice da tabela que deseja acessar: "))
        planilha_escolhida = planilhas[usuario_tabela]
    except (ValueError, IndexError):
        print("Índice inválido. Por favor, tente novamente.")
        return
    
    dados = ler_dados(planilha_escolhida)
    medias = calcular_media_tempos(dados)
    
    if medias:
        escolha = escolher_analise()

        if escolha == 'A':
            menor_tempo_piloto, menor_tempo = encontrar_menor_tempo(medias)
            print(f"\nO piloto com o menor tempo médio é {menor_tempo_piloto} com um tempo médio de {menor_tempo:.2f} segundos.")
        elif escolha == 'B':
            maior_tempo_piloto, maior_tempo = encontrar_maior_tempo(medias)
            print(f"\nO piloto com o maior tempo médio é {maior_tempo_piloto} com um tempo médio de {maior_tempo:.2f} segundos.")
        else:
            print("Opção inválida.")
    else:
        print('Nenhum tempo válido foi encontrado.')

# Executa o programa principal
if __name__ == '__main__':
    main()

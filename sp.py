import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo Excel
file_path = 'Formula_E.xlsx'

# Função para ler os dados da planilha selecionada
def ler_dados(planilha):
    df = pd.read_excel(file_path, sheet_name=planilha)
    df = df.rename(columns={"Unnamed: 2": "Piloto", "Best Lap": "Tempo"})
    return df

# Função para converter tempo no formato 'MM:SS.sss' para segundos
def converter_tempo(tempo):
    try:
        minutos, segundos = tempo.split(':')
        return int(minutos) * 60 + float(segundos)
    except ValueError:
        # Tratar caso o tempo não esteja no formato correto
        return None

# Função para calcular a média dos tempos de volta de cada piloto
def calcular_media_tempos(df):
    pilotos = df['Piloto'].dropna().unique()
    medias = {}
    for piloto in pilotos:
        tempos = df[df['Piloto'] == piloto]['Tempo'].dropna()
        tempos_convertidos = [converter_tempo(tempo) for tempo in tempos if converter_tempo(tempo) is not None]
        if tempos_convertidos:  # Verificar se há tempos válidos para o piloto
            medias[piloto] = sum(tempos_convertidos) / len(tempos_convertidos)
    return medias

# Função para encontrar o piloto com o menor tempo médio
def encontrar_menor_tempo(medias):
    menor_tempo_piloto = min(medias, key=medias.get)
    menor_tempo = medias[menor_tempo_piloto]
    return menor_tempo_piloto, menor_tempo

#Função para encontrar o piloto como maior tempo médio
def encontrar_maior_tempo(medias):
    maior_tempo_piloto = max(medias, key=medias.get)
    maior_tempo = medias[maior_tempo_piloto]
    return maior_tempo_piloto, maior_tempo

# Função principal para executar as tarefas
def main():
    planilha = '2024 Sao Paulo E-Prix'
    dados = ler_dados(planilha)
    
    medias = calcular_media_tempos(dados)
    
    if medias:  # Verificar se há médias calculadas
        menor_tempo_piloto, menor_tempo = encontrar_menor_tempo(medias)
        print(f'O piloto com o menor tempo médio é {menor_tempo_piloto} com um tempo médio de {menor_tempo:.2f} segundos.')

        maior_tempo_piloto, maior_tempo = encontrar_maior_tempo(medias)
        print(f'O piloto com o maior tempo médio é {maior_tempo_piloto} com um tempo médio de {maior_tempo:.2f} segundos.')
        
    else:
        print('Nenhum tempo válido foi encontrado.')

# Executa o programa principal
if __name__ == '__main__':
    main()

# Projeto: Análise de Tempos de Volta na Fórmula E

## Descrição do Projeto
Este projeto visa analisar os tempos de volta dos pilotos da Fórmula E a partir de dados fornecidos em uma planilha Excel. O código lê os dados, converte os tempos para segundos, calcula a média dos tempos de volta, e oferece análises detalhadas como a identificação dos pilotos com o menor e maior tempo médio, além de estatísticas adicionais, como variância e desvio padrão.

## Estrutura do Projeto
- **Formula_E.xlsx**: Arquivo Excel contendo os dados dos tempos de volta dos pilotos.
- **main.py**: Script principal que realiza a análise.

## Funcionalidades

### Leitura dos Dados
- **Função `ler_dados(planilha)`**: Lê e processa os dados da planilha.

### Conversão de Tempo
- **Função `converter_tempo(tempo)`**: Converte o tempo do formato 'MM:ss.sss' para segundos.

### Cálculo da Média dos Tempos de Volta
- **Função `calcular_media_tempos(df)`**: Calcula a média dos tempos de cada piloto.

### Identificação do Menor Tempo Médio
- **Função `encontrar_menor_tempo(medias)`**: Identifica o piloto com o menor tempo médio.

### Identificação do Maior Tempo Médio
- **Função `encontrar_maior_tempo(medias)`**: Identifica o piloto com o maior tempo médio.

### Estatísticas Adicionais
- **Função `calcular_estatisticas_adicionais(df)`**: Calcula variância e desvio padrão dos tempos de volta de cada piloto.

### Interatividade
- **Função `listar_planilhas()`**: Lista as corridas disponíveis para análise.
- **Função `escolher_analise()`**: Permite ao usuário escolher a análise desejada (melhor volta, pior volta ou estatísticas adicionais).

### Visualização Gráfica
- **Função `plotar_tempos(medias)`**: Gera um gráfico de barras mostrando os tempos médios de cada piloto.

### Execução Principal
- **Função `main()`**: Conduz o fluxo principal, permitindo a escolha da corrida e da análise.

## Instruções de Uso

### Pré-requisitos
- Python 3.x instalado.
- Bibliotecas `pandas` e `matplotlib` instaladas.

### Preparação do Arquivo
- O arquivo **Formula_E.xlsx** deve estar no mesmo diretório do script **main.py**.

### Execução do Script
- Execute o script **main.py** e siga as instruções no terminal para escolher a corrida e a análise desejada.

## Informações Relevantes
- Certifique-se de que os dados na planilha estão formatados corretamente, com os tempos de volta no formato 'MM:ss.sss'.
- Caso ocorra um erro de leitura dos dados ou formatação dos tempos, verifique a consistência dos dados na planilha.

---

## Nomes e RMs

- **Nome**:	  Gustavo Oliveira de Moura	        **RM**: 555827
- **Nome**:	  Lynn Bueno Rosa			              **RM**: 551102
- **Nome**:	  Vinicius Matareli     	          **RM**: 555200
- **Nome**:	 	Giovanne C. Z. Silva 	            **RM**: 556223

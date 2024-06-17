# Projeto: Análise de Tempos de Volta na Fórmula E

## Descrição do Projeto
Este projeto tem como objetivo analisar os tempos de volta dos pilotos na Fórmula E, a partir de dados fornecidos em uma planilha Excel. O código lê os dados da planilha, converte os tempos de volta para segundos, calcula a média dos tempos de volta de cada piloto e identifica o piloto com o menor tempo médio.

## Estrutura do Projeto
- **Formula_E.xlsx**: Arquivo Excel contendo os dados dos tempos de volta dos pilotos.
- **main.py**: Script principal que executa a análise dos dados.

## Funcionalidades

### Leitura dos Dados
- **Função `ler_dados(planilha)`**: Lê os dados da planilha especificada no arquivo Excel.

### Conversão de Tempo
- **Função `converter_tempo(tempo)`**: Converte o tempo no formato 'MM:ss.sss' para segundos.

### Cálculo da Média dos Tempos de Volta
- **Função `calcular_media_tempos(df)`**: Calcula a média dos tempos de volta de cada piloto.

### Identificação do Menor Tempo Médio
- **Função `encontrar_menor_tempo(medias)`**: Encontra o piloto com o menor tempo médio.

### Execução Principal
- **Função `main()`**: Executa as tarefas principais do script, incluindo a leitura dos dados, cálculo das médias e identificação do menor tempo médio.

## Instruções de Uso

### Pré-requisitos
- Python 3.x instalado.
- Bibliotecas `pandas` e `matplotlib` instaladas.

### Preparação do Arquivo
- Certifique-se de que o arquivo **Formula_E.xlsx** está no mesmo diretório que o script **main.py**.

### Execução do Script
- Execute o script **main.py**.

## Informações Relevantes
- Certifique-se de que os dados na planilha estão formatados corretamente, com os tempos de volta no formato 'MM:ss.sss'.
- Caso ocorra um erro de leitura dos dados ou formatação dos tempos, verifique a consistência dos dados na planilha.

---

## Nomes e RMs

- **Nome**:	  Gustavo Oliveira de Moura	        **RM**: 555827
- **Nome**:	  Lynn Bueno Rosa			              **RM**: 551102
- **Nome**:	  Ygor Vieira Pontes          	    **RM**: 555686
- **Nome**:	  Vinicius Matareli     	          **RM**: 555200
- **Nome**:	 	Giovanne C. Z. Silva 	            **RM**: 556223

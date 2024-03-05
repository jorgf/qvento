# QVENTO.py

## Sobre 
Esse projeto está sendo desenvolvido para a disciplina de Análise das estruturas I (Engenharia Civil). Tem por objetivo usar python para modelar comportamentos estruturais e automatizar cálculo de ação do vento.

- O procedimento leva em consideração as diretrizes da NBR 6123 - ações de vento e as notas de aula.

## Executando o programa
1. Para executar esse programa, primeiro é preciso configurar o arquivo 'input.json', com os dados de entrada para o problema estudado. Por padrão, temos o exemplo:
```
    "velocidade_basica": 30,
    "parametro_meteorologico":{
        "b":0.73,
        "p":0.16,
        "fr":0.98
    },
    "s1": 1.0,
    "s3": 1.0,
    "maior_lado": 20,
    "menor_lado": 15,
    "altura": 30,
    "pe_direito": 10,
    "ca_menor": 1.09,
    "ca_maior": 1.25
```
Onde:
    
- Velocidade básica do vento é definido pelo mapa de isopletas (tabela da NBR 6123);
- Os parâmetros meteorológicos são definidos através da classe da edificação e da categoria da viziinhança (tabela da NBR 6123);
- s1 e s3 são parâmetros definidos em norma;
- maior_lado corresponde ao maior lado, em planta, da edificação;
- menor_lado corresponde ao menor lado, em planta, da edificação;
- altura corresponde à altura total da edificação
- ca_maior refere-se ao coeficiente de arrasto considerando a análise para o maior lado;
- ca_menor refere-se ao coeficiente de arrasto para considerando a análise para o menor lado;

2. Após a configuração do arquivo 'input.json', basta, no terminal, digitar o comando:
```python qvento.py```, ou executar pela IDE que estiver usando.

## Pontos de melhoria
Alguns pontos que podem ser melhorados ao longo do tempo:
1. automatização dos parâmetros de entrada s1 e s3, assim, basta que a categoria da vizinhança e a geometria da edificação seja fornecida para determinar-mos a classe, s1 e s3;
2. Definir cotas para calculo da força;
3. Relatório - quadro resumo das informações;
4. Adoção de POO
5. Uso de interface gráfica para ter uma aplicação mais amigável ao usuário final;
6. padronizar linguagem (EN)
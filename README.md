# Objetivo

O arquivo **main.py** é o único necessário para execução do emp2. Ele receberá como entrada um arquivo .dat que contém a informação da matriz e retornará para o usuário uma representação gráfica do menor caminho usando o algoritmo de Djiktras.

## Instalação

O processo de instalação das dependências é bem simples e pode ser feita através do comando [pip](https://pip.pypa.io/en/stable/) e do arquivo **requirements.txt**.

```bash
pip install -r requirements.txt
```

## Como executar

Para executar o arquivo main.py, é preciso apenar executar o comando:

```bash
python main.py
```
No entanto, é preciso realizar a modificação do nome do arquivo em caso que estaremos um **.dat** diferente do arquivo padrão **maze.dat**. Para realizar essa alteração, altere a seguinte linha(33) para o nome do arquivo especificado:

```python
maze = Maze("maze.dat")
```

## Disclamer

Esse repo se refere ao trabalho da disciplina de estrutura de dados e foi elaborado utilizando referências da internet apresentadas a seguir:

[Stack abuse implementation](https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/) \
[Geek for geeks](https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/) 


## License

[MIT](https://choosealicense.com/licenses/mit/)
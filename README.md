
![Logo](/src/images/LOGO.jpg)


# Estudi-IA

Esse é um projeto feito para o desafio da imersão da [Alura](https://www.alura.com.br/) em parceria com a [Google](https://www.google.com.br/) e a [FIAP](https://www.fiap.com.br/).

A ideia do projeto é uma ferramenta que auxilie o estudante na hora de fazer aquela prova ou até mesmo ficar craque em algum assunto e nada melhor para treinar do que o bom e velho exercício.

É ae que o Estudi-IA se destaca, com ela você pode criar exercícios  de praticamente qualquer matéria, apenas com algumas configurações e você já tem uma lista de exercícios  prontinha para você estudar.




## Funcionalidades

- Cria lista de exercicios de praticamente qualquer matéria
- Organiza suas listas em pastas separadas
- Salva suas listas localmente em arquivos de fácil acesso.
- Corrija sua lista com uma IA de ponta que é o [Gemini](https://gemini.google.com/app)


## Instalação

Para começar a utilziar o Estudi-IA você vai presisar de 2 coisas básicas.

Chave de API do Google.
  - você pode conseguir a sua atráves desse [Link](https://aistudio.google.com/app/apikey) logando com a sua conta do Google

Chave de configuração PysimpleGUI 
  - A PysimpleGUI é uma biblioteca muito poderosa e como o nome ja diz simples de se usar na criação de interfaces gráficas, para você conseguir utilizar basta se cadastrar atráves desse [Link](https://www.pysimplegui.com/pricing) onde depois de cadastrar você irá receber uma chave por email vai poder usar nos seus projetos.

Com essas duas informaçoes você já está pronto para continuar a configuração.


Após realizar o clone do projeto na sua máquina abra seu terminal favorito e e crie um ambiente virtual dentro da pasta do projeto com o comando:

````python
  pythom -m venv venv
````
ative seu ambiente virtual:
````python
  .\venv\Scripts\activate
````
e após isso execute o comando para instalar as biblioteca que o projeto utiliza:

```python
  pip install -r requirements.txt
```
Agora é só executar o comando

```python
  python main.py
```

Na primeira vez que você executar o programa ira aparecer uma janela para você configurar a chave do PysimpleGUI, basta informar ela uma única vez para ficar gravada no seu computador.


    
## Uso/Exemplos



## Screenshots
### Tela inicial
![App Screenshot](/src/images/TELA_INICIAL.png)

Aqui temos duas coisas muito importantes:
  - O programa não funciona sem uma chave de API do Google
  - Lembre de colocar o caminho para onde você quer que o programa salve os seus exercicios

  Após preencher todos os campos é só clicar no botão enviar.

  ![App Screenshot](/src/images/CAMPOS_PREENCHIDOS.png)

Quando você clica em enviar o programa cria no caminho informado uma pasta para cada matéria que você já fez algum exercicio:

![App Screenshot](/src/images/PASTA_EXERCICIOS.png)

Dentro dessa pasta ele cria um arquivo com a quantidade de exercicios e a matéria que você informou:

![App Screenshot](/src/images/EXERCICIO.png)

o nome do arquivo é composto por:
  - Número dos exercicios que você já fez sobre esse matéria
  - Data e hora em que a lista foi criada

Assim você mandem tudo ornganizado e fica mais fácil na hora de revisar.

### Janela de correção

Aqui o programa vai listar para você todas as matérias que você tem na pasta:

![App Screenshot](/src/images/JANELA_CORRECAO.png)

Então você pode informar qual matéria você quer corrigir e também o exericio, ao clicar no botão confirmar o programa vai corrigir o exercicio selecionado e dar a respota/corrigir.

Caso você queira salvar o arquivo você pode clicar no botão de salvar, com isso ele vai salvar a sua resposta com o número do exercicio.

![App Screenshot](/src/images/RESPOSTA.png)


## Suporte

Para suporte, mande um email para lucasfreitasr@outlook.com.

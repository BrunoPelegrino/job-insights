# Job Insights!

<p align="center">
  <img src="https://github.com/BrunoPelegrino/job-insights/blob/main/src/flask_app/images/job-cover.png">
</p>


Neste projeto foi implementado análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com Flask (um framework web muito popular na comunidade Python). Também foi desenvolvido alguns testes para a implementação de uma análise de dados. Por fim, foi escrito uma rota e view para um recurso novo usando Flask!

Objetivo desse projeto foi colocar em prática o inicio do meu aprendizado com Python.



### :mountain_bicyclist: Habilidades que foram trabalhadas:

```
- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição.
- Utilizar funções built-in do Python.
- Utilizar tratamento de exceções.
- Realizar a manipulação de arquivos.
- Escrever funções.
- Escrever testes com Pytest.
- Escrever seus próprios módulos e importá-los em outros códigos.
- Implementar um rota e utilizr jija
```

- Lembre-se de clonar o repositório no diretório desejado na sua máquina!

```
 git clone git@github.com:BrunoPelegrino/job-insights.git
```

<details>
  <summary><strong>🏕️ Rodar aplicação em Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Rodar Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <p align="center">
    <img src="https://user-images.githubusercontent.com/99821267/216327877-ef47f244-0c11-4242-9b93-d0cc5c2c8e5d.png" width="200"/>
  </p>


  Rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
  Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`. 

  <p align="center">
    <img src="(https://user-images.githubusercontent.com/99821267/216327791-c0f6e3cb-d133-49c4-821d-b9372165a5be.png" width="800"/>
  </p>
  
</details>

---

© Desenvolvido por [Bruno Pelegrino](https://www.linkedin.com/in/bruno-pelegrino/) 

Feature: Descoberta e disponibilidade de livros

  Como cliente da livraria
  Quero consultar o catálogo de livros
  Para saber quais opções estão disponíveis antes de ir até a loja


  Scenario: Buscar um livro existente pelo título
    Given que existem livros cadastrados no catálogo
    When eu buscar pelo título "1984"
    Then o livro "1984" deve ser retornado


  Scenario: Buscar livros pelo autor
    Given que existem livros cadastrados no catálogo
    When eu buscar pelo autor "George Orwell"
    Then devem ser retornados 2 livros


  Scenario: Buscar um livro inexistente
    Given que existem livros cadastrados no catálogo
    When eu buscar pelo título "Livro Inexistente"
    Then nenhum livro deve ser retornado


  Scenario: Consultar quantidade disponível em estoque
    Given que existem livros cadastrados no catálogo
    When eu consultar a disponibilidade do livro "1984"
    Then devem ser informados 3 exemplares disponíveis


  Scenario: Filtrar livros por gênero
    Given que existem livros cadastrados no catálogo
    When eu filtrar os livros pelo gênero "Fantasia"
    Then devem ser retornados apenas livros do gênero "Fantasia"


  Scenario: Consultar lançamentos da semana
    Given que existem livros cadastrados no catálogo
    When eu consultar os lançamentos da semana
    Then deve ser retornado 1 lançamento
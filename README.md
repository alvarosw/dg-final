<p style="text-align:center" dir="auto">
  <a href="#orientacoes">Orientações</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#observacoes">Observações</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#etapa-1">Etapa 1</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#etapa-2">Etapa 2</a>
</p>
<hr>
<h1 style="text-align:center">Desenvolvedor Web (Back/Front-End) - Django/Python</h1>
<h2 id="orientacoes" style="text-align:center;border-bottom:none">Orientações</h2>

- Deverá ser utilizada a linguagem Python, o framework Django e o framework Django Rest Framework para desenvolver as soluções;
- Deverá ser criada uma branch nomeada com o seu nome e abrir um pull request para concluir a entrega do teste;
- <strong>Atenção</strong>: O candidato precisa fazer o fork do repositório para conseguir abrir o pull request;
- É necessário submeter um vídeo, com duração máxima de 5 minutos, que explique as funcionalidades do projeto. Recomendamos o uso da extensão ‘Awesome Screenshot’ para navegadores, que permite gravar o vídeo e gerar um link direto para ele. Este link deve ser incluído no arquivo ‘Readme’ do projeto.

<hr>
<h2 id="observacoes" style="text-align:center;border-bottom:none">Observações</h2>

- O banco de dados utilizado fica a sua escolha;
- Podem ser feitas alterações nas configurações do projeto Django;

<hr>
<h2 id="etapa-1" style="text-align:center;border-bottom:none">Etapa 1</h2>
A empresa de energia gostou do último projeto criado e com isso decidiu expandir as funcionalidades. Assim, resolveu contratá-lo para esse desenvolvimento. Você continuará o projeto anterior usando a linguagem Python e o framework Django.

#### A empresa de assinatura de energia te forneceu as seguintes premissas para o desconto:

| Consumo (Média) | Desconto (Residencial) | Desconto (Comercial) | Desconto (Industrial) |
| --- | --- | --- | --- |
| < 10.000 kWh | 18% | 16% | 12% |
| >= 10.000 kWh e <= 20.000 kWh | 22% | 18% | 15% |
| > 20.000 kWh | 25% | 22% | 18% |

#### Alem disso, deve-se considerar os seguintes percentuais de cobertura baseado no consumo:

| Consumo (Média) - kWh | < 10.000 kWh | >= 10.000 kWh e <= 20.000 kWh | > 20.000 kWh |
| --- | --- | --- | --- |
| Cobertura*** | 90% | 95% | 99% |

*** Cobertura é o valor da energia que o consumidor irá receber da empresa de assinatura de energia em relação à energia consumida

### A empresa tem:

- Um código que funciona como calculadora e recebe três valores:
  - Uma lista com consumos de energia elétrica;
  - Valor da tarifa da distribuidora;
  - Tipo de tarifa (Comercial, Residencial e Industrial);

### Requisitos Etapa 1:

1. A funcionalidade da calculadora deverá ser disponibilizada para acesso via API, recebendo os valores e retornando o resultado;
2. Deverá ser criada uma interface para utilização da calculadora, essa interface deve ser disponibilizada pelo Django e deve consumir a API para funcionar;
3. Deverá ser criado um acesso via API para cadastro de consumidores;
4. Deverá ser criada uma interface para o cadastro de consumidores, essa interface deve ser disponibilizada pelo Django e deve consumir a API para funcionar;
5. Deverá ser criado um acesso via API para a listagem de consumidores com seus descontos, essa listagem deve permitir a filtragem;
6. Deverá ser criada uma interface para a listagem de consumidores, essa interface deve ser disponibilizada pelo Django e deve consumir a API para funcionar;


<hr>
<h2 id="etapa-2" style="text-align:center;border-bottom:none">Etapa 2</h2>

A empresa de energia gostou da sua solução para a API e o seu site, mas necessita de algumas alterações para melhorar a integração com os clientes. Assim, resolveu contratá-lo novamente para implementar essas melhorias. Você continuará o projeto anterior usando a linguagem Python, o framework Django e o framework Django Rest Framework

### Requisitos Etapa 2:

1. Deverá ser criado um acesso via API para a listagem das regras de descontos;
2. Deverá ser criado um acesso via API para a listagem das regras de coberturas;
3. Deverá ser criado um acesso via API para atualização de consumidor;
4. Deverá ser criado um acesso via API para exclusão de consumidor;
5. Disponibilizar uma documentação da API(Pode ser via Swagger).

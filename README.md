# bds-framework

É uma biblioteca Python privada que condensa um conjunto de boas práticas para o desenvolvimento das aplicações que
compõem ou comporão a **BDS**  do LAIS e dos parceiros que contratarem o LAIS para fazer suas próprias BDS, a exemplo 
REDS-RN e BDS-ES. disponível apenas para usuários com com permissão no projeto 
https://git.lais.huol.ufrn.br/barramento/barramento-v2/bds-framework/ através do repositório pypi no Gitlab do LAIS. 

> **BDS** é acrônimo para **Barramento de Dados em Saúde**. 


## Usando em seu projeto

Entenda que, como uma biblioteca em repositório privado é necessária a autorização para usá-la, assim sendo, sempre 
que for instalar via `pip` você precisará autenticar-se no repositório do LAIS hospedado pelo GitLab. 

> Aproveite e confira as 
> [versões da biblioteca](https://git.lais.huol.ufrn.br/barramento/barramento-v2/bds-framework/-/packages).

### Autorizando e configurando
1. A **autorização** é feita em https://git.lais.huol.ufrn.br/-/profile/personal_access_tokens , veja como criar o 
[token de acesso pessoal](https://git.lais.huol.ufrn.br/help/user/profile/personal_access_tokens) na a documentação 
oficial do GitLab. Lembre de que deve ter ao menos o escopo api, este token pode ser usado para pacotes Python 
(libraries) ou Docker (imagens). Nome sugerido: `pacotes`.
2. Assumindo que o token gerado seja `ACCESS-TOKEN`, crie o arquivo `.pip/pip.conf` na pasta home do seu usuário, 
conforme exemplo abaixo:

```
[global]      
extra-index-url = https://__token__:ACCESS-TOKEN@git.lais.huol.ufrn.br/api/v4/projects/909/packages/pypi/simple
```

Exemplo no Linux:

```
mkdir ~/.pip
echo "[global]      
extra-index-url = https://__token__:ACCESS-TOKEN@git.lais.huol.ufrn.br/api/v4/projects/909/packages/pypi/simple" > ~/.pip/pip.conf
```

> Atenção para o `909` nesta URL, isso é o que identifica de qual projeto no GitLab o arquivo será baixado, ou seja, 
> serve para esta biblioteca apenas, assim sendo, caso você queira usar outra bibliteca dos nossos repostitório será 
> necessário configurar para o ID do projeto correto.

Feito isso o teu ambiente estará configurado e autorizado no repositório deste projeto no GitLab do LAIS.

### Usando no seu projeto 

Agora vamos ver como configurar isso no seu projeto, supondo que você use um arquivo `requirements.txt` em Linux, tente
o comando abaixo

```
echo '
# BDS
--extra-index-url https://git.lais.huol.ufrn.br/api/v4/projects/909/packages/pypi/simple
bds-framework==0.1.2
' >> requirements.txt
```

Agora é só instalar normalmente usando `pip install -r requirements.txt`, como sempre.

## Contribuíndo com o desenvolvimento do framework

> Aqui entende-se que o ambiente já esteja configurado para fazer acesso usando SSH ao repositório git do GitLab.

> Daqui para frente entende-se o uso do Linux ou Mac. Fique à vontade para documentar para Windows. 

1. Crie um ambiente virtual usando `mkvirtualenv bds-framework` ou da formas que você está aconstumado a usar 
2. Clone o projeto `git clone ssh://git@git.lais.huol.ufrn.br:2222/barramento/barramento-v2/bds-framework.git`
3. Entre com o código `cd bds-framework`
4. Instale os pacotes `pip install -r requirements`
5. Crie um branch para a issue em que você está vai trabalhar, no exemplo de ser a issue 4: `git checkout -b issue4`  
6. Codifique como de costume
7. Antes de fazer um push para o Gitlab confira a qualidade do código (todos serão gerados e salvos no servidor)
   1. Confira se o código está bem formatado: `flake8`. A meta não haver mensagem alguma
   2. Confira se a tipagem do código está boa: `mypy bds_framework`. A meta não haver mensagem alguma
   3. Confira se todos os testes passam: `python -m pytest`. A meta é cobertura superior a 92% e sucesso nos testes de 100%
8. Crie um Merge Request para a branch `main` e atribua a `kelson.medeiros`

## Dicas

1. Para saber se a documentação pydocs `pdoc --html -o artifacts/pydocs --config show_source_code=False --force bds/`
2. Ao subir o código a documentação está pública em .


## Tipo de commits

- `feat:` novas funcionalidades.
- `fix:` correção de bugs.
- `refactor:` refatoração ou performances (sem impacto em lógica).
- `style:` estilo ou formatação de código (sem impacto em lógica).
- `test:` testes.
- `doc:` documentação no código ou do repositório.
- `env:` CI/CD ou settings.
- `build:` build ou dependências.
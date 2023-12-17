# Portal Legal H2

Bem-vindo ao Portal Legal H2! Este é um projeto web construído com o framework Django para fornecer informações sobre o hidrogênio.

## Visão Geral

O Portal Legal H2 oferece várias funcionalidades, incluindo:

- **Página Inicial:** Apresenta as últimas notícias sobre hidrogênio.
- **Quem Somos:** Detalhes sobre a equipe e a missão do Portal Legal H2.
- **Contato:** Formulário de contato para se comunicar conosco.
- **Mapa Informativo:** Explore um mapa interativo com informações sobre locais relacionados ao hidrogênio.

## Configuração do Ambiente de Desenvolvimento

1. Certifique-se de ter Python instalado em seu sistema.
2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use "venv\Scripts\activate"

Instale as dependências:
    
    pip install -r requirements.txt
    
Execute as migrações do banco de dados:
    
    python manage.py migrate
    
Inicie o servidor de desenvolvimento:

    python manage.py runserver
Acesse a aplicação em http://localhost:8000/.

Estrutura do Projeto

    blog: Aplicação principal do Django.
    
    static: Arquivos estáticos (CSS, JavaScript, imagens).
    templates: Modelos HTML usando o Django Template Language.
    views.py: Lógica de visualização.
    portallegalh2: Configurações globais do projeto Django.
    
    settings.py: Configurações do Django.
    urls.py: Mapeamento de URLs.

Contribuições
Contribua para o projeto abrindo problemas ou enviando solicitações de pull.

Autor
    André Oliveira/Fernando Mateus/Sayonara Eliziario

Licença
Este projeto é licenciado sob a Licença MIT.


<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="API_REST__BHUB_0"></a>API REST - BHUB</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="_WEBSERVICO_para_desafio_da_BHUB__1"></a><em>WEB-SERVICO para desafio da BHUB</em></h2>
<p class="has-line-data" data-line-start="5" data-line-end="6">Durante o processo de seleção foi solicitado o desenvolvimento de um web-service RESTful utilizando qualquer linguagem de programação e framework.</p>
<p class="has-line-data" data-line-start="7" data-line-end="10">Aplicação esta hospedada nos serviços do host provider Heroku.<br>
<a href="https://bhub-desafio.herokuapp.com/api/v1/">https://bhub-desafio.herokuapp.com/api/v1/</a><br>
<a href="https://bhub-desafio.herokuapp.com/api/v1/swagger/">https://bhub-desafio.herokuapp.com/api/v1/swagger/</a></p>
<h2 class="code-line" data-line-start=11 data-line-end=12 ><a id="Tecnologias_Utilizadas_11"></a>Tecnologias Utilizadas</h2>
<ul>
<li class="has-line-data" data-line-start="13" data-line-end="14">Python</li>
<li class="has-line-data" data-line-start="14" data-line-end="15">Django</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Django Rest Framework</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Django Simple JWT</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">Django Swagger</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">Django Cors</li>
<li class="has-line-data" data-line-start="19" data-line-end="20">DB CLOUD Postgresql</li>
<li class="has-line-data" data-line-start="20" data-line-end="21">DB LOCALBASE SQLITE3</li>
<li class="has-line-data" data-line-start="21" data-line-end="22">Host Provider HEROKU</li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Docker</li>
</ul>
<h2 class="code-line" data-line-start=25 data-line-end=26 ><a id="Funcionalidades_25"></a>Funcionalidades</h2>
<ul>
<li class="has-line-data" data-line-start="27" data-line-end="28">Todas as principais ações CRUD</li>
<li class="has-line-data" data-line-start="28" data-line-end="29">Proteção de Views por Token JWT</li>
<li class="has-line-data" data-line-start="29" data-line-end="30">Disponibilidade de configuração de acesso de Host por CORS</li>
<li class="has-line-data" data-line-start="30" data-line-end="31">Documentação em Swagger</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">Testes Unitarios das aplicações Django</li>
</ul>
<h2 class="code-line" data-line-start=35 data-line-end=36 ><a id="Installation_35"></a>Installation</h2>
<p class="has-line-data" data-line-start="36" data-line-end="37">Aplicacao necessita da versao Python 3.7.14</p>
<p class="has-line-data" data-line-start="40" data-line-end="41">Instale as dependências e inicie o servidor.</p>
<pre><code class="has-line-data" data-line-start="43" data-line-end="47" class="language-sh"><span class="hljs-built_in">cd</span> API-CRUD-DJANGO
pip install -r requirements.txt
python manage.py runserver
</code></pre>
<h2 class="code-line" data-line-start=51 data-line-end=52 ><a id="Docker_51"></a>Docker</h2>
<p class="has-line-data" data-line-start="53" data-line-end="54">O Dillinger é muito fácil de instalar e implantar em um contêiner do Docker.</p>
<p class="has-line-data" data-line-start="55" data-line-end="58">Por padrão, o Docker irá expor a porta 8000, então altere isso dentro do<br>
Dockerfile se necessário. Quando estiver pronto, basta usar o Dockerfile para<br>
construir a imagem.</p>
<pre><code class="has-line-data" data-line-start="60" data-line-end="64" class="language-sh">docker-compose run web python src/BHub/manage.py migrate
docker-compose build
docker-compose up
</code></pre>
<p class="has-line-data" data-line-start="65" data-line-end="66">Isso criará a imagem do API-CRUD-DJANGO e extrairá as dependências necessárias.</p>
<h2 class="code-line" data-line-start=67 data-line-end=68 ><a id="License_67"></a>License</h2>
<p class="has-line-data" data-line-start="69" data-line-end="70">MIT</p>
<p class="has-line-data" data-line-start="71" data-line-end="72"><strong>Free Software, Hell Yeah!</strong></p>
<h1 align="center" class="code-line" data-line-start=0 data-line-end=1 ><a id="API_REST__BHUB_0"></a>API REST - BHUB</h1>
<h2 align="center" class="code-line" data-line-start=1 data-line-end=2 ><a id="_WEBSERVICO_para_desafio_da_BHUB__1"></a><em>WEB-SERVICO para desafio da BHUB</em></h2>
<p class="has-line-data" data-line-start="4" data-line-end="5">Durante o processo de seleção foi solicitado o desenvolvimento de um web-service RESTful utilizando qualquer linguagem de programação e framework.</p>
<p class="has-line-data" data-line-start="6" data-line-end="7">Aplicação esta hospedada nos serviços do host provider Heroku.&lt;br&gt;</p>
<p class="has-line-data" data-line-start="8" data-line-end="9"><a href="https://bhub-desafio.herokuapp.com/api/v1/">https://bhub-desafio.herokuapp.com/api/v1/</a>&lt;br&gt;</p>
<p class="has-line-data" data-line-start="10" data-line-end="11"><a href="https://bhub-desafio.herokuapp.com/api/v1/swagger/">https://bhub-desafio.herokuapp.com/api/v1/swagger/</a></p>
<h2 class="code-line" data-line-start=12 data-line-end=13 ><a id="Tecnologias_Utilizadas_12"></a>Tecnologias Utilizadas</h2>
<ul>
<li class="has-line-data" data-line-start="14" data-line-end="15">Python</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Django</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">Django Rest Framework</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">Django Simple JWT</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">Django Swagger</li>
<li class="has-line-data" data-line-start="19" data-line-end="20">Django Cors</li>
<li class="has-line-data" data-line-start="20" data-line-end="21">DB CLOUD Postgresql</li>
<li class="has-line-data" data-line-start="21" data-line-end="22">DB LOCALBASE SQLITE3</li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Host Provider HEROKU</li>
<li class="has-line-data" data-line-start="23" data-line-end="24">Docker</li>
<li class="has-line-data" data-line-start="24" data-line-end="26">Consumo de Api</li>
</ul>
<h2 class="code-line" data-line-start=26 data-line-end=27 ><a id="Funcionalidades_26"></a>Funcionalidades</h2>
<ul>
<li class="has-line-data" data-line-start="28" data-line-end="29">Todas as principais ações CRUD</li>
<li class="has-line-data" data-line-start="29" data-line-end="30">Proteção de Views por Token JWT</li>
<li class="has-line-data" data-line-start="30" data-line-end="31">Disponibilidade de configuração de acesso de Host por CORS</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">Documentação em Swagger</li>
<li class="has-line-data" data-line-start="32" data-line-end="33">Testes Unitarios das aplicações Django</li>
<li class="has-line-data" data-line-start="33" data-line-end="35">Consumo de API externa para trazer todos os bancos existentes</li>
</ul>
<h2 class="code-line" data-line-start=35 data-line-end=36 ><a id="Installation_35"></a>Installation</h2>
<p class="has-line-data" data-line-start="37" data-line-end="38">Aplicacao necessita da versao Python 3.7.14</p>
<p class="has-line-data" data-line-start="39" data-line-end="40">Instale as dependências e inicie o servidor.</p>
<pre><code class="has-line-data" data-line-start="42" data-line-end="46">&lt;span class=&quot;hljs-built_in&quot;&gt;cd&lt;/span&gt; API-CRUD-DJANGO
pip install -r requirements.txt
python manage.py runserver
</code></pre>
<h2 class="code-line" data-line-start=47 data-line-end=48 ><a id="Docker_47"></a>Docker</h2>
<p class="has-line-data" data-line-start="49" data-line-end="50">O Dillinger é muito fácil de instalar e implantar em um contêiner do Docker.</p>
<p class="has-line-data" data-line-start="51" data-line-end="52">Por padrão, o Docker irá expor a porta 8000, então altere isso dentro do&lt;br&gt;</p>
<p class="has-line-data" data-line-start="53" data-line-end="54">Dockerfile se necessário. Quando estiver pronto, basta usar o Dockerfile para&lt;br&gt;</p>
<p class="has-line-data" data-line-start="55" data-line-end="56">construir a imagem.</p>
<pre><code class="has-line-data" data-line-start="58" data-line-end="62">docker-compose run web python src/BHub/manage.py migrate
docker-compose build
docker-compose up
</code></pre>
<p class="has-line-data" data-line-start="63" data-line-end="64">Isso criará a imagem do API-CRUD-DJANGO e extrairá as dependências necessárias.</p>
<h2 class="code-line" data-line-start=65 data-line-end=66 ><a id="License_65"></a>License</h2>
<p class="has-line-data" data-line-start="67" data-line-end="68">MIT</p>
<p class="has-line-data" data-line-start="69" data-line-end="70"><strong>Free Software, Hell Yeah!</strong></p>
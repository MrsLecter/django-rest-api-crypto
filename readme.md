## Django REST Framework 
## About
<p>REST API using django-rest-api framework. On schedule (every minute), using task scheduler, collects information from 5 cryptocurrency exchanges (each exchange has its own api), calculates the average value for cryptocurrencies (BTC, ETH, USDT, USDC, BNB, BUSD, XRP, ADA, SOL, DOT) and adds data to the database. The project implements access to <i>/api/v1/currency</i> endpoints using a token. It also provides for getting the rate from a specific exchange <i>api/v1/market/[market]</i></p>
 
### Includes
- work with api (coinbase, coinmarket, coinpaprika, kucoin, coinstat)
- token-based auth
- db included
- used pagination (<i>/api/v1/currency/?offset=2</i>)
- use cron to update db data
### Endpoints
<ul>
<li><code>http://[your_host]:[your_port]/admin/</code> - admin panel</li>
<li><code>http://[your_host]:[your_port]/api/v1/market/<str:market>/</code> - get currency rate for current market</li>
<li><code>http://[your_host]:[your_port]/api/v1/auth/users/</code> - user registration (POST)</li>
<li><code>http://[your_host]:[your_port]/auth/token/login/</code> - login and receive token (POST)</li>
<li><code>http://[your_host]:[your_port]/api/v1/currency/</code> - use with header {Authorization: Token 'YOUR_TOKEN'} {GET}</li>
<li><code>http://[your_host]:[your_port]/auth/token/logout/</code> - logout use with header {Authorization: Token 'YOUR_TOKEN'} (POST)</li>
</ul>

### Usage
1) Activate virtual environment variable: source [env]/bin/activate
2) Run project python manage.py runserver

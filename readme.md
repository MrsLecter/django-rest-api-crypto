## Django REST Framework 
### Includes
- work with api (coinbase, coinmarket, coinpaprika, kucoin, coinstat)
- token-based auth
- db included
- used pagination (/api/v1/currency/?offset=2)
- use cron to update db data
### How to use

<code>http://[your_host]:[your_port]/admin/</code> - admin panel
<code>http://[your_host]:[your_port]/api/v1/market/<str:market>/</code> - get currency rate for current market
<code>http://[your_host]:[your_port]/api/v1/auth/users/</code> - user registration (POST)
<code>http://[your_host]:[your_port]/auth/token/login/</code> - login and receive token (POST)
<code>http://[your_host]:[your_port]/api/v1/currency/</code> - use with header {Authorization: Token 'YOUR_TOKEN'} {GET}
<code>http://[your_host]:[your_port]/auth/token/logout/</code> - logout use with header {Authorization: Token 'YOUR_TOKEN'} (POST)
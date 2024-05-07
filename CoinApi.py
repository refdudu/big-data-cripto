import requests
class CoinApi:
    def get(self):
        url = 'https://api.coingecko.com/api/v3/coins/markets'
        params = {
            'vs_currency': 'brl',
            'ids': 'dogecoin,bitcoin,ethereum',
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data


class CoinApiMock:
    def get(self):
        with open('coin.json', 'r') as f:
            # Carregar os dados do arquivo JSON
            dados = json.load(f)
            json_formatado = json.dumps(dados, indent=4)
            return json.loads(json_formatado)
            return jsonify(json.loads(json_formatado))

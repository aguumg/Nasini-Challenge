import pyRofex
import sys

symbol = sys.argv[1]
user = sys.argv[3]
pw = sys.argv[5]
account = sys.argv[7]

print('Iniciando sesión en Remarkets')
while True:
	try:
		pyRofex.initialize(user=user,
		password=pw,
		account=account,
		environment=pyRofex.Environment.REMARKET)

		print('Consultando símbolo')
		md = pyRofex.get_market_data(ticker=symbol, entries=[pyRofex.MarketDataEntry.BIDS, pyRofex.MarketDataEntry.LAST])

		if md['status'] == 'ERROR':
			print('Símbolo inválido')

		elif md['status'] == 'OK':
			md_price = md['marketData']['LA']['price']

			print('Último precio operado: $' + str(md_price))

			print('Consultando BID')

			if str(md['marketData']['BI']) == 'None':
				print('No hay BIDs activos')
				print('Ingresando orden a: $' + str(75.25))
				order = pyRofex.send_order(ticker = symbol,
			                           side = pyRofex.Side.BUY,
			                           size = 1,
			                           price = 75.25,
			                           order_type = pyRofex.OrderType.LIMIT)

			else:
				md_bid_price = md['marketData']['BI'][0]['price']
				print('Precio de BID: $' + str(md_bid_price))
				print('Ingresando orden a: $' + str(round(md_bid_price-0.01,5)))
				order = pyRofex.send_order(ticker = symbol,
			                           side = pyRofex.Side.BUY,
			                           size = 1,
			                           price = round(md_bid_price-0.01,5),
			                           order_type = pyRofex.OrderType.LIMIT)

		print('Cerrando sesión en Remarkets')
		break

	except Exception:
		print("Error! Revise las credenciales ingresadas")
		break

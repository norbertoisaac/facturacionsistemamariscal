#	Autor: Norberto Núñez (norbertoisaac2@gmail.com)
#	Fecha: 2024/05/12
#	Archivo: src/facturacionMLS.py
#	Lenguage: Python3.12
#	Descripción: Rutinas para reporte de facturación de locatarios del Shopping Mariscal Lopez
import time
t = time.time()
timeStampStr = time.strftime("%Y-%m-%dT%H:%M:%S",time.gmtime(t))

# Constantes
servicioHttp = 'https://sistema.mariscal.com.py/api/contrato/ventas'
servicioHttpTimeout = 5
logFileDir = '.'
logFileSuffix = 'transaction.log'
logFilePath = logFileDir + '/' + time.strftime("%Y-%m-%d",time.gmtime(t)) + '-' + logFileSuffix
resultCode = 1
logString = timeStampStr
logTransactionSwitch = False

if __name__ == '__main__':
	import sys
	if len(sys.argv)>1:
		inputFile = False
		# Argumentos de la línea de comandos
		for arg in sys.argv[1:]:
			if arg == '--log':
				logTransactionSwitch = True
			else:
				inputFile = arg
		# Procesamiento de los datos de entrada en CSV
		if inputFile:
			encabezadosLinea = False
			operacionLinea = False
			try:
				f=open(inputFile,'r')
				encabezadosLinea=f.readline().strip()
				operacionLinea=f.readline().strip()
				f.close()
			except:
				logString += ' resultCode=1 msj=errorAlAbrirElArchivoCsv'
			if operacionLinea and encabezadosLinea:
				encabezadosLista=encabezadosLinea.split(',')
				operacionLista=operacionLinea.split(',')
				if len(encabezadosLista) == len(operacionLista):
					token=False
					venta={}
					post={'contrato':'','fecha':'','ventas':[]}
					for i in range(len(encabezadosLista)):
						if encabezadosLista[i] == 'token':
							token=operacionLista[i]
						elif encabezadosLista[i] == 'contrato':
							post['contrato']=operacionLista[i]
						elif encabezadosLista[i] == 'fecha':
							post['fecha']=operacionLista[i]
							venta['fecha']=operacionLista[i]
						else:
							venta[encabezadosLista[i]]=operacionLista[i]
					post['ventas']=[venta]
					if token:
						import json
						postJson=json.dumps(post)
						##################
						import urllib.request
						import urllib.error
						try:
							h1Req=urllib.request.Request(servicioHttp, data=postJson.encode(), headers={'Authorization':'Bearer '+token, 'Content-Type':'application/json', 'Accept':'application/json'})
							h1Resp=urllib.request.urlopen(h1Req,data=postJson.encode(),timeout=servicioHttpTimeout)
							httpRetCode=h1Resp.status
							httpRetReason=h1Resp.reason
							logString += ' resultCode=' + str(httpRetCode) + ' msj=' + httpRetReason.replace(' ','_') + ' httpPost=' + postJson
							if httpRetCode == 200:
								resultCode = 0
						except urllib.error.HTTPError as err:
							logString += ' resultCode=' + str(err.code) + ' msj=' + err.reason.replace(' ','_') + ' httpPost=' + postJson
						##################
					else:
						logString += ' resultCode=1 msj=aunsenciaDeTokenEnElArchivoCsv'
				else:
					logString += ' resultCode=1 msj=archivoCsvInconsistente'
			else:
				logString += ' resultCode=1 msj=archivoCsvInvalido'
	if logTransactionSwitch:
		try:
			logString += '\n'
			f = open(logFilePath,'a')
			f.write(logString)
			f.close()
		except:
			print('Error al escribir el archivo ' + logFilePath + '\n' + logString)
exit(resultCode)

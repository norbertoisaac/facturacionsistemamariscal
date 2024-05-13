#	Autor: Norberto Núñez (norbertoisaac2@gmail.com)
#	Fecha: 2024/05/12
#	Archivo: src/facturacionMLS.py
#	Lenguage: Python3.12
#	Descripción: Rutinas para reporte de facturación de locatarios del Shopping Mariscal Lopez

# Constantes
servicioHttp='https://sistema.mariscal.com.py/api/contrato/ventas'
servicioHttpTimeout=5

if __name__ == '__main__':
	import sys
	if len(sys.argv)>1:
		try:
			f=open(sys.argv[1],'r')
			encabezadosLinea=f.readline().strip()
			operacionLinea=f.readline().strip()
			f.close()
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
					h1Req=urllib.request.Request(servicioHttp, data=postJson.encode(), headers={'Authorization':'Bearer '+token, 'Content-Type':'application/json', 'Accept':'application/json'})
					h1Resp=urllib.request.urlopen(h1Req,data=postJson.encode(),timeout=servicioHttpTimeout)
					httpRetCode=h1Resp.status
					httpRetReason=h1Resp.reason
					print(httpRetCode,httpRetReason)
					if httpRetCode == 200:
						exit(0)
					##################
		except:
			pass
exit(1)

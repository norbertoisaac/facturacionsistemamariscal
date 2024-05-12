curl --location 'https://sistema.mariscal.com.py/api/contrato/ventas' \
--header 'Accept: application/json' \
-H "Authorization: Bearer mytoken123" \
--data '{
    "contrato": "C0000000695",
    "fecha": "30-07-2023",
    "ventas": [
        {
            "comprobante": "001-001-1000001",
            "fecha": "30-07-2023",
            "tipo": "FACT",
            "moneda": "GS",
            "tipoCambio": "0",
            "gravadas10": "0",
            "gravadas5": "0.00",
            "exentas": "0.00",
            "total": "0",
            "cliente": "SIN NOMBRE",
            "ruc": "0000000-0"
        }
       
    ]
}'

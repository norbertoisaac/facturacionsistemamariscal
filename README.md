# Reporte de facturación del sistema de mariscal López Shopping
# Prerrequisito
Instalar Python3.12, preferentemente desde el microsoft store
# Forma de uso
```
python3 src/facturacionMLS.py tests/factura-2024-05-12-10-00-00-000000.csv
```
, donde el archivo tests/factura-2024-05-12-10-00-00-000000.csv tiene dos líneas, cada línea con campos y valores separados por comas, la primera línea son los encabezados y la segunda línea los valores correspondientes de las columnas:
```
token,contrato,comprobante,fecha,tipo,moneda,tipoCambio,gravadas10,gravadas5,exentas,total,cliente,ruc
mytoken123,C0000000695,001-001-1000001,30-07-2023,FACT,GS,0,0,0.00,0.00,0,SIN NOMBRE,0000000-0
```
La ejecución del comando devuelve True o 0 en caso de éxito, en cualquier otro caso devuelve False o 1.

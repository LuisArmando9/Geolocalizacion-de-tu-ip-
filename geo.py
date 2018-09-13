import os
import sys
#Autor @ArmWan
#correo ah25632@gmail.com

# se verifica que tu version python sea mayor a 3 
if sys.version_info >= (3,0):
    try:
        # se importan modulos 
        from bs4 import BeautifulSoup
        from geolite2 import geolite2
        import requests
        #Si manda una exepcion de que no esten instalados los forzara a instalar
    except ModuleNotFoundError:
        os.system('pip install bs4') 
        os.system('pip maxminddb-geolite2')
        os.system('pip install requests')
else:
    print("Necesitas una version mayor a 3 de python")  
# se declara una funcion para obtener la ip          
def ip():
    #la url de donde sacaremos la ip
    url = "http://www.vermiip.es/"
    try:
        # se verifica si hay conexion con la pagina 
        reque = requests.get(url)
        if reque.status_code == 200:
            # se obtiene el los elementos html
            html = BeautifulSoup(reque.text, 'html.parser')
            ip = html.h2.text.split(" ")[4]
            return ip
    except:
        print('No se puede obtener la ip')
# hacemos una funcion para la localizacion                   
def location():
    # mandamos a llamar la funcion que nos retornara la ip
    ipv4 = ip()
    #mandarmos a llamar el metodo lector de geolite2
    geo = geolite2.reader()
    #comprueba si get esta recibiendo la ip
    try:
        info = geo.get(ipv4)
        #compruba si el info tiene elementos
        if len(info) > 0:
            #creamos un diccionario con las caractericas+
            descr ={
                 'Municipio': info['city']['names']['en'],
                'Estado': info['subdivisions'][0]['names']['en'],
                 'Pais': info['country']['names']['en'],
                 'Continente': info['continent']['names']['en'],
                  'Latitud': info['location']['latitude'],
                  'longitud': info['location']['longitude'],
                  'ZonaHoraria': info['location']['time_zone'],
                  'CodigoPostal': info['postal']['code'],
                  'Ippublica': ipv4
             }
            #retornamos el diccionario
            return descr
    except TypeError:
        # Si no recibe la ip  
        return "No se puede obtener la localizacion"         
if __name__ == '__main__':
    print(location())


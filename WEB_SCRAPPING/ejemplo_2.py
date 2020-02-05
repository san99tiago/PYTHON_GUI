#Santiago Garcia Arango, 4 febrero de 2020
#CONTINUACION CON EJEMPLO 1 (mejorado) DE WEB SCRAPPING
#-----------------------------------------------------------------
#Librerias de trabajo para trabajo con descargas de paginas web...

#Incluidas en python:
import requests

#NO INCLUIDAS EN PYTHON (se debe descargar usando "pip install"):
#pip install beautifulsoup4
from bs4 import BeautifulSoup



#Se ingresa link de pagina web a revisar
url_1 = 'https://www.pagina12.com.ar/'

#Se ejecuta comando para hacer el request a la pagina web indicada
pagina_obtenida = requests.get(url_1)

#Se verifica que haya sido exitoso el request realizado previamente
#codigo de estado correcto = 200 
INFO_1_codigo_estado = pagina_obtenida.status_code

#Se muestra lo obtenido gracias a este request ()
INFO_2_texto = pagina_obtenida.text

#Se obtienen los titulos o "headers" encontrados en la pagina web
INFO_3_titulos_generales = pagina_obtenida.headers

#Se obtiene informacion del request hecha por nosotros
INFO_4_request_propio = pagina_obtenida.request.headers

#Se "parsea" o "mejora" texto encontrado en pagina web 
#NOTA: se recomienda parser "lxml"
#OJO: sopa_1 se debe imprimir asi: "print(sopa_1.prettify() )" para que...
#...quede con orden y estructura organizada e indentada (jerarquia)
sopa_1 = BeautifulSoup( pagina_obtenida.text , "lxml" )

#Ahora busquemos etiquetas deseadas (esto se hace como imagenes en folder de este archivo)...
#recordemos que para encontrar etiquetas en primer lugar, se debe buscar en el "developer tools"...
#de la pagina web visitada (nosotros las buscamos manualmente como se muestra en imagenes)
#Se depura la busqueda diciendo que unicamente me interesan los "li" (list items ), con ventaja de...
#obtener info en terminos de lista (de cada uno de los encontrados en "find_all")
encabezados_principales = sopa_1.find( "ul", attrs = {"class":"hot-sections"} ).find_all("li")

#Ahora recorremos cada uno de los encabezados y obtenemos su texto propio y su link respectivo
nombres_encabezados = []
links_encabezados = []

vector_nombres_todas_las_noticias = []
vector_links_todas_las_noticias = []

for i in range( len(encabezados_principales) ):
    #Se obtienen respectivamente textos y links de los encabezados
    nombres_encabezados.append( encabezados_principales[i].a.get_text() )
    links_encabezados.append( encabezados_principales[i].a.get("href") )

    #Se activa request a cada uno de los links indicados en encabezados respectivos
    pagina_secundaria = requests.get( links_encabezados[i] )

    #Se parsea info obtenida de pagina_secundaria respectiva
    sopa_secundaria = BeautifulSoup( pagina_secundaria.text, "lxml" )
    

    #Se crea vector para almacenar info de cada una de las hot sections (al ingresar a ellas)
    #OJO: se buscan los "h2", porque son los headers que contienen a "a" que contienen a su vez el texto
    vector_info_interna_noticias = sopa_secundaria.find("ul", attrs = {"class":"article-list"}).find_all("h2")
    
    #Se accede cuidadosamente a toda la info de cada subpagina (y luego se almacena en vector)...
    #es decir, vector de vectores
    nombres_noticias_secundarias = []
    links_noticias_secundarias = []
    for j in range( len(vector_info_interna_noticias) ):
        nombres_noticias_secundarias.append( vector_info_interna_noticias[j].a.get_text() )
        links_noticias_secundarias.append( vector_info_interna_noticias[j].a.get("href") )
   
    vector_nombres_todas_las_noticias.append( nombres_noticias_secundarias )
    vector_links_todas_las_noticias.append( links_noticias_secundarias )


#-------------------------------------------------------------------------
#SE MUESTRA TODO (PREFERIBLEMENTE UNO A UNO VISUALIZAR)
# print(INFO_1_codigo_estado)
# print(INFO_2_texto)
# print(INFO_3_titulos_generales)
# print(INFO_4_request_propio)
# print(sopa_1.prettify()  )
print(encabezados_principales )

#Se muestra la info valiosa de este codigo (vector nombres encabezados y vector de links )
print("\n\nNOMBRES ENCABEZADOS (VECTOR):")
print(nombres_encabezados)
print("\n\nLINKS ENCABEZADOS RESCPECTIVOS (VECTOR):")
print(links_encabezados)

print("\n\nVECTOR CON NOMBRES TODAS LAS NOTICIAS DE LAS PAGINAS SECUNDARIAS:")
print(vector_nombres_todas_las_noticias)

print("\n\nVECTOR CON LINKS TODAS LAS NOTICIAS DE LAS PAGINAS SECUNDARIAS:")
print(vector_links_todas_las_noticias)

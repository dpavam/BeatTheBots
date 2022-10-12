# Benzebot

### El Benzebot nos llevará al clasico

## Librerias: 
  - pip install selenium
  - pip install webdriver-manager
  
## Requerimientos:
- Google Chrome
  
### Como functiona
- Solo hay que ejectuar el archivo Ejecutar el archivo `ticket_function.py`
 Esto va a abrir una ventana de Chrome con el link al partido. No hay que hacer nada más, Benzebot lo hace todo. 

- *No minimizar*, se puede dejar al fondo (cambiar de programa o ventana). 

El script va a intentar bajar hasta donde se vean las localidades del estadio, hacer click sobre las localidades disponibles, sino refresca la pagina y vuelve a empezar.

## Consideraciones
El método actual puede buscar boletas por aproximadamente 4 minutos, luego, la página deja de mostrar la ventan de compra. Cuando se llega a los 4 minutos, hay 3 sonidos para alertar al usuario que es hora de volver a ejecutar el archivo.

Si por obra y gracia del espiritú de Messi hay una boleta, el script emite *un sonido* y trata de seleccionar la silla disponible. Si no hay una silla roja seleccionada, quiere decir que un bot nos dio piso. 


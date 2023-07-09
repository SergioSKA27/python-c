import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import base64
import struct
import math
from streamlit_extras.echo_expander import echo_expander
from code_editor import code_editor
import subprocess

st.set_page_config(
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


st.title(' 1. Introducción')
txt0 =r'''
# 1.1. Algoritmos
<div style="text-align: justify;">
Si la resolución de problemas es una parte central de la informática, entonces las soluciones que cree a través del
proceso de resolución de problemas también son importantes. En informática, nos referimos a estas soluciones como
algoritmos. Un algoritmo es una lista paso a paso de instrucciones que, si se siguen exactamente, resolverán el problema
en cuestión.

Por ejemplo, un algoritmo para calcular el área de un círculo dado su radio podría verse así:
| Ejemplo de algoritmo 1:|
|----------------------------|
| 1. Preguntar por el radio|
| 2. Calcule el área elevando al cuadrado el radio y multiplicando el resultado por $\pi$|
| 3. Mostrar el área calculada|

Tenga en cuenta que este algoritmo consta de un conjunto de pasos numerados. Está escrito en inglés, para facilitar
su comprensión. Aunque los algoritmos simples se entienden fácilmente cuando están escritos en inglés, los algoritmos
más complicados necesitan una notación más precisa. Para mejorar la precisión, los algoritmos a menudo se escriben en
pseudocódigo. El pseudocódigo es una notación que es más precisa que el inglés pero generalmente no tan precisa como un
lenguaje de programación. El mismo algoritmo expresado en pseudocódigo podría verse así:

|Ejemplo de algoritmo 2 (pseudocódigo)|
|----------------------------------|
|1. Preguntar por el  radio|
|2. Sea área = $radio^2\times \pi$|
|3. Visualización del Área|

Observe cómo el ejemplo de pseudocódigo expresa el paso 2 con mayor precisión, especificando la fórmula en términos
matemáticos.

Nuestro objetivo en informática es tomar un problema y desarrollar un algoritmo que pueda servir como una solución
general. Una vez que tengamos tal solución, podemos usar nuestra computadora para automatizar su ejecución usando
programación. La programación es una habilidad que permite a un informático tomar un algoritmo y representarlo en una
notación (un programa) que puede ser seguido por una computadora. Un programa está escrito en un lenguaje de
programación como Python, el lenguaje que aprenderá en este libro.

Para ayudarlo a comprender la diferencia entre un algoritmo y un programa, considere este programa para calcular
el área de un círculo:
</div>
'''
st.markdown(txt0, unsafe_allow_html=True)

with st.expander(label="Implementación en Python"):

    st.code(
    '''
    radius = int(Input("Enter the radius:"))
    area = (radius * radius) * 3.1415
    print("The area of a circle with radius", radius, "is:", area)'''
    )
r = st.number_input('Ingrese el radio',value=0)
if st.button('Ejecutar'):
    f = lambda r: (r * r) * 3.1415
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write('The area of a circle with radius, ',r,'is:',f(r))


txt1 = r'''
<div style="text-align: justify;">
Un programa es un algoritmo expresado en un lenguaje de programación. También podríamos decir que un programa es una
implementación de un algoritmo. En este ejemplo, tanto el algoritmo como el programa tienen tres pasos.
El primer paso obtiene alguna entrada del usuario y la entrada en algo con lo que la computadora puede hacer
matemáticas; el segundo paso realiza un cálculo utilizando la información obtenida en el primer paso; y el paso
final muestra el resultado al usuario. Aunque no hemos cubierto ningún detalle de Python, esperamos que pueda ver
la correspondencia entre los pasos del algoritmo, que podría ser seguido por un humano (pero no ejecutado por una
computadora), y los pasos del programa, que puede ser ejecutado por una computadora (intente ejecutar este usando el
botón Ejecutar).

Los algoritmos son importantes porque el proceso de resolver un problema a través de la programación a menudo
comienza con el diseño de un algoritmo. El programador a menudo expresa el algoritmo en pseudocódigo,
luego convierte el algoritmo en un programa para que la computadora lo ejecute. En la siguiente sección,
aprenderá cómo ejecutar programas de Python en una computadora.
</div>
'''

st.markdown(txt1, unsafe_allow_html=True)




txt2 = r'''
# 1.2. El lenguaje de programación Python
<div style="text-align: justify;">
El lenguaje de programación que aprenderás es Python. Python es un ejemplo de lenguaje de alto nivel;
otros lenguajes de alto nivel de los que quizás haya oído hablar son C++, PHP y Java.

Como puede inferir del nombre lenguaje de alto nivel, también hay lenguajes de bajo nivel, a veces denominados lenguajes
de máquina o lenguajes ensambladores. En términos generales, las computadoras solo pueden ejecutar programas escritos en
lenguajes de bajo nivel. Por lo tanto, los programas escritos en un lenguaje de alto nivel deben procesarse antes de que
puedan ejecutarse. Este procesamiento adicional lleva algún tiempo, lo cual es una pequeña desventaja de los lenguajes
de alto nivel. Sin embargo, las ventajas de los lenguajes de alto nivel son enormes.

Primero, es mucho más fácil programar en un lenguaje de alto nivel. Los programas escritos en un lenguaje de alto nivel
toman menos tiempo para escribirse, son más cortos y fáciles de leer, y es más probable que sean correctos. En segundo
lugar, los lenguajes de alto nivel son portátiles, lo que significa que pueden ejecutarse en diferentes tipos de
computadoras con pocas o ninguna modificación. Los programas de bajo nivel pueden ejecutarse en un solo tipo de
computadora y deben reescribirse para ejecutarse en otro.

Debido a estas ventajas, casi todos los programas están escritos en lenguajes de alto nivel. Los lenguajes de bajo
nivel se usan solo para unas pocas aplicaciones especializadas.

Dos tipos de programas procesan lenguajes de alto nivel en lenguajes de bajo nivel: intérpretes y compiladores.
Un intérprete lee un programa de alto nivel y lo ejecuta, lo que significa que hace lo que dice el programa.
Procesa el programa poco a poco, alternativamente leyendo líneas y realizando cálculos.

Un compilador lee el programa y lo traduce completamente antes de que el programa comience a ejecutarse. En este caso,
el programa de alto nivel se denomina código fuente y el programa traducido se denomina código objeto o ejecutable.
Una vez que se compila un programa, puede ejecutarlo repetidamente sin más traducción.

Muchos lenguajes modernos usan ambos procesos. Primero se compilan en un lenguaje de nivel inferior, llamado código
de bytes, y luego se interpretan mediante un programa llamado máquina virtual. Python usa ambos procesos,
pero debido a la forma en que los programadores interactúan con él, generalmente se lo considera un lenguaje
interpretado.
</div>

'''
st.markdown(txt2, unsafe_allow_html=True)




txt3 = r'''
# 1.3. Más sobre los programas
<div style="text-align: justify;">
Un programa es una secuencia de instrucciones que especifica cómo realizar un cálculo. El cálculo puede ser algo tan
complejo como representar una página html en un navegador web o codificar un video y transmitirlo a través de la red.
También puede ser un cálculo simbólico, como buscar y reemplazar texto en un documento o (curiosamente) compilar un
programa.

Los detalles se ven diferentes en diferentes idiomas, pero algunas instrucciones básicas aparecen en casi todos los
idiomas.

aporte
    Obtenga datos del teclado, un archivo o algún otro dispositivo.
producción
    Muestre datos en la pantalla o envíe datos a un archivo u otro dispositivo.
matemáticas y lógica
    Realizar operaciones matemáticas básicas como sumas y multiplicaciones y operaciones lógicas como and, or y not.
ejecución condicional
    Verifique ciertas condiciones y ejecute la secuencia apropiada de instrucciones.
repetición
    Realizar alguna acción repetidamente, generalmente con alguna variación.

Lo creas o no, eso es prácticamente todo lo que hay que hacer. Todos los programas que hayas usado alguna vez, por
complicados que sean, están formados por instrucciones que se parecen más o menos a estas. Por lo tanto, podemos
describir la programación como el proceso de dividir una tarea grande y compleja en subtareas cada vez más pequeñas
hasta que las subtareas sean lo suficientemente simples como para ejecutarlas con secuencias de estas instrucciones
básicas.
</div>

## 1.3.1. Vista previa de estructuras de control
<div style="text-align: justify;">
Todavía no profundizaremos mucho en las estructuras de control de Python, ¡pero es bueno mencionarlas antes para darle
una idea de lo que puede hacer con el lenguaje! Si esto tiene sentido para ti ahora, ¡es genial! Sin embargo,
no esperamos que los entienda todavía; la comprensión vendrá más tarde.

Primero tenemos estructuras que nos permiten iterar sobre algo. Podemos mirar cadenas carácter por carácter o listas
elemento por elemento hasta que hayamos llegado al final de ellas usando algo llamado bucle for.
</div>

'''


st.markdown(txt3, unsafe_allow_html=True)



with st.expander(label="Implementación en Python"):
    st.code('''
    for character in "Cool string":
        print(character)
    ''')
if st.button('Ejecutar',key='button1'):
    s = '```python linenos\n'
    for character in "Cool string":
        s = s +character+'\n'
    s= s + '```'
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(s)




txt4 = r'''


<div style="text-align: justify;">
También podemos iterar sin un punto de parada definido con bucles while.
Puede usar esto si desea recibir información del usuario de su programa,
pero no sabe cuánto tiempo les llevará terminar con su código.
</div>

'''

st.markdown(txt4, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
    grocery_item = ""
    while grocery_item != "done":
        grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list simply type: done")
        print(grocery_item)
    ''')
if st.button('Ejecutar',key='button2'):
    with st.expander(label=":blue[Output: ]",expanded=True):

        st.write("Please write down an item to add to your grocery list. When you are done writing the list simply type: done")
        i0 = 0
        while True:
            grocery_item = st.text_input("Item "+str(i0)+':')
            if grocery_item == '':
                input()
            if grocery_item == 'done':
                break
            st.write(grocery_item)
            i0+=1




txt5 = r'''
<div style="text-align: justify;">
Otras estructuras nos permitirán ejecutar solo partes de nuestros programas o solo hacer alguna tarea si se encuentran
un cierto conjunto de condiciones. Los condicionales, como se les llama, nos permiten hacer eso.
Vea cómo agregar condicionales a nuestro código puede cambiar lo que podemos escribir sobre las compras de comestibles.
</div>
'''


st.markdown(txt5, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
        grocery_item = ""
        grocery_list = []
        while grocery_item != "done":
            grocery_item = input("Please write down an item to add to your grocery list. When you are done writing the list then simply type: done")
            if grocery_item == 'done':
                continue
            else:
                print("adding the item to the list")
                grocery_list.append(grocery_item)
        print("Here is our grocery list:")
        print(grocery_list)
    ''')
if st.button('Ejecutar',key='button3'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        list_of_items = []

        st.write("Please write down an item to add to your grocery list. When you are done writing the list simply type: done")
        i1 = 0
        while True:
            grocery_item = st.text_input("Item "+str(i1)+':')
            if grocery_item == '':
                input()
            if grocery_item == 'done':
                break
            st.write("adding the item to the list")
            list_of_items.append(grocery_item)
            i1+=1
        st.write("Here is our grocery list:")
        st.write(list_of_items)





txt6 = r'''
# 1.4. Lenguajes formales y naturales
<div style="text-align: justify;">


Los idiomas naturales son los idiomas que hablan las personas, como el inglés, el español, el coreano y el chino
mandarín. No fueron diseñados por personas (aunque la gente trata de imponerles algún orden);
evolucionaron naturalmente.

Los lenguajes formales son lenguajes diseñados por personas para aplicaciones específicas. Por ejemplo,
la notación que usan los matemáticos es un lenguaje formal que es particularmente bueno para denotar relaciones
entre números y símbolos. Los químicos usan un lenguaje formal para representar la estructura química de las moléculas.
Y más importante:

Los lenguajes de programación son lenguajes formales que han sido diseñados para expresar cálculos.

Los lenguajes formales tienden a tener reglas estrictas sobre la sintaxis. Por ejemplo, 3+3=6 es un enunciado
matemático sintácticamente correcto, pero 3=+6\$ no lo es. $H_2O$ es un nombre químico sintácticamente correcto,
pero $_2Zz$ no lo es.

Las reglas de sintaxis vienen en dos sabores, pertenecientes a tokens y estructura. Los tokens son los elementos
básicos del lenguaje, como palabras, números y elementos químicos. Uno de los problemas con 3=+6\$ es que \$ no es un
token legal en matemáticas (al menos hasta donde sabemos). Del mismo modo, $_2Zz$ no es legal porque no hay ningún elemento
con la abreviatura $Zz$.


El segundo tipo de regla de sintaxis se relaciona con la estructura de una declaración, es decir, la forma en que
se organizan los tokens. La declaración 3=+6$ es estructuralmente ilegal porque no puede colocar un signo más
inmediatamente después de un signo igual. De manera similar, las fórmulas moleculares deben tener subíndices después
del nombre del elemento, no antes.

Cuando lees una oración en inglés o una declaración en un lenguaje formal, tienes que averiguar cuál es la estructura
de la oración (aunque en un lenguaje natural lo haces inconscientemente). Este proceso se denomina análisis.

Por ejemplo, cuando escuchas la oración, “El otro zapato cayó”, entiendes que el otro zapato es el sujeto y cayó es
el verbo. Una vez que haya analizado una oración, puede averiguar qué significa o la semántica de la oración.
Suponiendo que sabe lo que es un zapato y lo que significa caerse, comprenderá la implicación general de esta oración.

Aunque los lenguajes formales y naturales tienen muchas características en común (tokens, estructura, sintaxis y
semántica), existen muchas diferencias:

**ambigüedad:**
Los lenguajes naturales están llenos de ambigüedad, que las personas manejan usando pistas contextuales y
otra información. Los lenguajes formales están diseñados para ser casi o completamente inequívocos, lo que
significa que cualquier declaración tiene exactamente un significado, independientemente del contexto.

**redundancia:**
Para compensar la ambigüedad y reducir los malentendidos, los lenguajes naturales emplean mucha redundancia.
Como resultado, a menudo son detallados. Los lenguajes formales son menos redundantes y más concisos.

**literalidad:**
Los lenguajes formales significan exactamente lo que dicen. Por otro lado, los lenguajes naturales están llenos
de modismos y metáforas.


Las personas que crecen hablando un idioma natural, es decir, todos, a menudo tienen dificultades para adaptarse a los
idiomas formales. De alguna manera, la diferencia entre lenguaje natural y formal es como la diferencia entre poesía
y prosa, pero más aún:

**poesía:**
Las palabras se usan tanto por sus sonidos como por su significado, y todo el poema en conjunto crea un efecto o
una respuesta emocional. La ambigüedad no solo es común, sino que a menudo es deliberada.

**prosa:**
El significado literal de las palabras es más importante y la estructura aporta más significado. La prosa es más
susceptible de análisis que la poesía, pero sigue siendo a menudo ambigua.

**programa:**
El significado de un programa de computadora es inequívoco y literal, y puede entenderse completamente mediante el
análisis de los tokens y la estructura.

Aquí hay algunas sugerencias para programas de lectura (y otros lenguajes formales). Primero, recuerda que los lenguajes
formales son mucho más densos que los lenguajes naturales, por lo que lleva más tiempo leerlos. Además, la estructura
es muy importante, por lo que no suele ser buena idea leer de arriba a abajo, de izquierda a derecha. En cambio,
aprenda a analizar el programa en su cabeza, identificando los tokens e interpretando la estructura. Finalmente,
los detalles importan. Pequeñas cosas como los errores de ortografía y la mala puntuación, que puede salirse con
la suya en los lenguajes naturales, pueden marcar una gran diferencia en un lenguaje formal.
</div>
'''
st.markdown(txt6, unsafe_allow_html=True)


txt7 =r'''
# 1.5. Un primer programa típico
<div style="text-align: justify;">
Tradicionalmente, el primer programa escrito en un nuevo idioma se llama Hello, World! porque todo lo que hace es
mostrar las palabras ¡Hola, mundo! En Python, el código fuente se ve así.

```python linenos

print("¡Hola, mundo!")

```

Este es un ejemplo del uso de la función de impresión, que en realidad no imprime nada en papel. Muestra un valor en
la pantalla. En este caso, el resultado es la frase:

¡Hola Mundo!

Aquí está el ejemplo en una ventana de código activo, donde puede ejecutarlo
</div>
'''
st.markdown(txt7, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
        print("¡Hola Mundo!")
    ''')
if st.button('Ejecutar',key='button4'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write("¡Hola Mundo!")

txt8 = r'''
# 1.6. Comentarios
<div style="text-align: justify;">
A medida que los programas se hacen más grandes y complicados, se vuelven más difíciles de leer. Los lenguajes formales
son densos y, a menudo, es difícil mirar un fragmento de código y descubrir qué está haciendo o por qué. Por esta razón,
es una buena idea agregar notas a sus programas para explicar en lenguaje natural lo que está haciendo el programa.
Estas notas se denominan comentarios.

Un comentario en un programa de computadora es un texto destinado únicamente al lector humano; el intérprete lo ignora
por completo. En Python, el token # inicia un comentario. El resto de la línea se ignora. Aquí hay una nueva versión de
Hello, World!.
</div>
'''
st.markdown(txt8, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
        #---------------------------------------------------
        # This demo program shows off how elegant Python is!
        # Anyone may freely copy or modify this program.
        #---------------------------------------------------

        print("Hello, World!")     # Isn't this easy!
    ''')
if st.button('Ejecutar',key='button5'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write("Hello, World!")

txt9 =r'''
<div style="text-align: justify;">
Tenga en cuenta que cuando ejecuta este programa, solo imprime la frase Hello, World! No aparece ninguno de los
comentarios. También notará que hemos dejado una línea en blanco en el programa. El intérprete también ignora las
líneas en blanco, pero los comentarios y las líneas en blanco pueden hacer que sus programas sean mucho más fáciles
de analizar para los humanos. ¡Úsalos generosamente!

</div>

# 1.7. Glosario

<div style="text-align: justify;">

:blue[codigo activo:]
    Un entorno de interpretación único que permite ejecutar Python desde un navegador web.

:blue[algoritmo: ]
    Una lista paso a paso de instrucciones que, si se siguen exactamente, resolverán el problema en cuestión.

:blue[bug: ]
    Un error en un programa.

:blue[código de bytes:]
    Un lenguaje intermedio entre el código fuente y el código objeto. Muchos lenguajes modernos primero compilan el código fuente en código de bytes y luego interpretan el código de bytes con un programa llamado máquina virtual.

:blue[codelens:]
    Un entorno interactivo que permite al usuario controlar la ejecución paso a paso de un programa Python

:blue[comentario:]
    Información en un programa que está destinada a otros programadores (o cualquiera que lea el código fuente) y no tiene efecto en la ejecución del programa.

:blue[compilar:]
    Traducir un programa escrito en un lenguaje de alto nivel a un lenguaje de bajo nivel de una sola vez, en preparación para su posterior ejecución.

:blue[depuración:]
    El proceso de encontrar y eliminar cualquiera de los tres tipos de errores de programación: *error de sintaxis*, *error semántico* y *error de tiempo de ejecución*.

:blue[excepción:]
    Otro nombre para un error de tiempo de ejecución.

:blue[ejecutable:]
    Otro nombre para el código objeto que está listo para ser ejecutado.

:blue[lenguaje formal:]
    Cualquiera de los lenguajes que la gente ha diseñado para propósitos específicos, como representar ideas matemáticas o programas de computadora; todos los lenguajes de programación son lenguajes formales.

:blue[lenguaje de alto nivel:]
    Un lenguaje de programación como Python que está diseñado para ser fácil de leer y escribir para los humanos.

:blue[interpretar:]
    Para ejecutar un programa en un lenguaje de alto nivel traduciéndolo una línea a la vez.

:blue[lenguaje de bajo nivel:]
    Un lenguaje de programación que está diseñado para ser fácil de ejecutar para una computadora; también llamado lenguaje máquina o lenguaje ensamblador.

:blue[lenguaje natural:]
    Cualquiera de los idiomas que habla la gente que evolucionó naturalmente.

:blue[código de objeto:]
    La salida del compilador después de traducir el programa.

:blue[analizar gramaticalmente:]
    Examinar un programa y analizar la estructura sintáctica.

:blue[portabilidad:]
    Una propiedad de un programa que puede ejecutarse en más de un tipo de computadora.

:blue[función de impresión:]
    Una función utilizada en un programa o secuencia de comandos que hace que el intérprete de Python muestre un valor en su dispositivo de salida.

:blue[resolución de problemas:]
    El proceso de formular un problema, encontrar una solución y expresar la solución.

:blue[programa:]
    Una secuencia de instrucciones que especifica a una computadora acciones y cálculos a realizar.

:blue[lenguaje de programación:]
    Vocabulario y conjunto de reglas gramaticales para instruir a una computadora o dispositivo informático para que realice tareas específicas.

:blue[Python shell:]
    Una interfaz de usuario interactiva para el intérprete de Python, y el usuario de un shell de Python escribe comandos en el indicador (>>>) y presiona la tecla de retorno para enviar estos comandos inmediatamente al intérprete para su procesamiento. Para iniciar Python Shell, el usuario debe abrir la terminal y escribir "python". Una vez que el usuario presiona enter, aparece Python Shell y el usuario puede interactuar con él.

:blue[Error de tiempo de ejecución:]
    Un error que no ocurre hasta que el programa ha comenzado a ejecutarse pero que impide que el programa continúe.

:blue[error semántico:]
    Un error en un programa que hace que haga algo diferente a lo que pretendía el programador.

:blue[semántica:]
    El significado de un programa.

:blue[modo shell:]
    Un modo de usar Python donde las expresiones se pueden escribir y ejecutar en el símbolo del sistema, y los resultados se muestran inmediatamente en la ventana del terminal de comandos. El modo Shell se inicia abriendo la terminal de su sistema operativo y escribiendo "python". Presiona enter y aparecerá Python Shell. Esto contrasta con el código fuente. Consulte también la entrada en el shell de Python.

:blue[código fuente:]
    Las instrucciones de un programa, almacenadas en un archivo, en un lenguaje de alto nivel antes de ser compiladas o interpretadas.

:blue[sintaxis:]
    La estructura de un programa.

:blue[error de sintaxis:]
    Un error en un programa que lo hace imposible de analizar y, por lo tanto, imposible de interpretar.

:blue[simbólico:]
    Uno de los elementos básicos de la estructura sintáctica de un programa, análoga a una palabra en un lenguaje natural.
</div>
'''
st.markdown(txt9, unsafe_allow_html=True)


code1 = r'''
#Ingresa tu propio código de python y  prueba tus conocimientos :D!
#¡Recuerda que todo lo que ingreses el editor se borrara una vez que cierres la pagina!
'''
bts = [
 {
   "name": "Copy",
   "feather": "Copy",
   "hasText": True,
   "alwaysOn": True,
   "commands": ["copyAll"],
   "style": {"top": "0.46rem", "right": "0.4rem"}
 },
 {
   "name": "Shortcuts",
   "feather": "Type",
   "class": "shortcuts-button",
   "hasText": True,
   "commands": ["toggleKeyboardShortcuts"],
   "style": {"bottom": "calc(50% + 1.75rem)", "right": "0.4rem"}
 },
 {
   "name": "Collapse",
   "feather": "Minimize2",
   "hasText": True,
   "commands": ["selectall",
                "toggleSplitSelectionIntoLines",
                "gotolinestart",
                "gotolinestart",
                "backspace"],
   "style": {"bottom": "calc(50% - 1.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Guardar",
   "feather": "Save",
   "hasText": True,
   "commands": ["save-state", ["response","saved"]],
   "response": "saved",
   "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Ejecutar",
   "feather": "Play",
   "primary": True,
   "hasText": True,
   "showWithIcon": True,
   "commands": ["submit"],
   "style": {"bottom": "0.44rem", "right": "0.4rem"}
 },
 {
   "name": "Comandos",
   "feather": "Terminal",
   "primary": True,
   "hasText": True,
   "commands": ["openCommandPallete"],
   "style": {"bottom": "3.5rem", "right": "0.4rem"}
 }
]

css_string = '''
background-color: #bee1e5;

body > #root .ace-streamlit-dark~& {
   background-color: #262830;
}

.ace-streamlit-dark~& span {
   color: #fff;
   opacity: 0.6;
}

span {
   color: #000;
   opacity: 0.5;
}

.code_editor-info.message {
   width: inherit;
   margin-right: 75px;
   order: 2;
   text-align: center;
   opacity: 0;
   transition: opacity 0.7s ease-out;
}

.code_editor-info.message.show {
   opacity: 0.6;
}

.ace-streamlit-dark~& .code_editor-info.message.show {
   opacity: 0.5;
}
'''
# create info bar dictionary
info_bar = {
  "name": "language info",
  "css": css_string,
  "style": {
            "order": "1",
            "display": "flex",
            "flexDirection": "row",
            "alignItems": "center",
            "width": "100%",
            "height": "2.5rem",
            "padding": "0rem 0.75rem",
            "borderRadius": "8px 8px 0px 0px",
            "zIndex": "9993"
           },
  "info": [{
            "name": "python",
            "style": {"width": "100px"}
           }]
}
# CSS string for Code Editor
css_string2 = '''
font-weight: 600;
&.streamlit_code-editor .ace-streamlit-dark.ace_editor {
  background-color: #111827;
  color: rgb(255, 255, 255);
}
&.streamlit_code-editor .ace-streamlit-light.ace_editor {
        background-color: #eeeeee;
        color: rgb(0, 0, 0);
}
'''
# style dict for Ace Editor
ace_style = {"borderRadius": "0px 0px 8px 8px"}

# style dict for Code Editor
code_style = {"width": "100%"}
editor0 = code_editor(code1,theme="contrast",buttons=bts,lang='python',height=[15, 30],focus=True,info=info_bar,props={"style": ace_style}, component_props={"style": code_style, "css": css_string2})


if editor0['type'] == "submit" and len(editor0['text']) != 0:
# Run the Python code and capture the output
    result = subprocess.run(['python', '-c', editor0['text']], capture_output=True, text=True)
    output = result.stdout
    error = result.stderr
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(output, error)

if editor0['type'] == "saved" and len(editor0['text']) != 0:
    filename = st.text_input('Ingrese el nombre del archivo sin la extension .py','example')
    st.download_button(
        label="Descargar",
        data=editor0['text'],
        file_name=filename+'.py',
        mime='text/python',)

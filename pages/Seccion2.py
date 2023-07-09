import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import base64
import struct
import math

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


st.title('2. Variables, declaraciones y expresiones')


txt0 = r'''
# 2.1. Valores y tipos de datos
<div style="text-align: justify;">
Un valor es una de las cosas fundamentales, como una palabra o un número, que manipula un programa. Algunos valores son
5 (el resultado cuando sumamos 2 + 3) y "¡Hola, mundo!". Estos objetos se clasifican en diferentes clases o tipos de
datos: 4 es un número entero y "¡Hola, mundo!" es una cadena, llamada así porque contiene una cadena o secuencia de
letras. Usted (y el intérprete) pueden identificar las cadenas porque están entre comillas.

Podemos especificar valores directamente en los programas que escribimos. Por ejemplo, podemos especificar un número
como literal simplemente escribiéndolo (literalmente) directamente en el programa (por ejemplo, 5 o 4.32).
En un programa, especificamos una palabra, o más generalmente una cadena de caracteres, encerrando los caracteres
entre comillas (por ejemplo, "¡Hola, mundo!").

Durante la ejecución de un programa, el intérprete de Python crea una representación interna de los literales que se
especifican en un programa. Luego puede manipularlos, por ejemplo, multiplicando dos números. A las representaciones
internas las llamamos objetos o simplemente valores.

No puede ver directamente las representaciones internas de los valores. Sin embargo, puede utilizar la función de
impresión para ver una representación impresa en la ventana de resultados.

La representación impresa de un número usa la representación decimal familiar (leer números romanos es un desafío
divertido en los museos, pero gracias a Dios que el intérprete de Python no presenta el número 2014 como MMXIV en
la ventana de salida). Por lo tanto, la representación impresa de un número que se muestra en la ventana de salida es
la misma que el literal que especifica en un programa.

Sin embargo, la representación impresa de una cadena de caracteres no es exactamente igual que el literal utilizado para
especificar la cadena en un programa. Para el literal en un programa, encierra la cadena entre comillas.
La representación impresa, en la ventana de resultados, omite las comillas.

</div>
'''
st.markdown(txt0, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
        print(3.2)
        print("Hello, World!")
    ''')
if st.button('Ejecutar',key='button20'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(3.2)
        st.write("Hello, World!")


with st.expander('Nota:'):
    st.markdown(unsafe_allow_html=True,body=r'''
    <div style="text-align: justify;">
    Los literales aparecen en los programas. El intérprete de Python convierte los literales en valores, que tienen
    representaciones internas que las personas nunca pueden ver directamente. Las salidas son representaciones
    externas de valores que aparecen en la ventana de salida. Cuando tengamos cuidado, usaremos los términos de
    esta manera. A veces, sin embargo, nos volveremos un poco descuidados y nos referiremos a literales o
    representaciones externas como valores.
    </div>
    ''')


txt1 = r'''
<div style="text-align: justify;">
Los números con punto decimal pertenecen a una clase llamada flotante, porque estos números se representan en un formato
llamado punto flotante. En esta etapa, puede tratar las palabras clase y escribir indistintamente. Volveremos a una
comprensión más profunda de lo que es una clase en capítulos posteriores.

Pronto encontrará también otros tipos de objetos, como listas y diccionarios. Cada uno de estos tiene su propia
representación especial para especificar un objeto como un literal en un programa y para mostrar un objeto cuando lo
imprime. Por ejemplo, el contenido de la lista está encerrado entre corchetes [ ]. También encontrará algunos objetos
más complicados que no tienen representaciones impresas muy agradables: imprimirlos no será muy útil.
</div>

# 2.3. Operadores y operandos

<div style="text-align: justify;">
Puede construir expresiones complejas a partir de otras más simples usando operadores. Los operadores son fichas
especiales que representan cálculos como la suma, la multiplicación y la división. Los valores sobre los que trabaja
el operador se denominan operandos.

Las siguientes son todas las expresiones legales de Python cuyo significado es más o menos claro:

    20 + 32
    5 ** 2
    (5 + 9) * (15 - 7)

Los tokens :red[+], :red[-] y :red[*], y el uso de paréntesis para agrupar, significan en Python lo que significan en matemáticas
. El asterisco (:red[*]) es la ficha de multiplicación y :red[**] es la ficha de exponenciación.
La suma, la resta, la multiplicación y la exponenciación hacen lo que esperas.

Recuerda que si queremos ver los resultados del cómputo, el programa necesita especificarlo con la palabra print.
Los primeros tres cálculos ocurren, pero sus resultados no se imprimen.
</div>
'''

st.markdown(txt1, unsafe_allow_html=True)

with st.expander(label="Implementación en Python"):
    st.code('''
        print(20 + 32)
        print(5 ** 2)
        print((5 + 9) * (15 - 7))
    ''')
if st.button('Ejecutar',key='button21'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(20 + 32)
        st.write(5 ** 2)
        st.write((5 + 9) * (15 - 7))
txt2 = r'''
En Python 3, que usaremos, el operador de división :red[/] produce un resultado de coma flotante (incluso si el resultado es
un número entero; 4:red[/]2 es 2.0). Si desea una división truncada, que ignora el resto, puede usar el operador :red[//] (por
ejemplo, 5:red[//]2 es 2).
'''
st.markdown(txt2, unsafe_allow_html=True)

with st.expander(label="Implementación en Python"):
    st.code('''
        print(9 / 5)
        print(5 / 9)
        print(9 // 5)
    ''')
if st.button('Ejecutar',key='button22'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(9 / 5)
        st.write(5 / 9)
        st.write(9 // 5)

txt3 = r'''
Preste especial atención a los ejemplos anteriores. Tenga en cuenta que 9//5 trunca en lugar de redondear,
por lo que produce el valor 1 en lugar de 2.
El operador de división truncada, //, también funciona en números de coma flotante. Se trunca al entero más cercano,
pero aún produce un resultado de coma flotante. Así 7.0 // 3.0 es 2.0.

'''
st.markdown(txt3, unsafe_allow_html=True)
with st.expander(label="Implementación en Python"):
    st.code('''
        print(7.0 / 3.0)
        print(7.0 // 3.0)

    ''')
if st.button('Ejecutar',key='button23'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(7.0 / 3.0)
        st.write(7.0 // 3.0)

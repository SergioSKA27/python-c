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


txt = r'''
<div style="text-align: justify;">

</div>
'''

st.title('Numpy')


txt0 = r'''
<div style="text-align: justify;">
Numpy es el paquete fundamental para la computación numérica con Python. Proporciona formas poderosas de crear,
almacenar y/o manipular datos, lo que le permite integrarse sin problemas y rápidamente con una amplia variedad de
bases de datos. Esta es también la base sobre la que se construye Pandas, que es un paquete centrado en datos de
alto rendimiento que aprenderemos más adelante en el curso.

En esta lección, hablaremos sobre la creación de arreglos con ciertos tipos de datos, la manipulación de arreglos,
la selección de elementos de arreglos y la carga de conjuntos de datos en arreglos. Tales funciones son útiles para
manipular datos y comprender las funcionalidades de otros paquetes de datos comunes de Python.
</div>
'''
st.markdown(txt0, unsafe_allow_html=True)

with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        #Recordará que importamos una biblioteca usando la palabra clave `import` ya que la abreviatura común de numpy es np
        import numpy as np
        import math
    ''')

txt1 = r'''
<div style="text-align: justify;">
Las matrices se muestran como una lista o lista de listas y también se pueden crear a través de la lista. Al crear un
matriz, pasamos una lista como argumento en la matriz numpy
</div>
'''
st.markdown(txt1, unsafe_allow_html=True)

with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        a = np.array([1, 2, 3])
        print(a)
    ''')
if st.button('Ejecutar',key='button0'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        a = np.array([1, 2, 3])
        st.write(a)

txt2 = r'''
<div style="text-align: justify;">
Podemos imprimir el número de dimensiones de una lista usando el atributo ndim
</div>
'''
st.markdown(txt2, unsafe_allow_html=True)

with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        a.ndim
    ''')
if st.button('Ejecutar',key='button1'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        a = np.array([1, 2, 3])
        st.write(a.ndim)


# If we pass in a list of lists in numpy array, we create a multi-dimensional array, for instance, a matrix

txt3 = r'''
<div style="text-align: justify;">
    Si pasamos una lista de listas en una matriz Numpy, creamos una matriz multidimensional, por ejemplo, una matriz
</div>
'''


with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        b = np.array([[1,2,3],[4,5,6]])
        print(b)
    ''')
if st.button('Ejecutar',key='button2'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        b = np.array([[1,2,3],[4,5,6]])
        st.write(b)

txt4 = r'''
<div style="text-align: justify;">
Podemos imprimir la longitud de cada dimensión llamando al atributo de forma, que devuelve una tupla
</div>
'''
st.markdown(txt4, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(b.shape)
    ''')
if st.button('Ejecutar',key='button3'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        b = np.array([[1,2,3],[4,5,6]])
        st.write(b.shape)




txt5 = r'''
<div style="text-align: justify;">
También podemos verificar el tipo de elementos en la matriz
</div>
'''
st.markdown(txt5, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(a.dtype)
    ''')
if st.button('Ejecutar',key='button4'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        a = np.array([1, 2, 3])
        st.write(a.dtype)



txt5 = r'''
<div style="text-align: justify;">
También podemos verificar el tipo de elementos en la matriz
</div>
'''
st.markdown(txt5, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(a.dtype)
    ''')
if st.button('Ejecutar',key='button5'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        a = np.array([1, 2, 3])
        st.write(a.dtype)






txt6 = r'''
<div style="text-align: justify;">
Además de enteros, los flotadores también se aceptan en matrices numpy
</div>
'''
st.markdown(txt6, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        c = np.array([2.2, 5, 1.1])
        print(c.dtype.name)
    ''')
if st.button('Ejecutar',key='button6'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        c = np.array([2.2, 5, 1.1])
        st.write(c.dtype.name)





txt7 = r'''
<div style="text-align: justify;">
Veamos los datos en nuestra matriz.
Tenga en cuenta que Numpy convierte automáticamente enteros, como 5, hasta flotantes, ya que no hay pérdida de prescisión.
Numpy intentará brindarle el mejor formato de tipo de datos posible para mantener sus tipos de datos homogéneos, que
significa que todos los datos son de la mismo tipo, en la matriz
</div>
'''
st.markdown(txt7, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(c)
    ''')
if st.button('Ejecutar',key='button7'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        c = np.array([2.2, 5.0, 1.1])
        st.write(str(c))







txt8 = r'''
<div style="text-align: justify;">
A veces sabemos la forma de una matriz que queremos crear, pero no lo que queremos ser.numpy
Ofrece varias funciones para crear matrices con marcadores de posición iniciales, como los de cero o uno.
Creemos dos matrices, ambas la misma forma pero con diferentes valores de relleno
</div>
'''
st.markdown(txt7, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        d = np.zeros((2,3))
        print(d)

        e = np.ones((2,3))
        print(e)
    ''')
if st.button('Ejecutar',key='button8'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        d = np.zeros((2,3))
        st.write(d)

        e = np.ones((2,3))
        st.write(e)


txt9 = r'''
<div style="text-align: justify;">
Verás zeros, ones, y rand utilizado con bastante frecuencia para crear matrices de ejemplo, especialmente en stack overflow
posts y otros foros.
También podemos generar una matriz con números aleatorios
</div>
'''



st.markdown(txt9, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        np.random.rand(2,3)
    ''')
if st.button('Ejecutar',key='button9'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(np.random.rand(2,3))




txt10 = r'''
<div style="text-align: justify;">
También podemos crear una secuencia de números en una matriz con la función arange(). El primer argumento es donde
Comenzar la secuencia, y el segundo argumento es el final de la secuencia, y el tercer argumento es la diferencia entre
cada número consecutivo

Creemos una matriz de cada número uniforme de diez (inclusivo) a cincuenta (exclusivo)
</div>
'''



st.markdown(txt10, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        f = np.arange(10, 50, 2)
        print(f)
    ''')
if st.button('Ejecutar',key='button10'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        f = np.arange(10, 50, 2)
        st.write(str(f))


txt11 = r'''
<div style="text-align: justify;">
Si queremos generar una secuencia de flotadores, podemos usar la función linspace (). En esta función el tercer
argumento no es la diferencia entre dos números, sino el número total de elementos que desea generar
</div>
'''



st.markdown(txt11, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        np.linspace( 0, 2, 15 ) # 15 números de 0 (inclusivo) a 2 (inclusive)
    ''')
if st.button('Ejecutar',key='button11'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(str(np.linspace( 0, 2, 15 )))




txt12 = r'''
# Operaciones con Arrays
<div style="text-align: justify;">
Podemos hacer muchas cosas con arrays, tales como manipulación matemática (adición, resta, cuadrado,
exponentes) así como usar arrays booleanos, que son valores binarios.También podemos hacer manipulación de matrices como
como producto, transposición, inversa, etc.
</div>
'''



st.markdown(txt12, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        # Operadores aritméticos en array se aplican a todos los elementos entrada a entrada.

        # Creemos un par de arrays
        a = np.array([10,20,30,40])
        b = np.array([1, 2, 3,4])

        # Ahora veamos a - b
        c = a-b
        print(c)

        # Y veamos a * b
        d = a*b
        print(d)
    ''')
if st.button('Ejecutar',key='button12'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        a = np.array([10,20,30,40])
        b = np.array([1, 2, 3,4])
        # Ahora veamos a - b
        c = a-b
        # Y veamos a * b
        d = a*b
        st.write(str(c))
        st.write(str(d))



txt13 = r'''
<div style="text-align: justify;">
Con la manipulación aritmética, podemos convertir los datos de corriente de forma que queremos que sea.Con numpy yo
podría convertir fácilmente una serie de valores de Farenheit, digamos el pronóstico del tiempo, a Celsius
</div>
'''



st.markdown(txt13, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        # Creemos una variedad de valores
        farenheit = np.array([0,-10,-5,-15,0])

        # Y la fórmula para la conversión es ((°F − 32) × 5/9 = °C)
        celcius = (farenheit - 32) * (5/9)
        print(celcius)
    ''')
if st.button('Ejecutar',key='button13'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        farenheit = np.array([0,-10,-5,-15,0])
        celcius = (farenheit - 32) * (5/9)
        st.write(celcius)



txt14 = r'''
<div style="text-align: justify;">
Otra manipulación útil e importante es el array booleano. Podemos aplicar un operador en un array, y un
array booleano será devuelto para cualquier elemento en el original, con verdadero emitido si cumple con la condición y falsa sino.
Por ejemplo, si queremos obtener una matriz booleana para verificar los títulos de Celcius que son mayores de -20 grados
Otra manipulación útil e importante es el array booleano.Es que podemos aplicar un operador en un array, y un
booleano  será devuelto para cualquier elemento en el original, con verdadero emitido si cumple con la condición y falsa oterana.
Por ejemplo, si queremos obtener un array booleano para verificar los títulos de Celcius que son mayores de -20 grados
</div>
'''



st.markdown(txt14, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(celcius > -20)
    ''')
if st.button('Ejecutar',key='button14'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        farenheit = np.array([0,-10,-5,-15,0])
        celcius = (farenheit - 32) * (5/9)
        st.write(str(celcius > -20))
        st.write((celcius > -20))



txt15 = r'''
<div style="text-align: justify;">
Aquí hay otro ejemplo, podríamos usar el operador del módulo para verificar los números en una matriz para ver si son uniformes.
Recuerde que el módulo hace división pero retorna la porción del residuo)
</div>
'''



st.markdown(txt15, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(celcius%2 == 0)
    ''')
if st.button('Ejecutar',key='button15'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        farenheit = np.array([0,-10,-5,-15,0])
        celcius = (farenheit - 32) * (5/9)
        st.write(str(celcius%2 == 0))
        st.write((celcius%2 == 0))





















































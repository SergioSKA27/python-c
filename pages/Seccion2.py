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
with st.expander(label="Implementación en Python",expanded=True):
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

with st.expander(label="Implementación en Python",expanded=True):
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
<div style="text-align: justify;">
En Python 3, que usaremos, el operador de división :red[/] produce un resultado de coma flotante (incluso si el resultado es
un número entero; 4 :red[/] 2 es 2.0). Si desea una división truncada, que ignora el resto, puede usar el operador :red[//] (por
ejemplo, 5 :red[//] 2 es 2).
</div>
'''
st.markdown(txt2, unsafe_allow_html=True)

with st.expander(label="Implementación en Python",expanded=True):
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
<div style="text-align: justify;">
Preste especial atención a los ejemplos anteriores. Tenga en cuenta que 9//5 trunca en lugar de redondear,
por lo que produce el valor 1 en lugar de 2.
El operador de división truncada, //, también funciona en números de coma flotante. Se trunca al entero más cercano,
pero aún produce un resultado de coma flotante. Así 7.0 // 3.0 es 2.0.
</div>
'''
st.markdown(txt3, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(7.0 / 3.0)
        print(7.0 // 3.0)

    ''')
if st.button('Ejecutar',key='button23'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(7.0 / 3.0)
        st.write(7.0 // 3.0)

txt4 = r'''
<div style="text-align: justify;">
El operador de módulo, a veces también llamado operador de resto u operador de resto entero, funciona con números
enteros (y expresiones enteras) y produce el resto cuando el primer operando se divide por el segundo.
En Python, el operador de módulo es un signo de porcentaje (:red[%]). La sintaxis es la misma que para otros operadores.
</div>
'''
st.markdown(txt4, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(7 // 3)    # This is the integer division operator
        print(7 % 3)     # This is the remainder or modulus operator
    ''')
if st.button('Ejecutar',key='button24'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(7 // 3)
        st.write(7 % 3)

txt5 = r'''
<div style="text-align: justify">
En el ejemplo anterior, 7 dividido por 3 es 2 cuando usamos la división de enteros y hay un resto de 1.

El operador de módulo resulta sorprendentemente útil. Por ejemplo, puede verificar si un número es divisible por otro:
si x % y es cero, entonces x es divisible por y. Además, puede extraer el dígito o dígitos más a la derecha de un
número. Por ejemplo, x % 10 produce el dígito más a la derecha de x (en base 10). De manera similar, x % 100 produce
los dos últimos dígitos.


</div>

# 2.4. Llamadas de función

<div style="text-align
El intérprete de Python puede calcular nuevos valores con llamadas a funciones. Estás familiarizado con la idea de las
funciones del álgebra de la escuela secundaria. Allí podría definir una función f especificando cómo transforma una
entrada en una salida, f(x) = 3x + 2. Luego, podría escribir f(5) y esperar obtener el valor 17.

Python adopta una sintaxis similar para invocar funciones. Si hay una función con nombre foo que toma una sola entrada,
podemos invocar foo en el valor 5 escribiendo foo(5).

Hay muchas funciones integradas disponibles en Python. Verá algunos en este capítulo y en los siguientes.
Las funciones son como fábricas que toman algún material, realizan alguna operación y luego envían el objeto resultante.
Icono que representa una función. Parece similar a una fábrica con tres lugares en la parte superior para que entren las
entradas y un lugar en la parte inferior para que salga el valor de salida/retorno.

En este caso, nos referimos a los materiales como argumentos o entradas y el objeto resultante se denomina salida o
valor de retorno. Este proceso de recibir información, hacer algo y luego devolver la salida
se muestra en el siguiente gif.
</div>
'''
st.markdown(txt5, unsafe_allow_html=True)
file0_ = open("pages/function_calls.gif", "rb")



contents0 = file0_.read()
data_url0 = base64.b64encode(contents0).decode("utf-8")
file0_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url0}" alt="func"></div>',
    unsafe_allow_html=True,
)

with st.expander('Nota:'):
    st.markdown(unsafe_allow_html=True,body=r'''
    <div style="text-align: justify;">
    No confunda el "valor de salida" de una función con la ventana de salida. La salida de una función es un valor de
    Python y nunca podemos ver realmente la representación interna de un valor. Pero podemos hacer dibujos que nos
    ayuden a imaginar qué valores son, o podemos imprimirlos para ver una representación externa en la
    ventana de resultados.

    Para confundir aún más las cosas, la impresión es en realidad una función. Todas las funciones producen valores
    de salida. Solo la función de impresión hace que las cosas aparezcan en la ventana de salida.
    </div>
    ''')
txt6 = r'''
<div style="text-align: justify;">
También es posible que los programadores definan nuevas funciones en sus programas. Aprenderá cómo hacerlo más adelante
en el curso. Por ahora, solo necesita aprender a invocar o llamar a una función y comprender que la ejecución de la
función devuelve un valor calculado.
</div>
'''
st.markdown(txt4, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        def square(x):
            return x * x

        def sub(x, y):
            return x - y
    ''')
def square(x):
    """
    The function "square" takes a number as input and returns the square of that number.

    :param x: The parameter "x" is a number that will be squared
    :return: The square of the input number.
    """
    return x * x

def sub(x, y):
    """
    The function sub(x, y) subtracts y from x and returns the result.

    :param x: The first parameter, x, is a number that represents the minuend in the subtraction operation
    :param y: The parameter "y" is the second number that will be subtracted from the first number "x"
    :return: the result of subtracting y from x.
    """
    return x - y

txt7 = r'''
<div style="text-align: justify;">
Hemos definido dos funciones arriba. La  función square toma un solo parámetro de entrada y devuelve esa entrada
multiplicada por sí misma. La función sub toma dos parámetros de entrada y devuelve el resultado de restar el segundo
del primero. Obviamente, estas funciones no son especialmente útiles, ya que tenemos disponibles los operadores
:red[*] y :red[-].
Pero ilustran cómo funcionan las funciones. La siguiente imagen ilustra cómo funciona la función square.
</div>
'''
st.markdown(txt7, unsafe_allow_html=True)
file1_ = open("pages/square_function.gif", "rb")



contents1 = file1_.read()
data_url1 = base64.b64encode(contents1).decode("utf-8")
file1_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url1}" alt="sqfunc"></div>',
    unsafe_allow_html=True,
)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(square(3))
        square(5)
        print(sub(6, 4))
        print(sub(5, 9))
    ''')
if st.button('Ejecutar',key='button25'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(square(3))
        st.write(square(5))
        st.write(sub(6, 4))
        st.write(sub(5, 9))

txt8 = r'''
<div style="text-align: justify;">
Tenga en cuenta que cuando una función toma más de un parámetro de entrada, las entradas están separadas por una coma.
También tenga en cuenta que el orden de las entradas es importante. El valor anterior a la coma se trata como la primera
entrada, el valor posterior como la segunda entrada.

Nuevamente, recuerde que cuando Python realiza cálculos, los resultados solo se muestran en la ventana de salida si hay
una declaración de impresión que dice que debe hacerlo. En la ventana de código activo anterior, el cuadrado (5) produce
el valor 25, pero nunca podemos verlo en la ventana de salida, porque no se imprime.
</div>

# 2.4.1. Llamadas a funciones como parte de expresiones complejas

<div style="text-align: justify;">
En cualquier parte de una expresión en la que pueda escribir un literal como un número, también puede escribir una
invocación de función que produzca un número.

Por ejemplo:
</div>
'''

st.markdown(txt8, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(square(3) + 2)
        print(sub(square(3), square(1+1)))
    ''')
if st.button('Ejecutar',key='button26'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(square(3) + 2)
        st.write(sub(square(3), square(1+1)))

txt9 = r'''
<div style="text-align: justify;">
Echemos un vistazo a cómo se desarrolla esa última ejecución.
Tenga en cuenta que siempre tenemos que resolver primero la expresión dentro de los paréntesis más internos, para
determinar qué entrada proporcionar al llamar a las funciones.
</div>

    print(sub(square(3), square(1+1)))

    print(sub(9, square(1+1)))

    print(sub(9, square(2)))

    print(sub(9, 4))

    print(5)

# 2.4.2. Las funciones son objetos; los paréntesis invocan funciones
<div style="text-align: justify;">
¿Recuerdas que antes mencionamos que algunos tipos de objetos de Python no tienen una buena representación impresa?
Las funciones son en sí mismas solo objetos. Si le dice a Python que imprima el objeto de función, en lugar de imprimir
los resultados de invocar el objeto de función, obtendrá una de esas representaciones impresas no tan agradables.

Simplemente escribir el nombre de la función se refiere a la función como un objeto. Escribir el nombre de la función
seguido de paréntesis () invoca la función.

'''
st.markdown(txt9, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(square)
        print(square(3))
    ''')
if st.button('Ejecutar',key='button27'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(square)
        st.write(square(3))

txt10 = r'''
# 2.5. Tipos de datos

Si no está seguro de en qué clase (tipo de datos) cae un valor, Python tiene una función llamada tipo que puede decírselo.
'''

st.markdown(txt10, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(type("Hello, World!"))
        print(type(17))
        print("Hello, World")
        print(type(3.2))

    ''')
if st.button('Ejecutar',key='button28'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(type("Hello, World!"))
        st.write(type(17))
        st.write("Hello, World")
        st.write(type(3.2))
txt11 = r'''
¿Qué pasa con valores como "17" y "3.2"? Parecen números, pero están entre comillas como cadenas.
'''

st.markdown(txt11, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(type("17"))
        print(type("3.2"))


    ''')
if st.button('Ejecutar',key='button29'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(type("17"))
        st.write(type("3.2"))


txt12 = r'''
¡Son cadenas!

Las cadenas en Python se pueden encerrar entre comillas simples (') o comillas dobles ("), o tres de cada una (\'\'\' o \"\"\")

<div style="textalign: justify;">
Las cadenas entre comillas dobles pueden contener comillas simples dentro de ellas, como en "La barba de Bruce", y las
cadenas entre comillas simples pueden tener comillas dobles dentro de ellas, como en "Los caballeros que dicen "¡Ni!"".
Las cadenas encerradas con tres apariciones de cualquiera de los símbolos de comillas se denominan cadenas entre
comillas triples. Pueden contener comillas simples o dobles:
'''
st.markdown(txt12, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(\'\'\'"Oh no", she exclaimed, "Ben's bike is broken!"\'\'\')


    ''')
if st.button('Ejecutar',key='button210'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write('''"Oh no", she exclaimed, "Ben's bike is broken!"''')

txt13 = r'''
Las cadenas entre comillas triples pueden incluso abarcar varias líneas:
'''
st.markdown(txt13, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print("\"\"This message will span
        several lines
        of the text."\"\")
    ''')
if st.button('Ejecutar',key='button211'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write("""This message will span\n
                    several lines\n
                    of the text.""")

txt14 = r'''
<div style="text-align: justify;">
A Python no le importa si usa comillas simples o dobles o las comillas de tres de un tipo para rodear sus cadenas.
Una vez que ha analizado el texto de su programa o comando, la forma en que almacena el valor es idéntica en todos
los casos, y las comillas que lo rodean no forman parte del valor.
</div>

# 2.6. Funciones de conversión de tipos

<div style="text-align: justify;">
A veces es necesario convertir valores de un tipo a otro. Python proporciona algunas funciones simples que nos
permitirán hacer eso. Las funciones int, float y str (intentarán) convertir sus argumentos en tipos int, float y str
respectivamente. Llamamos a estas funciones de conversión de tipos.

La función int puede tomar un número de punto flotante o una cadena y convertirlo en un int. Para los números de coma
flotante, descarta la parte decimal del número, un proceso que llamamos truncamiento hacia cero en la recta numérica.
Veamos esto en acción:
</div>
'''
st.markdown(txt14, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(3.14, int(3.14))
        print(3.9999, int(3.9999))       # This doesn't round to the closest int!
        print(3.0, int(3.0))
        print(-3.999, int(-3.999))        # Note that the result is closer to zero

        print("2345", int("2345"))        # parse a string to produce an int
        print(17, int(17))                # int even works on integers
        print(int("23bottles"))

    ''')
if st.button('Ejecutar',key='button212'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(3.14, int(3.14))
        st.write(3.9999, int(3.9999))
        st.write(3.0, int(3.0))
        st.write(-3.999, int(-3.999))

        st.write("2345", int("2345"))
        st.write(17, int(17))
        try:
            st.write(int("23bottles"))
        except Exception as e:
            st.error(str(e))

txt15 = r'''
<div style="text-align: justify;">
El último caso muestra que una cadena tiene que ser un número sintácticamente legal, de lo contrario obtendrá uno de
esos molestos errores de tiempo de ejecución. Modifique el ejemplo eliminando las botellas y vuelva a ejecutar el
programa. Deberías ver el número entero 23.

El convertidor de tipos float puede convertir un entero, un float o una cadena legal sintácticamente en un float.
</div>
'''

st.markdown(txt15, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(float("123.45"))
        print(type(float("123.45")))

    ''')
if st.button('Ejecutar',key='button213'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(float("123.45"))
        st.write(type(float("123.45")))
txt15 = r'''
<div style="text-align: justify;">
El convertidor de tipos str convierte su argumento en una cadena. Recuerde que cuando imprimimos una cadena,
las comillas se eliminan en la ventana de salida. Sin embargo, si imprimimos el tipo, podemos ver que definitivamente es str.
</div>
'''

st.markdown(txt15, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        print(str(17))
        print(str(123.45))
        print(type(str(123.45)))


    ''')
if st.button('Ejecutar',key='button214'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        st.write(str(17))
        st.write(str(123.45))
        st.write(type(str(123.45)))

txt16= r'''
<div style="text-align=justify;">
Una operación común en la que es posible que deba realizar una conversión de tipo es cuando está concatenando varias
cadenas pero desea incluir un valor numérico como parte de la cadena final. Debido a que no podemos concatenar una
cadena con un número entero o de coma flotante, a menudo tendremos que convertir números en cadenas antes de concatenarlos.
</div>
'''
st.markdown(txt16, unsafe_allow_html=True)
with st.expander(label="Implementación en Python",expanded=True):
    st.code('''
        value = 50 + 5
        print('The value is ' + value)   # Wrong
        print('The value is ' + str(value))   # Good

    ''')
if st.button('Ejecutar',key='button215'):
    with st.expander(label=":blue[Output: ]",expanded=True):
        value = 50 + 5
        try:
            st.write('The value is' + value)   # Wrong
        except Exception as e:
            st.error(str(e))
        st.write('The value is ' + str(value))   # Good


txt17 =r'''
# 2.7. Variables


<div style=text-align: justify;">
Una de las características más poderosas de un lenguaje de programación es la capacidad de manipular variables.
Una variable es un nombre que hace referencia a un valor.

Las sentencias de asignación crean nuevas variables y también les dan valores a los que referirse.

    mensaje = "What's up, Doc?"

    n = 17

    pi = 3.14159

Este ejemplo hace tres asignaciones. El primero asigna el valor de cadena "¿Qué pasa, Doc?" a una nueva variable llamada
mensaje. El segundo asigna el entero 17 a n, y el tercero asigna el número de punto flotante 3.14159 a una variable
llamada pi.

El token de asignación, :red[=], no debe confundirse con la igualdad (veremos más adelante que la igualdad usa el token :red[==]).
La declaración de asignación vincula un nombre, en el lado izquierdo del operador, con un valor, en el lado derecho.
Es por eso que obtendrá un error si ingresa:

    17 = n
</div>
'''
st.markdown(txt17, unsafe_allow_html=True)


with st.expander('Tip:'):
    st.markdown(unsafe_allow_html=True,body=r'''
    <div style="text-align: justify;">
    Al leer o escribir código, dígase a sí mismo "a n se le asigna 17" o "n obtiene el valor 17" o "n es
    una referencia al objeto 17" o "n se refiere al objeto 17". No digas "n es igual a 17".
    </div>
    ''')

txt18 = r'''
<div style="text-align: justify;">
Una forma común de representar variables en papel es escribir el nombre con una flecha que apunta al valor de la
variable. Este tipo de figura, conocida como diagrama de referencia, a menudo se denomina instantánea de estado porque
muestra en qué estado se encuentra cada una de las variables en un instante particular. (Piense en ello como el estado
mental de la variable). Este diagrama muestra el resultado de ejecutar las declaraciones
de asignación que se muestran arriba.
</div>
'''

st.markdown(unsafe_allow_html=True, body=txt18)

file2_ = open("pages/refdiagram1.png", "rb")



contents2 = file2_.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file2_.close()

st.markdown(
    f'<div style="text-align: center;"><img src="data:image/gif;base64,{data_url2}" alt="diag1"></div>',
    unsafe_allow_html=True,
)


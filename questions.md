1. Fundamentos de Python

¿Cuál es la diferencia entre una lista, tupla, conjunto y diccionario?

list: Colección ordenada y mutable. Permite elementos duplicados.

tuple: Colección ordenada e inmutable. Permite elementos duplicados.

set: Colección no ordenada y sin elementos duplicados.

dict: Colección de pares clave-valor. Mutable y sin claves duplicadas.

**¿Qué son los *args y kwargs?

*args: Recibe una cantidad variable de argumentos posicionales.

**kwargs: Recibe una cantidad variable de argumentos con nombre (clave-valor).

¿Qué hace una función lambda? ¿En qué casos la usas?

Es una función anónima de una sola línea. Se usa para funciones simples, especialmente como argumentos de map(), filter() o sorted().

¿Cuál es la diferencia entre is y ==?

==: Compara el valor.

is: Compara la identidad del objeto (si ocupan el mismo lugar en memoria).

¿Qué es una lista por comprensión y por qué es útil?

Sintaxis concisa para crear listas a partir de otras iterables. Es más legible y eficiente.

¿Qué significa que Python tenga tipado dinámico?

Las variables no tienen tipo fijo; el tipo se asigna en tiempo de ejecución según el valor.

🟠 2. Orientación a objetos (OOP)

Explica los principios de POO: herencia, encapsulamiento, polimorfismo.

Herencia: Una clase hija puede heredar atributos y métodos de una clase padre.

Encapsulamiento: Oculta detalles internos de una clase, exponiendo solo lo necesario.

Polimorfismo: Un método puede comportarse de forma distinta dependiendo del objeto que lo llama.

¿Para qué sirve super()?

Llama a métodos de la clase padre desde una clase hija, comúnmente usado en __init__().

¿Qué son los métodos mágicos (__init__, __str__, __repr__, __eq__)?

Son métodos especiales que personalizan el comportamiento de los objetos.

__init__: Constructor

__str__: Representación amigable

__repr__: Representación técnica

__eq__: Comparación de igualdad

¿Qué es la diferencia entre clase y objeto?

Clase: Molde o plantilla.

Objeto: Instancia de una clase.

🔹 3. Manejo de errores

¿Cómo manejas excepciones en Python?

Uso de bloques try/except. Se puede capturar errores específicos y manejar comportamientos.

¿Cuál es la diferencia entre try/except y try/finally?

except: Maneja la excepción.

finally: Siempre se ejecuta, haya error o no (para liberar recursos, cerrar archivos, etc).

¿Qué sucede si no capturas una excepción?

El programa lanza un error y se detiene.

🔸 4. Testing con Python

¿Cuál es la diferencia entre unittest y pytest?

unittest: Módulo nativo de Python, orientado a clases, verboso.

pytest: Framework externo, más conciso y flexible, mejor para proyectos modernos.

¿Qué son los fixtures en pytest?

Funciones especiales que proveen datos o configuración antes de ejecutar los tests.

¿Cómo haces mocking de una función externa?

Usando unittest.mock. Se reemplaza una función externa por una simulada para evitar dependencias.

¿Qué validas en una prueba unitaria?

Que una función específica produzca el resultado esperado dadas entradas controladas.

🟡 5. Automatización y pruebas QA

¿Cómo automatizarías la validación de una API REST?

Usar requests para enviar peticiones y validar status_code, headers y contenido de la respuesta.

¿Cómo pruebas un endpoint que requiere autenticación?

Enviando headers o tokens en la petición (como Authorization: Bearer token).

¿Qué tipos de pruebas automatizas con Python?

Pruebas unitarias, integración, funcionales (API), de regresión, y algunas UI (con Selenium o Playwright).

¿Qué pruebas negativas harías a una API?

Inputs vacíos, tipos de datos incorrectos, endpoints erróneos, sin autenticación.

⚙️ 6. Scripts útiles o experiencia real

¿Has escrito scripts para validar logs o procesar archivos?

Sí, usando Python para leer archivos .log o .txt, buscar patrones y generar reportes.

¿Has trabajado con JSON, CSV o Excel desde Python?

Sí, usando json, csv, y pandas para leer y procesar esos formatos.

¿Has integrado tus pruebas en un pipeline CI/CD?

Sí, integrando pytest con GitHub Actions, CodeBuild (AWS), o Jenkins para ejecutar pruebas automáticas.

⚡ 7. Conceptuales / soft + prácticas

¿Cuál fue el mayor bug que detectaste con un test en Python?

Ejemplo ideal: una regresión donde una API aceptaba valores duplicados y el test lo detectó tras una actualización.

¿Cómo organizas un framework de automatización?

Estructura de carpetas clara, uso de pytest o behave, configuración externa (JSON/YAML), y reportes.

¿Cómo investigas una prueba que falla de forma intermitente?

Reviso logs, tiempos de respuesta, dependencias externas, y ejecuto varias veces con --reruns (pytest) para aislar causas.


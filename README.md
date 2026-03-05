# # Prueba Técnica – Python, JavaScript y GitHub (Examen 4)

---

## Instrucciones Generales

1. Crea un **repositorio nuevo en GitHub** con el nombre:
   `technical-test-python-js-exam-4`
2. Todo el código debe subirse a ese repositorio.
3. Cada ejercicio debe ir en su propio archivo.
4. Usa commits claros y bien nombrados.
5. Al final, abre un **Pull Request** al repositorio que se te proporcionará.
6. Entrega la **URL del repositorio** y del **PR**.

---

## Bloque 1 – GitHub (Ejercicio práctico)

### Ejercicio 1: Flujo de trabajo obligatorio

Debes demostrar que sabes manejar un flujo de trabajo real en GitHub.

Pasos obligatorios:
1. Crea el repositorio.
2. Crea una rama llamada `development`.
3. En esa rama, haz al menos **3 commits**.
4. Haz un **squash** de esos commits en uno solo.
5. Renombra el commit final a: `Initial solution`.
6. Abre un Pull Request desde `development` a `main`.

El repositorio debe reflejar claramente este historial.

---

## Notas del desarrollo

- Iniciando el desarrollo en la rama development.

## Bloque 2 – Python (máx. 2 ejercicios)

### Ejercicio 2: Agrupación con lógica

Dado un listado de eventos:

```python
events = [
    {"type": "click", "user": "a"},
    {"type": "scroll", "user": "b"},
    {"type": "click", "user": "a"},
    {"type": "hover", "user": "c"},
    {"type": "click", "user": "b"},
]
```

Escribe una función que devuelva un diccionario con el número de eventos por usuario.

Resultado esperado:
```python
{
    "a": 2,
    "b": 2,
    "c": 1
}
```

No uses librerías externas.

---

### Ejercicio 3: Validación avanzada

Escribe una función que valide contraseñas con las siguientes reglas:
- Mínimo 10 caracteres
- Al menos una mayúscula
- Al menos un número
- No puede contener espacios

La función debe devolver `True` o `False`.

---

## Bloque 3 – JavaScript (máx. 2 ejercicios)

### Ejercicio 4: Transformación de datos

Dado este array:

```js
const orders = [
  { id: 1, total: 50, paid: true },
  { id: 2, total: 30, paid: false },
  { id: 3, total: 70, paid: true },
];
```

Devuelve:
- El total acumulado **solo de los pedidos pagados**
- Un array con los `id` de los pedidos no pagados

No modifiques el array original.

---

### Ejercicio 5: Control de estado

Implementa una función que simule un sistema de encendido/apagado.

Ejemplo:
```js
toggle("on")  // off
toggle("off") // on
```

Debe funcionar correctamente incluso si se llama muchas veces seguidas.

---

## Reto Final (Opcional)

Puedes hacerlo en **Python o JavaScript**.

### Reto: Motor de reglas

Implementa un pequeño motor de reglas que:
- Reciba una lista de reglas (condiciones + acción)
- Evalúe un objeto de entrada
- Ejecute solo las acciones cuyas reglas se cumplan

Ejemplo de regla:
```json
{
  "if": { "role": "admin", "active": true },
  "then": "ALLOW_ACCESS"
}
```

Ejemplo de entrada:
```json
{ "role": "admin", "active": true }
```

Salida esperada:
```json
["ALLOW_ACCESS"]
```

Puntos extra si:
- Permites múltiples condiciones
- Manejas errores
- El código es extensible

---

## Entrega

- URL del repositorio
- URL del Pull Request

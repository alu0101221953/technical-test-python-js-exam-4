def contar_eventos_por_usuario(events):
    resultado = {}
    for ev in events:
        usuario = ev["user"]
        resultado[usuario] = resultado.get(usuario, 0) + 1
    return resultado

events = [
    {"type": "click", "user": "a"},
    {"type": "scroll", "user": "b"},
    {"type": "click", "user": "a"},
    {"type": "hover", "user": "c"},
    {"type": "click", "user": "b"},
]

print(contar_eventos_por_usuario(events))
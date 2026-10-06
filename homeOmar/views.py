DATOS_PELICULAS = {
    'accion': {
        'titulo': 'Acción y Suspenso (Omar)',
        'descripcion': 'Películas llenas de adrenalina y persecuciones.',
        'peliculas': [
            # Fíjate que ahora solo dice 'images/...'
            {'nombre': 'John Wick 4', 'edad': '+16', 'imagen': 'images/accion1.jpg'},
            {'nombre': 'Mad Max', 'edad': '+18', 'imagen': 'images/accion2.jpg'},
        ]
    },
    # ... resto del código ...
}

def index(request):
    # Si tu archivo index.html está suelto dentro de la carpeta templates global:
    return render(request, 'index.html', {'generos': DATOS_PELICULAS})

def detalle_genero(request, genero_id):
    genero_seleccionado = DATOS_PELICULAS.get(genero_id)
    # Si tu archivo detalle.html está suelto dentro de la carpeta templates global:
    return render(request, 'detalle.html', {'genero': genero_seleccionado})
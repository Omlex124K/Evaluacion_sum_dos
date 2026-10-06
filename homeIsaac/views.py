from django.shortcuts import render

def index(request):
    generos = {
        'terror': {
            'titulo': 'Terror y Misterio (Isaac)',
            'descripcion': 'Historias oscuras que pondrán a prueba tus nervios.',
            'peliculas': [
                {'nombre': 'El Conjuro', 'edad': '+14', 'imagen': 'homeIsaac/images/terror1.jpg'},
                {'nombre': 'It', 'edad': '+16', 'imagen': 'homeIsaac/images/terror2.jpg'},
            ]
        },
        'animacion': {
            'titulo': 'Animación',
            'descripcion': 'Grandes historias animadas para disfrutar.',
            'peliculas': [
                {'nombre': 'Spider-Man: Across the Spider-Verse', 'edad': 'Todo Espectador', 'imagen': 'homeIsaac/images/animacion1.jpg'},
                {'nombre': 'El Viaje de Chihiro', 'edad': 'Todo Espectador', 'imagen': 'homeIsaac/images/animacion2.jpg'},
            ]
        }
    }
    return render(request, 'homeIsaac/index.html', {'generos': generos})
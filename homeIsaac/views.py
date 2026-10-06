from django.shortcuts import render

def index(request):
    generos = {
        'terror': {
            'titulo': 'Terror y Misterio (Isaac)',
            'descripcion': 'Historias oscuras que pondrán a prueba tus nervios.',
            'peliculas': [
                {'nombre': 'El Conjuro', 'edad': '+14', 'imagen': 'images/terror1.jpg'},
                {'nombre': 'It', 'edad': '+16', 'imagen': 'images/terror2.jpg'},
            ]
        },
        'animacion': {
            'titulo': 'Animación (Isaac)',
            'descripcion': 'Grandes historias animadas para disfrutar.',
            'peliculas': [
                {'nombre': 'Spider-Man: Across the Spider-Verse', 'edad': 'TE', 'imagen': 'images/animacion1.jpg'},
                {'nombre': 'El Viaje de Chihiro', 'edad': 'TE', 'imagen': 'images/animacion2.jpg'},
            ]
        }
    }
    # Apunta al MISMO index global
    return render(request, 'index.html', {'generos': generos})
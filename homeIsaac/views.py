from django.shortcuts import render

def index(request):
    generos = {
        'terror': {
            'titulo': 'Terror y Misterio (Isaac)',
            'descripcion': 'Historias oscuras que pondrán a prueba tus nervios.',
            'peliculas': [
                {'nombre': 'El Conjuro', 'edad': '+14', 'imagen': 'images/ELConjuro.jpg'},
                {'nombre': 'It', 'edad': '+16', 'imagen': 'images/IT.jpg'},
            ]
        },
        'animacion': {
            'titulo': 'Animación (Isaac)',
            'descripcion': 'Grandes historias animadas para disfrutar.',
            'peliculas': [
                {'nombre': 'Spider-Man: Across the Spider-Verse', 'edad': 'TE', 'imagen': 'images/Spider_man.jpg'},
                {'nombre': 'El Viaje de Chihiro', 'edad': 'TE', 'imagen': 'images/ElViaje.jpg'},
            ]
        }
    }
    # Apunta al MISMO index global
    return render(request, 'index.html', {'generos': generos})
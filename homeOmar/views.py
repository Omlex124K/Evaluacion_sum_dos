from django.shortcuts import render

def index(request):
    generos = {
        'accion': {
            'titulo': 'Acción y Suspenso (Omar)',
            'descripcion': 'Películas llenas de adrenalina y persecuciones.',
            'peliculas': [
                {'nombre': 'John Wick 4', 'edad': '+16', 'imagen': 'images/JhonWik.jpg'},
                {'nombre': 'Mad Max', 'edad': '+18', 'imagen': 'images/MadMax.jpg'},
            ]
        },
        'scifi': {
            'titulo': 'Ciencia Ficción (Omar)',
            'descripcion': 'Explora universos paralelos y futuros lejanos.',
            'peliculas': [
                {'nombre': 'Interstellar', 'edad': '+13', 'imagen': 'images/Interestelar.jpg'},
                {'nombre': 'Matrix', 'edad': '+16', 'imagen': 'images/Matrix.jpg'},
            ]
        }
    }
    # Apunta al index global
    return render(request, 'index.html', {'generos': generos})
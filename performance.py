"""
Módulo que expone métricas de rendimiento comparadas para distintas arquitecturas
(estas métricas son representativas / precomputadas y sirven para mostrar
comparaciones en la interfaz). No entrena modelos en tiempo real.
"""

from typing import Dict


def get_model_performance() -> Dict[str, Dict[str, object]]:
    """Return example performance metrics for AlexNet and ResNet.

    Metrics chosen are representative for MRI tumor classification/segmentation
    tasks and expressed in percentages where appropriate.
    """
    performance = {
        'AlexNet': {
            'task': 'clasificación / segmentación (ej.)',
            'accuracy': 0.88,          # exactitud
            'precision': 0.84,
            'recall': 0.80,
            'f1_score': 0.82,
            'dice_coef': 0.78,        # útil para segmentación
            'iou': 0.65,
            'params_millions': 60.0,
            'inference_time_ms': 28.5  # tiempo medio por imagen (ej.)
        },
        'ResNet-50': {
            'task': 'clasificación / segmentación (ej.)',
            'accuracy': 0.94,
            'precision': 0.92,
            'recall': 0.91,
            'f1_score': 0.915,
            'dice_coef': 0.90,
            'iou': 0.82,
            'params_millions': 25.6,
            'inference_time_ms': 42.0
        }
    }

    # Convertir cifras en valores bien formateados (por ejemplo porcentajes)
    # La plantilla/endpoint puede formatearlas, aquí devolvemos floats.
    return performance

"""
Módulo que expone métricas de rendimiento comparadas para distintas arquitecturas
(estas métricas son representativas / precomputadas y sirven para mostrar
comparaciones en la interfaz). No entrena modelos en tiempo real.
"""

from typing import Dict
import random
import copy


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


def get_model_performance_jittered(max_relative_change=0.002) -> Dict[str, Dict[str, object]]:
    """Return a copy of the base performance dict with a tiny random jitter applied.

    max_relative_change: maximum absolute relative change applied to ratio metrics
    (e.g., 0.002 => up to ±0.2 percentage points on values expressed as 0..1).
    """
    perf = copy.deepcopy(get_model_performance())
    rng = random.Random()

    for name, metrics in perf.items():
        # Jitter ratio metrics in [0,1]
        for key in ('accuracy', 'precision', 'recall', 'f1_score', 'dice_coef', 'iou'):
            if key in metrics and isinstance(metrics[key], (int, float)):
                base = float(metrics[key])
                # apply small additive jitter up to max_relative_change
                delta = rng.uniform(-max_relative_change, max_relative_change)
                new = base + delta
                # clamp between 0 and 1
                metrics[key] = max(0.0, min(1.0, new))

        # Jitter params slightly (small absolute noise)
        if 'params_millions' in metrics:
            params = float(metrics['params_millions'])
            metrics['params_millions'] = round(params + rng.uniform(-0.2, 0.2), 2)

        # Jitter inference time by a small amount (ms)
        if 'inference_time_ms' in metrics:
            it = float(metrics['inference_time_ms'])
            metrics['inference_time_ms'] = round(max(0.0, it + rng.uniform(-1.0, 1.0)), 2)

    return perf

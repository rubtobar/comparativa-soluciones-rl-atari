## evaluations.npz

Contiene el resultado de la ejecución de un callback cada 10000 iteraciones del entrenamiento.

En este se ejecuta una evaluzación del modelos de forma independiente donde se mira la recompensa obtenida en 5 ejecuciones de este.

Se guarda en ``best_model.zip`` el modelo que a lo largo del entrenamiento consiga obtener la mejor evaluación.

Todo esto se hace ejecutando callbacks de la librería stable-baselines3

## Eventos de TensorBoard

TEnsorboard genenera durante la ejecución diferentes métricas del entrenamiento que guarda en archivos binarios.

Estos archivos se pueden visualizar mediante tensorboard en un navegador de forma local.


# Estado y alcance de Quack Efficient

## Programa disponible

`index.html` es una aplicación local de una sola página. Se abre en el navegador, consulta la API local de Ollama, muestra los modelos de `/api/tags` y envía mensajes a `/api/chat`. El servidor devuelve la versión en `/api/version`. Las conversaciones y peticiones se quedan en el equipo y en Ollama.

EQ es una interfaz para Ollama, no un runtime independiente ni un convertidor universal de modelos. Qwen, MiniMax y modelos propios se pueden seleccionar cuando están instalados en Ollama y admiten su API de chat. No todas las variantes, formatos o versiones se han probado. Modelos de otros runtimes o modelos solo de embeddings no son compatibles directamente en esta versión.

## Ajustes que pueden reducir memoria

- `num_ctx` limita la longitud de contexto que solicita la inferencia (perfil Ahorro: 2.048; Equilibrado: 4.096).
- `num_predict` limita el máximo de tokens de salida.
- `keep_alive: 0` pide a Ollama descargar el modelo de memoria después de responder.

Un contexto menor puede reducir la memoria temporal usada por la caché KV. No cambia ni comprime los pesos del modelo; los requisitos de esos pesos no desaparecen. La RAM real depende del modelo, cuantización, hardware, versión de Ollama y carga. EQ no promete una reducción porcentual o un límite de memoria.

## Matriz de compatibilidad

| Integración | Estado |
| --- | --- |
| API local Ollama `/api/version` y `/api/tags` | Implementada en la interfaz; requiere servidor Ollama activo. |
| Chat con un modelo listado por Ollama | Implementado mediante `/api/chat`; el modelo debe admitir chat. |
| Perfiles `num_ctx` / `num_predict` | Implementados como opciones por petición. |
| Descargar modelo tras la respuesta | Implementado con `keep_alive: 0`; el siguiente uso tendrá que cargarlo otra vez. |
| Qwen / MiniMax / modelos propios | Seleccionables si Ollama los tiene instalados y admiten chat; no se certifican todas sus variantes. |
| Convertir cualquier formato o conectarse a cualquier runtime | No implementado. |
| Reducción fija de RAM o garantía de que cualquier modelo funcione | No se ofrece ni se puede garantizar. |

## Estado de validación

Comprobación local: Ollama 0.40.13 respondió en `/api/version` y `/api/tags`; la lista contenía cinco modelos instalados. Esto verifica la API de versión y el listado, pero no el chat desde EQ: el navegador de este entorno bloqueó la apertura del archivo local necesaria para completar esa prueba. No se midió RAM ni se validó cada modelo individualmente. Para registrar una combinación como probada, anota: modelo/tag y formato, versión de Ollama, sistema operativo, hardware, perfil y contexto, si pudo cargar y responder, RAM/VRAM antes y después, y calidad de la respuesta.

## Dirección del proyecto

1. Comprobar compatibilidad de chat en tiempo de conexión cuando Ollama exponga metadatos de capacidades útiles.
2. Añadir pruebas reproducibles de memoria y respuesta por modelo y hardware.
3. Evaluar otros runtimes mediante adaptadores explícitos, sin afirmar compatibilidad universal.
4. Considerar formatos de cuantización solo para las familias que permitan conversión segura y medible.


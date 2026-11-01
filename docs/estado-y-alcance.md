# Estado y alcance

## Lo que incluye esta versión

El starter contiene un paquete Python instalable y una CLI mínima:

- `eq info` presenta la versión, el sistema operativo y el estado experimental.
- `eq check --runtime ollama` y `eq check --runtime generic` explican que no hay adaptadores disponibles. El comando termina con código 2.

La comprobación no se conecta a un runtime. No se incluyen pesos, modelos, benchmarks ni servicios externos.

## Compatibilidad de modelos

**No hay ningún modelo validado ni compatible a través de EQ en esta versión**, porque todavía no existe un adaptador de inferencia. Esto no determina si un modelo funciona con Ollama, otro runtime o su aplicación original.

| Familia o runtime | Integración en EQ | Estado |
| --- | --- | --- |
| Texto / LLM | No implementada | Sin modelos probados |
| Imagen | No implementada | Sin modelos probados |
| Vídeo | No implementada | Sin modelos probados |
| Ollama | No implementada | El comando `eq check` no se conecta a Ollama |
| Genérico | No implementada | El comando `eq check` solo muestra un diagnóstico |

La tabla no afirma que un modelo sea incompatible: indica que EQ aún no puede evaluarlo. Para registrar una comprobación futura hacen falta el identificador y versión del modelo, formato, runtime y versión, sistema operativo, hardware y resultados de carga, generación, memoria, velocidad y calidad.

## Lo que aún no hace

EQ no modifica pesos, no cuantiza modelos, no optimiza la caché KV, no reduce por sí solo el uso de memoria y no garantiza un límite de 3 GB. Tampoco garantiza compatibilidad o una mejora de calidad, latencia o rendimiento con ningún modelo o sistema.

Los nombres `inspect`, `benchmark` y `optimize` describen posibles comandos futuros; no existen en esta versión.

## Dirección prevista

1. Definir una interfaz estable para adaptadores y detección de capacidades.
2. Añadir una integración concreta con un runtime y documentar sus versiones compatibles.
3. Crear benchmarks repetibles para memoria máxima, latencia, rendimiento y calidad.
4. Añadir perfiles que expongan claramente sus compromisos entre recursos y calidad.
5. Ampliar a otras familias de modelos y sistemas operativos tras validar cada combinación.

Cada paso requiere implementación y resultados antes de anunciarse como función disponible.

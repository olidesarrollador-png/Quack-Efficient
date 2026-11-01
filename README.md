# Quack Efficient (EQ)

**Efficient Quack Labs AI · toolkit experimental para explorar la eficiencia de inferencia.**

![Vista conceptual de Quack Efficient](assets/eq-overview.svg)

> **Estado actual:** EQ es un starter de diagnóstico. Todavía no comprime modelos ni acelera inferencias. No promete reducir la RAM, funcionar con cualquier modelo ni ofrecer compatibilidad con Ollama. Consulta [qué funciona hoy](docs/estado-y-alcance.md) antes de usarlo.

## ¿Qué es EQ?

Quack Efficient (EQ) es la base de un proyecto que busca ayudar a medir y, más adelante, reducir el coste de ejecutar modelos de IA. La idea es añadir integraciones específicas para cada motor y formato, perfiles que equilibren memoria, velocidad y calidad, y pruebas reproducibles.

Cada modelo y runtime tiene capacidades distintas. Por eso EQ está planteado como un conjunto de adaptadores comprobables, no como un optimizador universal. El starter incluido solo ofrece dos comandos informativos: `eq info` y `eq check`.

## Requisitos

- Python 3.10 o posterior.
- Windows, macOS o Linux.
- Git es opcional si descargas el ZIP en vez de clonar el repositorio.
- No hace falta instalar Ollama ni descargar modelos para probar el starter.

## Instalación paso a paso

### 1. Obtén el proyecto

Con Git:

```bash
git clone https://github.com/olidesarrollador-png/Quack-Efficient.git
cd Quack-Efficient
```

También puedes pulsar **Code → Download ZIP** en GitHub y extraerlo. Abre una terminal dentro de la carpeta extraída.

### 2. Crea un entorno virtual

```bash
python -m venv .venv
```

### 3. Activa el entorno

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, puedes usar directamente `.venv\Scripts\python.exe -m pip ...` y `.venv\Scripts\eq.exe ...`, o abrir una terminal CMD y ejecutar `.venv\Scripts\activate.bat`.

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Instala EQ en modo desarrollo

```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

### 5. Comprueba la instalación

```bash
eq info
eq check --runtime generic
```

`eq info` muestra versión y plataforma. `eq check` devuelve código de salida `2` y avisa de que no hay adaptadores; ese resultado es lo esperado en este starter. No indica que tu equipo o modelo tenga un problema.

Para ver las opciones disponibles:

```bash
eq --help
```

## Qué hace cada comando

| Comando | Resultado |
| --- | --- |
| `eq info` | Muestra la versión, el sistema operativo y que solo es un scaffold. |
| `eq check --runtime ollama` | Informa que no hay adaptador; no consulta Ollama. |
| `eq check --runtime generic` | Informa que no hay adaptador genérico. |

No existen todavía comandos `inspect`, `benchmark` ni `optimize`. Los ejemplos de esos comandos son ideas para el futuro, no funciones disponibles.

## Cómo está organizado

- `src/eq/cli.py`: interfaz de línea de comandos actual.
- `src/eq/__init__.py`: versión del paquete.
- `pyproject.toml`: metadatos e instalación del paquete Python.
- `docs/estado-y-alcance.md`: capacidades, límites y dirección del proyecto.
- `assets/eq-overview.svg`: ilustración conceptual de la experiencia prevista.

## Dirección del proyecto

La arquitectura prevista contempla un núcleo común, adaptadores separados por runtime/modelo, perfiles configurables y benchmarks que comparen memoria, latencia, velocidad y calidad. Las metas de plataforma son Windows, macOS y Linux. La compatibilidad con cada combinación se añadirá solo después de implementarla y probarla.

La hoja de ruta y el estado comprobable están en [docs/estado-y-alcance.md](docs/estado-y-alcance.md).

## Desarrollo y contribuciones

1. Crea y activa un entorno virtual siguiendo los pasos anteriores.
2. Instala el paquete con `python -m pip install -e .`.
3. Mantén las afirmaciones sobre rendimiento ligadas a mediciones reproducibles.
4. Conserva las licencias y avisos de modelos y dependencias de terceros.
5. No envíes modelos, prompts ni datos privados de usuarios sin su consentimiento explícito.
6. Documenta las regresiones de calidad junto con cualquier mejora de memoria o velocidad.

Antes de proponer compatibilidad con un runtime, indica versión, plataforma, modelo y pasos para reproducir los resultados.

## Licencia y uso

Este starter no incluye una licencia de software revisada. El archivo de política incluido en el ZIP era un borrador con un correo de contacto sin completar; por eso no se publica como licencia válida. Hasta que el titular del proyecto elija y añada una licencia, no se debe asumir permiso para redistribuir o usar el código con fines comerciales. Las condiciones de modelos, runtimes y dependencias de terceros se aplican por separado.

## Atribución

Quack Efficient (EQ) — Efficient Quack Labs AI. Concepto y atribución original: Quack Labs.

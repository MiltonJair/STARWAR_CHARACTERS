# Guía de Inicio Rápido

Esta guía te ayudará a comenzar a usar el proyecto SWAPI ETL en minutos.

## ⚡ Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/MiltonJair/STARWAR_CHARACTERS.git
cd STARWAR_CHARACTERS

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el ETL
python -m src.main
```

## 📊 ¿Qué hace el script?

El script automáticamente:
1. ✅ Descarga datos de 6 categorías de SWAPI
2. ✅ Transforma y enriquece la información
3. ✅ Guarda todo en el directorio `data/`

## 📁 Archivos Generados

Después de ejecutar, encontrarás en `data/`:

**Dataset Principal:**
- `swapi_people_dataset.csv` - Información completa y enriquecida de personajes

**Datos por Categoría (CSV y JSON):**
- `swapi_films.*` - Películas
- `swapi_people.*` - Personajes
- `swapi_planets.*` - Planetas
- `swapi_species.*` - Especies
- `swapi_starships.*` - Naves espaciales
- `swapi_vehicles.*` - Vehículos

## 💡 Uso Básico

### Importar módulos individuales

```python
# Usar el cliente de API
from src.api_client import get_all_swapi_data

films = get_all_swapi_data('films')
print(f"Encontradas {len(films)} películas")
```

```python
# Usar transformaciones
from src.transformers import segment_weight, segment_gender

peso_categoria = segment_weight(75)  # '71-80 kg'
genero = segment_gender('male')      # 'Male'
```

```python
# Exportar datos
from src.exporters import save_dataframe_as_csv
import pandas as pd

df = pd.DataFrame([{'nombre': 'Luke', 'edad': 19}])
save_dataframe_as_csv(df, 'mi_datos.csv')
```

## 🔧 Configuración

Puedes modificar la configuración en `src/config.py`:

```python
# Cambiar endpoint de API
SWAPI_ENDPOINT = 'https://swapi.py4e.com/api/'

# Modificar rangos de peso
WEIGHT_SEGMENTS = [
    (15, 35, '15-35 kg'),
    # ... añade más rangos
]
```

## 📚 Más Información

- **Documentación completa**: Ver [README.md](README.md)
- **Arquitectura del proyecto**: Ver [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- **Contribuir**: Ver [CONTRIBUTING.md](CONTRIBUTING.md)
- **Historial de cambios**: Ver [CHANGELOG.md](CHANGELOG.md)

## ⏱️ Tiempo de Ejecución

El proceso completo toma aproximadamente:
- **Películas**: ~5 segundos
- **Personajes**: ~2-3 minutos (incluye transformaciones)
- **Otras categorías**: ~30 segundos cada una

Total estimado: **5-10 minutos**

## 🆘 Problemas Comunes

### Error: "ModuleNotFoundError: No module named 'pandas'"
**Solución:** Instala las dependencias
```bash
pip install -r requirements.txt
```

### Error: "ConnectionError" o timeout
**Solución:** Verifica tu conexión a internet y que SWAPI esté disponible

### Los datos no aparecen en `data/`
**Solución:** El directorio se crea automáticamente. Si no existe, créalo:
```bash
mkdir data
```

## 🎯 Próximos Pasos

Una vez que tengas los datos:
1. Abre `swapi_people_dataset.csv` en Excel o tu herramienta favorita
2. Explora las transformaciones añadidas (edad, segmentaciones, etc.)
3. Crea visualizaciones y análisis
4. ¡Comparte tus descubrimientos!

---

**¿Listo?** ¡Ejecuta `python -m src.main` y comienza tu análisis! 🚀

# Star Wars Characters - SWAPI ETL

Este repositorio contiene una herramienta ETL (Extract, Transform, Load) para extraer y analizar datos de personajes de Star Wars utilizando la API pública SWAPI (Star Wars API).

## 📋 Descripción

Este proyecto extrae datos completos de Star Wars desde SWAPI, los transforma para añadir información enriquecida y los exporta en formatos CSV y JSON para análisis posterior. El objetivo es descubrir insights interesantes que puedan atraer a nuevos espectadores a la saga.

## 🚀 Características

- Extracción completa de datos de 6 categorías de SWAPI:
  - Películas (Films)
  - Personajes (People)
  - Planetas (Planets)
  - Especies (Species)
  - Naves espaciales (Starships)
  - Vehículos (Vehicles)

- Transformaciones avanzadas de datos:
  - Cálculo de edad de personajes en la primera película
  - Conversión de URLs a nombres legibles
  - Segmentación por género y peso
  - Métricas derivadas (número de películas, vehículos, etc.)

- Exportación dual en CSV y JSON para máxima compatibilidad

## 📁 Estructura del Proyecto

```
STARWAR_CHARACTERS/
├── src/                    # Código fuente
│   ├── __init__.py        # Inicialización del paquete
│   ├── config.py          # Constantes y configuración
│   ├── api_client.py      # Cliente de la API SWAPI
│   ├── transformers.py    # Funciones de transformación de datos
│   ├── exporters.py       # Funciones de exportación de datos
│   └── main.py            # Punto de entrada principal
├── data/                   # Datos generados (CSV/JSON)
├── docs/                   # Documentación adicional
├── requirements.txt        # Dependencias del proyecto
├── .gitignore             # Archivos ignorados por Git
└── README.md              # Este archivo
```

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/MiltonJair/STARWAR_CHARACTERS.git
cd STARWAR_CHARACTERS
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

Ejecuta el script principal para iniciar el proceso ETL:

```bash
python -m src.main
```

El script:
1. Extraerá datos de todas las categorías de SWAPI
2. Transformará los datos añadiendo información enriquecida
3. Guardará los resultados en el directorio `data/`

### Salida Generada

El proceso genera los siguientes archivos en `data/`:

- `swapi_people_dataset.csv` - Dataset completo de personajes con todas las transformaciones
- `swapi_films.csv` / `swapi_films.json` - Datos de películas
- `swapi_people.csv` / `swapi_people.json` - Datos de personajes
- `swapi_planets.csv` / `swapi_planets.json` - Datos de planetas
- `swapi_species.csv` / `swapi_species.json` - Datos de especies
- `swapi_starships.csv` / `swapi_starships.json` - Datos de naves
- `swapi_vehicles.csv` / `swapi_vehicles.json` - Datos de vehículos

## 📊 Campos Transformados

El dataset de personajes incluye campos adicionales calculados:

- `age_at_first_film` - Edad del personaje en la primera película
- `gender_segment` - Segmentación estandarizada de género
- `weight_segment` - Segmentación de peso en rangos
- `num_films` - Número de películas en las que aparece
- `num_vehicles` - Número de vehículos que posee
- `num_species` - Número de especies a las que pertenece

## 🔧 Requisitos

- Python 3.7 o superior
- pandas >= 2.0.0
- requests >= 2.31.0

## 📝 Licencia

Este proyecto utiliza datos de [SWAPI - The Star Wars API](https://swapi.py4e.com/), que está libremente disponible para uso público.

## 👤 Autor

Milton Jair

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

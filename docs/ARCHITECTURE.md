# Arquitectura del Proyecto SWAPI ETL

## Descripción General

Este documento describe la arquitectura y organización del proyecto SWAPI ETL, una herramienta modular para extraer, transformar y cargar datos de Star Wars desde la API SWAPI.

## Estructura de Módulos

### 1. `src/config.py`
**Propósito:** Almacena todas las constantes y configuraciones del proyecto.

**Contenido:**
- `SWAPI_ENDPOINT`: URL base de la API
- `CATEGORIES`: Diccionario con las categorías disponibles y sus URLs
- `WEIGHT_SEGMENTS`: Rangos para la segmentación de peso

**Por qué es importante:** Centralizar la configuración facilita el mantenimiento y permite cambios rápidos sin modificar la lógica del negocio.

### 2. `src/api_client.py`
**Propósito:** Maneja toda la comunicación con la API SWAPI.

**Funciones principales:**
- `get_all_swapi_data(category)`: Obtiene todos los datos de una categoría con paginación automática
- `get_resource_name(url)`: Obtiene el nombre de un recurso desde su URL
- `get_resource_names(urls)`: Versión batch de la función anterior

**Por qué es importante:** Separar la lógica de API permite cambiar el proveedor de datos sin afectar el resto del código.

### 3. `src/transformers.py`
**Propósito:** Contiene todas las funciones de transformación y enriquecimiento de datos.

**Funciones principales:**
- `calculate_age()`: Calcula la edad de los personajes
- `segment_gender()`: Estandariza categorías de género
- `segment_weight()`: Categoriza pesos en rangos
- `transform_people_dataframe()`: Aplica todas las transformaciones al DataFrame de personajes

**Por qué es importante:** Mantener las transformaciones en un módulo separado hace que sean reutilizables y fáciles de testear.

### 4. `src/exporters.py`
**Propósito:** Gestiona la exportación de datos a diferentes formatos.

**Funciones principales:**
- `save_dataframe_as_csv()`: Exporta DataFrame a CSV
- `save_data_as_json()`: Exporta datos a JSON
- `export_swapi_category()`: Exporta una categoría en ambos formatos

**Por qué es importante:** Centralizar la lógica de exportación permite añadir nuevos formatos fácilmente.

### 5. `src/main.py`
**Propósito:** Punto de entrada principal que orquesta todo el proceso ETL.

**Flujo de ejecución:**
1. Extrae datos de películas
2. Extrae y transforma datos de personajes
3. Guarda el dataset de personajes
4. Exporta todas las categorías

**Por qué es importante:** Proporciona una interfaz clara y simple para ejecutar todo el proceso.

## Flujo de Datos

```
1. Extracción (Extract)
   ├─ api_client.py obtiene datos de SWAPI
   └─ config.py proporciona las URLs

2. Transformación (Transform)
   ├─ transformers.py enriquece los datos
   ├─ Convierte URLs a nombres
   ├─ Calcula métricas derivadas
   └─ Segmenta datos en categorías

3. Carga (Load)
   ├─ exporters.py guarda los datos
   ├─ Exporta a CSV
   └─ Exporta a JSON
```

## Beneficios de esta Arquitectura

### ✅ Separación de Responsabilidades
Cada módulo tiene una responsabilidad única y bien definida.

### ✅ Mantenibilidad
Es fácil encontrar y modificar funcionalidades específicas.

### ✅ Testabilidad
Las funciones puras son fáciles de testear sin dependencias externas.

### ✅ Escalabilidad
Añadir nuevas funcionalidades es simple y no afecta el código existente.

### ✅ Reutilización
Los módulos pueden ser importados y utilizados en otros proyectos.

## Comparación: Antes vs. Después

### Antes (Monolítico)
- ❌ Un único archivo de 181 líneas
- ❌ Lógica mezclada y difícil de seguir
- ❌ Difícil de mantener y extender
- ❌ Sin documentación estructurada
- ❌ Sin configuración centralizada

### Después (Modular)
- ✅ Código organizado en 5 módulos especializados
- ✅ Cada módulo con responsabilidad única
- ✅ Fácil de entender y mantener
- ✅ Documentación completa con docstrings
- ✅ Configuración centralizada
- ✅ Estructura de proyecto profesional

## Extensiones Futuras

Gracias a esta arquitectura modular, es fácil añadir:

1. **Nuevas Fuentes de Datos**: Crear nuevos clientes en `api_client.py`
2. **Más Transformaciones**: Añadir funciones a `transformers.py`
3. **Nuevos Formatos**: Extender `exporters.py` (ej: Excel, Parquet)
4. **Tests Unitarios**: Cada módulo puede ser testeado independientemente
5. **API REST**: Exponer la funcionalidad como servicio web
6. **Caché**: Implementar caché para reducir llamadas a la API
7. **Logging**: Añadir sistema de logs centralizado

## Conclusión

Esta arquitectura modular transforma un script monolítico en un proyecto profesional, mantenible y escalable, siguiendo las mejores prácticas de desarrollo de software.

# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

## [1.0.0] - 2026-02-04

### 🎉 Reorganización Completa del Repositorio

#### Añadido
- **Estructura de directorios organizada:**
  - `src/` - Código fuente modular
  - `data/` - Directorio para datos generados
  - `docs/` - Documentación del proyecto

- **Módulos Python separados:**
  - `src/config.py` - Constantes y configuración centralizada
  - `src/api_client.py` - Cliente para la API SWAPI
  - `src/transformers.py` - Funciones de transformación de datos
  - `src/exporters.py` - Funciones de exportación (CSV/JSON)
  - `src/main.py` - Punto de entrada principal del ETL

- **Archivos de configuración:**
  - `requirements.txt` - Gestión de dependencias
  - `.gitignore` - Exclusión de archivos generados y temporales

- **Documentación mejorada:**
  - `README.md` actualizado con instrucciones completas
  - `docs/ARCHITECTURE.md` - Explicación detallada de la arquitectura
  - Docstrings en todas las funciones

#### Mejorado
- **Código modular:** Separación de responsabilidades por módulo
- **Mantenibilidad:** Código más fácil de leer y mantener
- **Documentación:** Instrucciones claras de instalación y uso
- **Tipado:** Añadidas anotaciones de tipo en funciones principales

#### Migrado
- Todo el código de `etl_swapi.py` ha sido refactorizado y distribuido en módulos especializados

### 📝 Detalles Técnicos

**Antes:**
- 1 archivo monolítico (`etl_swapi.py`)
- 181 líneas de código mezcladas
- Sin estructura de proyecto

**Después:**
- 5 módulos especializados
- Código organizado y documentado
- Arquitectura profesional siguiendo mejores prácticas

### 🔄 Retrocompatibilidad

Los datos generados mantienen exactamente el mismo formato que antes:
- `swapi_people_dataset.csv` - Dataset principal de personajes
- Archivos CSV y JSON por categoría

### 🎯 Próximos Pasos

- Añadir tests unitarios
- Implementar sistema de logging
- Considerar caché para reducir llamadas a la API
- Añadir CI/CD pipeline

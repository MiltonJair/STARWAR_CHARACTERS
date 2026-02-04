# Guía de Contribución

¡Gracias por tu interés en contribuir al proyecto SWAPI ETL! Esta guía te ayudará a hacer contribuciones efectivas.

## 🚀 Cómo Contribuir

### 1. Reportar Problemas

Si encuentras un bug o tienes una sugerencia:

1. Verifica que el problema no haya sido reportado previamente
2. Abre un nuevo issue con:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Comportamiento esperado vs. actual
   - Versión de Python y dependencias

### 2. Proponer Nuevas Funcionalidades

Para proponer nuevas características:

1. Abre un issue describiendo:
   - La funcionalidad propuesta
   - Casos de uso
   - Beneficios esperados
2. Espera feedback antes de comenzar a implementar

### 3. Enviar Pull Requests

#### Preparación

1. Fork el repositorio
2. Crea una rama desde `main`:
   ```bash
   git checkout -b feature/nombre-descriptivo
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

#### Desarrollo

1. **Sigue la arquitectura modular existente:**
   - `config.py` para constantes
   - `api_client.py` para interacciones con API
   - `transformers.py` para transformaciones de datos
   - `exporters.py` para exportación de datos

2. **Mantén el estilo de código:**
   - Usa docstrings en todas las funciones
   - Añade type hints cuando sea posible
   - Sigue PEP 8 para el estilo de Python

3. **Documenta tus cambios:**
   - Actualiza README.md si es necesario
   - Actualiza ARCHITECTURE.md si cambias la estructura
   - Añade entradas a CHANGELOG.md

#### Ejemplo de Docstring

```python
def mi_funcion(parametro: str) -> int:
    """
    Descripción breve de la función.
    
    Args:
        parametro: Descripción del parámetro
        
    Returns:
        Descripción del valor de retorno
    """
    # Implementación
    pass
```

#### Testing

Antes de enviar tu PR:

1. Verifica que el código importa correctamente:
   ```bash
   python -c "from src import *"
   ```

2. Prueba las funciones de transformación:
   ```bash
   python -c "from src.transformers import *; print('Tests OK')"
   ```

#### Commit

1. Haz commits descriptivos:
   ```
   feat: Añade función para calcular IMC de personajes
   fix: Corrige error en segmentación de peso
   docs: Actualiza README con nuevas instrucciones
   ```

2. Prefijos sugeridos:
   - `feat`: Nueva funcionalidad
   - `fix`: Corrección de bug
   - `docs`: Cambios en documentación
   - `refactor`: Refactorización de código
   - `test`: Añade o modifica tests
   - `chore`: Tareas de mantenimiento

#### Pull Request

1. Asegúrate de que tu rama esté actualizada con `main`
2. Abre un PR con:
   - Título descriptivo
   - Descripción detallada de los cambios
   - Referencias a issues relacionados
   - Screenshots si hay cambios visuales

## 📋 Checklist del PR

Antes de marcar tu PR como listo:

- [ ] El código sigue la arquitectura modular existente
- [ ] Se añadieron docstrings a funciones nuevas
- [ ] Se actualizó la documentación relevante
- [ ] Se añadieron entradas al CHANGELOG.md
- [ ] El código importa sin errores
- [ ] Los commits tienen mensajes descriptivos

## 💡 Ideas de Contribución

### Funcionalidades Deseadas

- [ ] Tests unitarios con pytest
- [ ] Sistema de logging configurable
- [ ] Caché de respuestas de API
- [ ] CLI con argumentos personalizables
- [ ] Soporte para más formatos de exportación (Excel, Parquet)
- [ ] Visualizaciones de datos
- [ ] API REST para exponer funcionalidades

### Mejoras de Documentación

- [ ] Tutorial paso a paso
- [ ] Ejemplos de uso avanzado
- [ ] Guía de análisis de datos
- [ ] Traducción al inglés

## 📞 ¿Necesitas Ayuda?

Si tienes preguntas:

1. Revisa la documentación en `/docs`
2. Busca en issues cerrados
3. Abre un nuevo issue con la etiqueta "question"

## 📜 Código de Conducta

- Sé respetuoso y constructivo
- Acepta críticas constructivas
- Enfócate en lo mejor para el proyecto
- Ayuda a mantener un ambiente colaborativo

## 🙏 Agradecimientos

¡Todas las contribuciones son valoradas! Gracias por ayudar a mejorar este proyecto.

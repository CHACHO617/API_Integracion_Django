# ClimaSeguro - API REST con integración SOAP

Este proyecto implementa una API RESTful utilizando Django y Django REST Framework para registrar zonas agrícolas, e integra un servicio SOAP real para convertir temperaturas de Celsius a Fahrenheit.

---

## Funcionalidades

### API REST - Zonas Agrícolas

Permite realizar operaciones CRUD sobre zonas agrícolas:

- **POST /api/zonas/**  
  Registrar una nueva zona agrícola

- **GET /api/zonas/**  
  Listar todas las zonas registradas

- **GET /api/zonas/{id}/**  
  Consultar una zona específica

- **DELETE /api/zonas/{id}/**  
  Eliminar una zona

- **PUT /api/zonas/id**

**Ejemplo JSON para POST & PUT:**
```json
{
  "nombre": "Región Norte",
  "cultivo_principal": "Café",
  "hectareas": 120.5,
  "latitud": -0.25,
  "longitud": -78.52
}
```

---

## Consumo de Servicio SOAP - Conversión de Temperatura 

Utiliza el servicio SOAP público de W3Schools para convertir temperaturas
Servicio SOAP consumido: https://www.w3schools.com/xml/tempconvert.asmx?WSDL

- **GET /api/temperatura/convertir?valor=30** 

**Respuesta Esperada:**
```json
{
  "celsius": 30.0,
  "fahrenheit": 86.0
}

```

## Instalación y Ejecución 

### 1. Clonar el repositorio
- git clone https://github.com/CHACHO617/API_Integracion_Django.git
- cd API_Integracion_Django

### 2. Crear entorno virtual
- python -m venv venv
- source venv/bin/activate        # En Windows: venv\Scripts\activate

### 3. Instalar dependencias
- pip install -r requirements.txt

### 4. Aplicar migraciones
- python manage.py migrate

### 5. Ejecutar el servidor
- python manage.py runserver

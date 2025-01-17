# Text Converter API

## ✅ Descripción

Este proyecto es una **API serverless** desarrollada para convertir texto a mayúsculas, desplegada en **AWS Lambda** y expuesta a través de **API Gateway**. Forma parte de mi portafolio y está diseñado para mostrar habilidades en **CI/CD** e integración de servicios en la nube.

---

## 🚀 Tecnologías utilizadas

- **FastAPI**: Framework para la creación de la API.
- **Mangum**: Adaptador para ejecutar FastAPI en AWS Lambda.
- **AWS Lambda**: Plataforma serverless para ejecutar el backend.
- **API Gateway**: Puerta de enlace HTTP para exponer el endpoint.
- **Docker**: Contenedor para empaquetar y desplegar la aplicación.
- **GitHub Actions**: Pipeline CI/CD para automatizar el despliegue.

---

## 🌟 Características principales

- **Serverless**: Totalmente desplegado en AWS Lambda, optimizando costos.
- **Automatización**: Cada cambio en la rama principal despliega automáticamente la nueva versión mediante GitHub Actions.
- **Portabilidad**: Docker asegura que la aplicación sea fácil de replicar.
- **Documentación automática**: Generación de Swagger UI gracias a FastAPI.

---

## 🛠️ Cómo usar el endpoint

### **URL del endpoint**
```
https://<api-id>.execute-api.<region>.amazonaws.com/default/convert
```

### **Método HTTP**
`POST`

### **Headers**
```json
{
  "Content-Type": "application/json"
}
```

### **Cuerpo de la solicitud**
```json
{
  "text": "hello"
}
```

### **Respuesta esperada**
```json
{
  "converted_text": "HELLO"
}
```

---

## 🔧 Cómo ejecutar el proyecto localmente

1. Clona el repositorio:
   ```bash
   git clone https://github.com/physiodevapp/text-converter-lambda.git
   cd text-converter-lambda
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: .\venv\Scripts\activate
   ```

3. Ejecuta el servidor local:
   ```bash
   uvicorn lambda_handler:app --host 0.0.0.0 --port 8000
   ```

4. Accede a la API en: [http://localhost:8000](http://localhost:8000)

---

## 🚀 Despliegue continuo

El proyecto utiliza **GitHub Actions** para automatizar el despliegue a AWS Lambda cada vez que se realiza un push a la rama principal. El flujo incluye:

1. Construcción de la imagen Docker.
2. Publicación de la imagen en Amazon ECR.
3. Actualización automática del código en AWS Lambda.

---

## 📌 Próximos pasos
- Añadir nuevas funcionalidades para demostrar la versatilidad del desarrollo en la nube.
- Ampliar la lógica de la API para incluir más operaciones con texto.


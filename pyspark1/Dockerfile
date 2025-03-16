FROM python:3.10-slim

# Instalar Java (usando OpenJDK 17) y otras dependencias necesarias
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    rm -rf /var/lib/apt/lists/*

# Configurar JAVA_HOME para que PySpark encuentre Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /workspace

# Actualizar pip e instalar PySpark
RUN pip install --upgrade pip && pip install pyspark

# Copiar los archivos del proyecto al contenedor
COPY . /workspace
# API Registro de Residencias

Este proyecto contiene una API REST para el registro de alumnos y empresas en el proceso de residencoas. El contenedor Docker incluye la aplicación y todas sus dependencias.

## Requisitos

- Docker

1. Se crea un Pipeline y se inserta el siguiente script

![image](https://github.com/user-attachments/assets/df02d2d4-2c25-4f55-80d2-55eab28a30de)


        pipeline {
        agent any
        stages {
        stage('Pull Docker Image') {
             steps {
                 script {
                     sh 'docker pull brandon1924/api-residencias:latest'
                 }
             }
         }
         stage('Run Docker Container') {
             steps {
                 script {
                     sh 'docker run -d -p 8000:8000 brandon1924/api-residencias'
                 }
             }
         }
         }
         }
   
3. Ejecutar el pipeline y ahora ya se puede realizar pruebas con Postman.
   Capturas de pantalla de las pruebas de los métodos:

- POST alumno


- GET alumno por su número de control


- PUT alumno por su número de control


- DELETE alumno por su número de control


- POST empresa
  

- GET empresa por su id
  

- PUT empresa por su id


- DELETE empresa por su id


- POST empresa_alumno


- GET empresa_alumno por su id


- put empresa_alumno por su id


- DELETE empresa_alumno por su id

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

![jenkins-docker](https://github.com/user-attachments/assets/310ea13e-af32-4e38-a525-e8a189c95e9d)

   
3. Ejecutar el pipeline y ahora ya se puede realizar pruebas con Postman.
   Capturas de pantalla de las pruebas de los métodos:

- POST alumno
![image](https://github.com/user-attachments/assets/129455b2-2b54-40fa-8ac9-df70f6c2ffe6)


- GET alumno 
![image](https://github.com/user-attachments/assets/0d6f0bec-4cca-4dfb-ae53-a5ea18d85ffd)


- PUT alumno por su número de control
![image](https://github.com/user-attachments/assets/2ebb731f-3d8c-40d3-8b7d-5102afb5450d)


- DELETE alumno por su número de control
![image](https://github.com/user-attachments/assets/3846f2a2-d64e-446a-81b9-8db3ffa7a1aa)


- POST empresa
![image](https://github.com/user-attachments/assets/8ea58384-f9cc-467d-8498-44d7b5feb42c)


- GET empresa por su id
![image](https://github.com/user-attachments/assets/871152b3-6c03-4ea9-8a86-be1b5121b37f)

- PUT empresa por su id
![image](https://github.com/user-attachments/assets/38b2c483-0c3b-4216-9cb0-f66b7a94024c)

- DELETE empresa por su id
![image](https://github.com/user-attachments/assets/95641349-e2ca-4d85-96c9-4e0eba59dd44)

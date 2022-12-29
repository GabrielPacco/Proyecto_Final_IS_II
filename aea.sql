pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/GabrielPacco/Backend_SecoSystem']]])
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/GabrielPacco/Backend_SecoSystem'
                sh 'python3 app.py'
            }
        }
        stage('Test unitario') {
            steps {
                git branch: 'main', url: 'https://github.com/GabrielPacco/Backend_SecoSystem'
                sh 'python3 test/unitarias/test_model.py'
            }
        }
        stage('Test funcional') {
            steps {
                git branch: 'main', url: 'https://github.com/GabrielPacco/Backend_SecoSystem'
                sh 'python3 test/funcionales/test_create_evento.py'
            }
        }
    }
}
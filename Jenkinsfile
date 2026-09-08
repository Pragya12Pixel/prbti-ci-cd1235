pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check AWS') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                                  credentialsId: 'aws-ecr-creds']]) {
                    bat 'aws sts get-caller-identity'
                }
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t cicd-python-app:v%BUILD_NUMBER% .'
            }
        }
    }
}
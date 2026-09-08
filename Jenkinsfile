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

        stage('ECR Login') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding',
                                  credentialsId: 'aws-ecr-creds']]) {
                    bat 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 726583840174.dkr.ecr.ap-south-1.amazonaws.com'
                }
            }
        }

        stage('Docker Tag') {
            steps {
                bat 'docker tag cicd-python-app:v%BUILD_NUMBER% 726583840174.dkr.ecr.ap-south-1.amazonaws.com/cicd-python-app:v%BUILD_NUMBER%'
            }
        }

        stage('Docker Push') {
            steps {
                bat 'docker push 726583840174.dkr.ecr.ap-south-1.amazonaws.com/cicd-python-app:v%BUILD_NUMBER%'
            }
        }
    }
}
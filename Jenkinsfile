pipeline {
    agent any

    environment {
        IMAGE_NAME = "niputu17/demo-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/niputu17/demo-app.git',
                    credentialsId: 'github-cred'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $IMAGE_NAME:latest
                    '''
                }
            }
        }

        stage('Deploy to Minikube with Helm') {
            steps {
                sh '''
                    helm upgrade --install demo-app ./chart/demo-app \
                      --set image.repository=$IMAGE_NAME \
                      --set image.tag=latest
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    kubectl get pods
                    kubectl get svc demo-app
                    curl -s $(minikube ip):30001
                '''
            }
        }
    }
}

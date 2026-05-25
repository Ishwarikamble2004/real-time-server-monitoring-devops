pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ishwarikamble2004/real-time-server-monitoring-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'cd app && docker build -t system-health-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop system-health-container || exit 0'
                bat 'docker rm system-health-container || exit 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d -p 5001:5000 --name system-health-container system-health-app'
            }
        }
    }
}
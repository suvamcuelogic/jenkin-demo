pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "\033[33mAnsi-color_Example\033[0m"'

            }
        }
        stage('Test') {
            steps {
            sh "echo '\033[34mTesting\033[0m '"
            }
        }
        stage('Deploy') {
            steps {
            sh "echo '\033[35mDeploying!\033[0m '"
            }
        }
    }
}

pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python -m unittest discover -v -p ""*.py" test'
            }
        }
    }
}
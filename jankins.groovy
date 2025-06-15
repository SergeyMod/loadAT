pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out task4 branch...'
                git branch: 'task4', url: 'https://github.com/SergeyMod/loadAT.git'
            }
        }

        stage('Build & Test') {
            steps {
                echo '⚙️ Building virtual environment and running tests...'
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
                    pytest --alluredir=allure-results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                echo '📊 Generating Allure report...'
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}
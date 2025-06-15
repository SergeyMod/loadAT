pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        PYTHON = "${VENV_DIR}/bin/python3"
        PIP = "${VENV_DIR}/bin/pip"
        PYTEST = "${VENV_DIR}/bin/pytest"
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
                    source ${VENV_DIR}/bin/activate
                    ${PIP} install --upgrade pip
                    if [ -f requirements.txt ]; then ${PIP} install -r requirements.txt; fi
                    ${PYTEST} --alluredir=allure-results
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
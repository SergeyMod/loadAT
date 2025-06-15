pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        PYTHON = "${VENV_DIR}/bin/python"
        PIP = "${VENV_DIR}/bin/pip"
        PYTEST = "${VENV_DIR}/bin/pytest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out test4 branch...'
                git branch: 'test4', url: 'https://github.com/your-org/your-repo.git'
            }
        }

        stage('Build & Test') {
            steps {
                echo '⚙️ Building virtual environment and running tests...'
                sh '''
                    python -m venv ${VENV_DIR}
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
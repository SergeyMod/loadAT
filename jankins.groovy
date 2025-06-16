pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
        API_URL = "${params.URL ?: 'https://petstore.swagger.io/v2'}"
        TEST_TYPE = "${params.TEST_TYPE}"
    }

    parameters {
        string(name: 'URL', defaultValue: 'https://petstore.swagger.io/v2', description: 'API base URL')
        choice(name: 'TEST_TYPE', choices: ['api', 'ui', 'all'], description: 'Тип тестов для запуска')
    }

    triggers {
        cron('0,30 9-10 * * *\n0 11 * * *')
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
                    if [ "${TEST_TYPE}" = "api" ]; then
                        pytest -m "api" --url=${API_URL} --alluredir=allure-results
                    elif [ "${TEST_TYPE}" = "ui" ]; then
                        pytest -m "ui" --url=${API_URL} --alluredir=allure-results
                    else
                        pytest --url=${API_URL} --alluredir=allure-results
                    fi
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
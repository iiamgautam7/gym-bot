pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe'
        VENV = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                REM Create virtual environment if not exists
                if not exist "${VENV}" (${PYTHON} -m venv "${VENV}")
                
                REM Upgrade pip and install requirements
                "${VENV}\\Scripts\\python.exe" -m pip install --upgrade pip
                "${VENV}\\Scripts\\python.exe" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                REM Run Gym Bot
                "${VENV}\\Scripts\\python.exe" gymbot.py
                """
            }
        }

        stage('Archive DB') {
            steps {
                archiveArtifacts artifacts: 'gymbot.db', fingerprint: true
            }
        }
    }

    post {
        always {
            bat """
            REM Kill any remaining Python processes
            taskkill /F /IM python.exe /T || exit 0
            """
        }
    }
}

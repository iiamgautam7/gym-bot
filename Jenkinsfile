pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\venv"
        PYTHON = "${VENV_DIR}\\Scripts\\python.exe"
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
                if not exist "${VENV_DIR}" (
                    C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m venv "${VENV_DIR}"
                )

                REM Upgrade pip and install requirements
                "${PYTHON}" -m pip install --upgrade pip
                "${PYTHON}" -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                REM Run Flask app in background using START /B (non-interactive)
                start "" /B "${PYTHON}" app.py

                REM Wait 10 seconds using PowerShell sleep
                powershell -Command "Start-Sleep -Seconds 10"
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                REM Run Gym Bot after Flask is up
                "${PYTHON}" gymbot.py
                """
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


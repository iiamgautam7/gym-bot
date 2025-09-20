pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
        VENV_DIR = "${WORKSPACE}\\venv"
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
                if not exist "%VENV_DIR%" (
                    ${PYTHON} -m venv %VENV_DIR%
                )

                REM Upgrade pip and install requirements
                %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip
                %VENV_DIR%\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                REM Run Flask app in background using START with /B (no interactive input)
                start "" /B "%VENV_DIR%\\Scripts\\python.exe" app.py

                REM Wait 10 seconds using non-interactive method (powershell sleep)
                powershell -Command "Start-Sleep -Seconds 10"
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                REM Run Gym Bot after Flask is up
                %VENV_DIR%\\Scripts\\python.exe gymbot.py
                """
            }
        }
    }

    post {
        always {
            bat """
            REM Kill any remaining Python processes (optional)
            taskkill /F /IM python.exe /T
            """
        }
    }
}

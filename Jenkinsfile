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

                REM Activate virtual environment and upgrade pip
                call %VENV_DIR%\\Scripts\\activate
                %VENV_DIR%\\Scripts\\python.exe -m pip install --upgrade pip

                REM Install required packages
                %VENV_DIR%\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                REM Activate venv and run Flask in background
                call %VENV_DIR%\\Scripts\\activate
                start /B %VENV_DIR%\\Scripts\\python.exe app.py > flask.log 2>&1

                REM Wait 5 seconds for Flask to start
                timeout /T 5
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                REM Activate venv and run Gym Bot
                call %VENV_DIR%\\Scripts\\activate
                %VENV_DIR%\\Scripts\\python.exe gymbot.py
                """
            }
        }
    }

    post {
        always {
            bat """
            REM Optional: stop Flask if needed (Windows)
            taskkill /F /IM python.exe /T
            """
        }
    }
}

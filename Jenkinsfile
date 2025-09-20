pipeline {
    agent any

    environment {
        // Full paths to your Python and pip executables
        PYTHON_PATH = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
        PIP_PATH = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                // Explicitly specify the 'main' branch to fix "Couldn't find any revision to build"
                git branch: 'main', url: 'https://github.com/iiamgautam7/gym-bot.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                REM Create virtual environment
                ${PYTHON_PATH} -m venv venv

                REM Activate virtual environment
                call venv\\Scripts\\activate

                REM Upgrade pip and install dependencies
                ${PIP_PATH} install --upgrade pip
                ${PIP_PATH} install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                REM Kill any existing Flask process to avoid conflicts
                for /F "tokens=5" %%a in ('netstat -ano ^| findstr :5000') do taskkill /PID %%a /F

                REM Start Flask app in background
                start /B ${PYTHON_PATH} app.py
                timeout /T 5
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                REM Activate virtual environment and run bot
                call venv\\Scripts\\activate
                ${PYTHON_PATH} gymbot.py
                """
            }
        }
    }

    triggers {
        // Run daily at 6 PM
        cron('0 18 * * *')
    }
}

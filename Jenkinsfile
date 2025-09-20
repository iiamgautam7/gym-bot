pipeline {
    agent any

    environment {
        PYTHON_PATH = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                // Ensure it checks out the main branch
                git branch: 'main', url: 'https://github.com/iiamgautam7/gym-bot.git'
            }
        }

        stage('Setup Python') {
            steps {
                bat """
                REM Create virtual environment
                ${env.PYTHON_PATH} -m venv venv

                REM Activate virtual environment and upgrade pip
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe -m pip install --upgrade pip

                REM Install requirements
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                REM Activate virtual environment and run Flask
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe app.py
                """
            }
        }

        stage('Run Gym Bot') {
            steps {
                bat """
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe gymbot.py
                """
            }
        }
    }

    triggers {
        cron('0 18 * * *')  // Runs daily at 6 PM
    }
}

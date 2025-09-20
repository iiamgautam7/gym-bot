pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/iiamgautam7/gym-bot.git'
            }
        }
        stage('Setup Python') {
            steps {
                bat """
                C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m venv venv
                call venv\\Scripts\\activate
                C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe install --upgrade pip
                C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\pip.exe install -r requirements.txt
                """
            }
        }
        stage('Run Flask App') {
            steps {
                bat """
                start /B venv\\Scripts\\python.exe app.py
                timeout /T 5
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
        cron('0 18 * * *')  // Run daily at 6 PM
    }
}

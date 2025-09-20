pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/iiamgautam7/gym-bot.git'
            }
        }
        stage('Setup Python') {
            steps {
                bat '''
                REM Create virtual environment
                C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python.exe -m venv venv
                
                REM Activate virtual environment
                call venv\\Scripts\\activate
                
                REM Upgrade pip and install requirements
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                bat '''
                REM Start Flask app in background
                start /B call venv\\Scripts\\activate && python app.py
                
                REM Wait 5 seconds for server to start
                timeout /T 5
                '''
            }
        }
        stage('Run Gym Bot') {
            steps {
                bat '''
                REM Run Selenium bot
                call venv\\Scripts\\activate
                python gymbot.py
                '''
            }
        }
    }
    triggers {
        cron('0 18 * * *')  // Run daily at 6 PM
    }
}

pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/gym-bot.git'
            }
        }
        stage('Setup Python') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                bat '''
                start /B python app.py
                timeout /T 5
                '''
            }
        }
        stage('Run Gym Bot') {
            steps {
                bat '''
                venv\\Scripts\\activate
                python gym.py
                '''
            }
        }
    }
    triggers {
        cron('0 18 * * *')  // Run daily at 6 PM
    }
}

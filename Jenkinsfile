pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo '📦 Checking out code from GitHub...'
                git branch: 'main', url: 'https://github.com/vj141900-dotcom/amazon-grid-ci.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '⚙️ Installing Python and Selenium...'
                sh 'pip3 install selenium'
            }
        }

        stage('Run Selenium Grid Test') {
            steps {
                echo '🚀 Running Selenium Grid test...'
                sh 'python3 amazon_test.py'
            }
        }

        stage('Generate Report') {
            steps {
                echo '📝 Archiving test report...'
                archiveArtifacts artifacts: 'report.html', followSymlinks: false
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline execution completed!'
        }
    }
}

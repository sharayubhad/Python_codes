pipeline{
    agent any

    stages{
        stage('Git Clone'){
            steps{
                git branch: 'main', credentialId: '' , url: ''
            }

        }
    }

    post{
        success{
            echo 'pipeline successfully completed'
        }
        failure{
            echo 'pipeline failed,Please checks the logs for more information.'

        }
    }
}
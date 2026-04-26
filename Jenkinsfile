pipeline {
    agent any

    environment {
        // We define the EC2 details here
        EC2_HOST = 'your-ec2-ip-address'
        SSH_KEY_ID = 'ec2-ssh-key' // The ID of the credential stored in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                // Equivalent to actions/checkout@v4
                checkout scm
            }
        }

        stage('Deploy to EC2') {
            steps {
                // Using sshagent to securely handle your private key
                sshagent([env.SSH_KEY_ID]) {
                    // 1. Copy files using SCP
                    sh "scp -o StrictHostKeyChecking=no -r . ubuntu@${env.EC2_HOST}:/home/ubuntu/app"

                    // 2. Run remote commands using SSH
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@${env.EC2_HOST} '
                            if ! [ -x "\$(command -v docker)" ]; then
                                sudo apt-get update
                                sudo apt-get install -y docker.io
                                sudo usermod -aG docker ubuntu
                            fi
                            
                            cd /home/ubuntu/app
                            sudo docker stop flask-app || true
                            sudo docker rm flask-app || true
                            sudo docker build -t flask-app .
                            sudo docker run -d -p 80:5000 --name flask-app flask-app
                        '
                    """
                }
            }
        }
    }
}

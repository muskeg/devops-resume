pipeline {
	agent {
		docker {
			image 'centos:centos8'
			args '-u root:root --dns 8.8.8.8'
		}
	}
	environment {
		GPG_SECRET_KEY = credentials('gpg-secret-key')
	}

	stages {
		stage('Checkout and environment') {
			steps {
				echo "Building.."
				checkout scm
				sh """
				yum install -y yum-utils
				yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
				yum install epel-release
				yum install -y docker git-secret
				gpg --batch --import $GPG_SECRET_KEY
				cd $WORKSPACE
				git secret reveal -f -p ''
				cat .env.prod
				"""
                        }	
        	}
        

		stage('Deploy') {
			steps {
				echo "Deploy.."
			}
		}
	}
	
	post { 
		always { 
			cleanWs()
		}
	}
}

pipeline {
	agent {
		docker {
			image 'maven:3.6.3-alpine'
			args '-u root:root'
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
				apk add git-secret
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

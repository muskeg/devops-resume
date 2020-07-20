pipeline {
	agent {
		docker {
			image 'alpine:latest'
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
				cat > /etc/apk/repositories << EOF; $(echo)
				http://dl-cdn.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/main
				http://dl-cdn.alpinelinux.org/alpine/v$(cat /etc/alpine-release | cut -d'.' -f1,2)/community
				EOF

				apk update
				apk add docker git-secret
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

pipeline {
	agent {
		docker {
			image 'alpine:3.12'
			args '-u root:root --network host'
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
				echo "http://dl-cdn.alpinelinux.org/alpine/v3.12/main" >> /etc/apk/repositories
				echo "http://dl-cdn.alpinelinux.org/alpine/v3.12/community" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/main/" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories
				apk update
				apk add openrc docker docker-compose gawk git git-secret
				gpg --batch --import $GPG_SECRET_KEY
				cd $WORKSPACE
				git secret reveal -f -p ''
				touch /run/openrc/softlevel
				rc-service docker status
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

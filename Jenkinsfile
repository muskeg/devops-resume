pipeline {
	agent {
		docker {
			image 'centos:centos8'
			args '-u root:root --network host -v /var/run/docker.sock:/var/run/docker.sock -v /usr/local/bin/docker-compose:/usr/local/bin/docker-compose'
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
				yum install -y epel-release
				yum install -y git-secret
				yum install -y docker-ce --nobest
				gpg --batch --import $GPG_SECRET_KEY
				cd $WORKSPACE
				git secret reveal -f -p ''
				docker-compose -f docker-compose.prod.yaml up -d --build
                                docker images
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

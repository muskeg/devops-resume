pipeline {
	agent none
	stages {
		stage('Clean up') {
                        agent {
                                node {
                                        label 'jenkins@muskegg'
                                }
                        }
			steps {
				cleanWs()
			}
		}

		stage('Checkout, env files') {
        		agent {
                		docker {
                        		image 'alpine:3.12'
                        		args '-u root:root --network host -v ${PWD}:/usr/src/app -w /usr/src/app'
                		}
        		}
			environment {
				GPG_SECRET_KEY = credentials('gpg-secret-key')
			}
			steps {
				checkout scm
				sh """
				echo "http://dl-cdn.alpinelinux.org/alpine/v3.12/main" >> /etc/apk/repositories
				echo "http://dl-cdn.alpinelinux.org/alpine/v3.12/community" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/main/" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/community/" >> /etc/apk/repositories
				echo "http://nl.alpinelinux.org/alpine/edge/testing/" >> /etc/apk/repositories
				apk update
				apk add gawk git git-secret
				gpg --batch --import $GPG_SECRET_KEY
				cd $WORKSPACE
				git secret reveal -f -p ''
				"""
                        }	
        	}
        

                stage('Build') {
			agent {
				node { 
					label 'jenkins@muskegg' 
				}
			}
                        steps {
				sh """
				cd $WORKSPACE
				/usr/local/bin/docker-compose -f docker-compose.prod.yaml build
				docker tag registry.muskegg.com:5000/webresume:latest registry.muskegg.com:5000/webresume:1.${BUILD_NUMBER} 
				docker tag registry.muskegg.com:5000/webresume-nginx:latest registry.muskegg.com:5000/webresume-nginx:1.${BUILD_NUMBER} 
				docker images
				"""
                        }
                }

		stage('Deploy') {
                        agent {
                                node {
                                        label 'jenkins@muskegg'
                                }
                        }
			steps {
				echo "Deploy.."
				withCredentials([usernamePassword(credentialsId: 'registry-muskegg', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
  					sh 'docker login https://registry.muskegg.com:5000 -u $USERNAME -p $PASSWORD'
				}
				sh """
				docker push registry.muskegg.com:5000/webresume
				docker push registry.muskegg.com:5000/webresume-nginx
				"""
				echo "Applying Kubernetes Deployment"
				script {
					def build_version = env.BUILD_NUMBER
        				def remote = [:]
        				remote.name = "kubernetes-master"
        				remote.host = "pi.home.muskegg.com"
        				remote.allowAnyHosts = true
					withCredentials([usernamePassword(credentialsId: 'ssh-k8s-master', passwordVariable: 'sshPassword', usernameVariable: 'sshUser')]) {
        				remote.user = sshUser
        				remote.password = sshPassword
					echo "kubectl --kubeconfig=/home/pi/.kube/config set image deployment muskegg-deployment app=registry.muskegg.com:5000/webresume:1.${build_version} web=registry.muskegg.com:5000/webresume-nginx:1.${build_version}"
					sshCommand remote: remote, command: "kubectl --kubeconfig=/home/pi/.kube/config set image deployment muskegg-deployment app=registry.muskegg.com:5000/webresume:1.${build_version} web=registry.muskegg.com:5000/webresume-nginx:1.${build_version}"
					}
				}
			}
		}
	}
	
}

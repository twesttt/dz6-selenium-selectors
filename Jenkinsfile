properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'master'
        }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage("Check system memory") {
            steps {
                sh "free -h"
            }
        }

//         stage("Clone the code") {
//             steps {
//                 sh "git clone https://github.com/twesttt/dz6-selenium-selectors.git"
//             }
//         }

        stage("Build docker image") {
            steps {
                sh "cd dz6-selenium-selectors"
                sh "git checkout allure-report"
                sh "git pull"
                docker { image 'hello-world' }
//                 sh "docker build -t mytest ."

            }
        }
    }
}
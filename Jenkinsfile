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

        stage("Build docker image") {
            steps {
                sh "git branch"
                sh "docker build -t mytest ."
            }
        }

        stage("Run tests in Docker") {
            steps {
                sh "docker run mytest"
            }
        }

        stage("Allure report"){
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'target/allure-results']]
            }
        }
    }
}
//     post {
//         always {
//             stage("Allure report"){
//                 steps {
//                     allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
//                 }
//             }
//         }
//     }

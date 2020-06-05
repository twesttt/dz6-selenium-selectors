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
                sh "cd dz6-selenium-selectors"
                sh "git checkout allure-report"
                sh "git pull"
                sh "docker build -t mytest ."
            }
        }

        stage("Run tests in Docker") {
            steps {
                sh "docker run mytest"
            }
        }
    }
    post {
        always {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
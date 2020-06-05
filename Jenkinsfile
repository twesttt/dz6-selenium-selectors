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
                sh "git clone https://github.com/twesttt/dz6-selenium-selectors.git"
                sh "cd dz6-selenium-selectors"
                sh "git checkout allure-report"
                sh "git pull"
                sh "docker build -t mytest ."
            }
        }

        stage("Run tests in Docker and get Allure reports") {
            steps {
                sh "docker run mytest"
            }
        }

        stage("Allure Reports") {
            allure([
                includeProperties: false,
                jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: './allure-results']]
                ])
        }

    }
}
pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build . -t test:1'
        sh 'docker ps'
      }
    }

    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        script{
        def doc_containers = sh(returnStdout: true, script: 'docker container ps -aq').replaceAll("\n", " ") 
                    if (doc_containers) {
                        sh "docker stop ${doc_containers}"
                    }}
        sh 'docker run -d -p 8000:8000 test:1'
        sh 'docker ps'
      }
    }

  }
}

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build . -t test_python'
      }
    }

    stage('Stop old') {
      steps {
        echo 'Stop old..'
        script {
            def doc_containers = sh(returnStdout: true, script: 'docker container ps -aq').replaceAll("\n", " ")
                if (doc_containers) {
                    sh "docker stop ${doc_containers}"
                }
        }
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        sh 'docker run --name python-web --detach --rm --network python-app -p 8000:8000 test_python'
        sh 'docker ps'
      }
    }
  }
}

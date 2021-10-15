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
        sh 'docker ps'
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
        sh 'docker run --name python-web --rm -d -p 80:5000 test_python'
        sh 'docker ps'
        sh 'docker ps -a'
      }
    }
  }
}

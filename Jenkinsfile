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
                    sh 'docker stop ${doc_containers}'
                    sh 'docker system prune -a'
                }
        }
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        sh 'docker network create python-app'
        sh 'docker run --name python-web --rm -itd --network python-app --network-alias python-web -h python-web -p 8000:8000 test_python'
        sh 'docker ps'
      }
    }
  }
}

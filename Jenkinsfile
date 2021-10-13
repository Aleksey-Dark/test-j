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
         sh 'docker ps -a'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        sh 'docker run --name python-web --rm -d --network python-app --network-alias python-web -h python-web -p 8000:8000 test_python'
        sh 'docker ps'
      }
    }
  }
}

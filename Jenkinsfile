pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build . -t flask'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        sh 'docker volume create python-data'
        sh 'docker run --name python-app --rm --detach --network python-app --network-alias python-app --publish 80:8000 --volume python-data:/usr/src/app flask'
        sh 'docker ps'
        sh 'docker exec docker bash -c \'pwd\''
      }
    }
  }
}

pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build . -t test_python'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying....'
        sh 'docker network create python-app'
        sh 'docker volume create python-data'
        sh 'docker run --name python-app --rm --detach --network python-app --publish 8000:8000 --volume python-data:./ python-web'
        sh 'docker ps'
        sh 'sudo docker exec python-web bash -c \'pwd\''
      }
    }
  }
}

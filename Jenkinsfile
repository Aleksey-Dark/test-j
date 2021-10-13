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
        sh 'docker container run --name python-app --rm --detach --publish 8000:8000 python-web'
        sh 'docker ps'
        sh 'sudo docker exec python-web bash -c \'pwd\''
      }
    }
  }
}

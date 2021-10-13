pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building..'
        sh 'docker build . -t flask'
        sh 'docker ps -a'
        sh 'docker ps'
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
        sh 'docker volume create python-data'
        sh 'docker run --name python-web --detach --rm --network python-app --network-alias python-app --publish 8000:8000 --volume python-data:/usr/src/app flask'
        sh 'docker ps -a'
        sh 'docker ps'
        sh 'docker exec python-web bash -c \'pwd\''
      }
    }
  }
}

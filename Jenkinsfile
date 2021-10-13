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
        sh 'docker stop $(docker ps -a | awk -v i="^$1.*" '{if($2~i){print$1}}')'
        sh 'docker run -d test:1 -p 80:8000'
        sh 'docker ps'
      }
    }

  }
}

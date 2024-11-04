pipeline {
    agent any

    environment {
        CONDA_ENV = 'pyspark'                   // Name of the Conda environment you want to use
        CONDA_HOME = '/home/ubuntu/miniconda3'  // Path to your Conda installation
    }

    stages {
        stage('Check Branch') {
            when {
                expression { env.BRANCH_NAME == 'master' }
            }
            steps {
                echo "Running on the 'master' branch..."
            }
        }

        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }

        stage('Setup Conda Environment') {
            steps {
                script {
                    echo "Checking if the Conda environment ${CONDA_ENV} exists..."
                    def envExists = sh(script: "${CONDA_HOME}/bin/conda env list | grep ${CONDA_ENV}", returnStatus: true) == 0

                    if (!envExists) {
                        echo "Creating Conda environment: ${CONDA_ENV}"
                        sh "${CONDA_HOME}/bin/conda create -n ${CONDA_ENV} python=3.10.0 -y"
                    } else {
                        echo "Conda environment ${CONDA_ENV} already exists."
                    }
                }
            }
        }

        stage('Activate Environment and Install Dependencies') {
            steps {
                echo 'Activating the Conda environment and installing dependencies...'
                sh """
                    source ${CONDA_HOME}/bin/activate ${CONDA_ENV} || true
                    ${CONDA_HOME}/bin/conda run -n ${CONDA_ENV} pip install -r requirements.txt
                """
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                sh """
                    source ${CONDA_HOME}/bin/activate ${CONDA_ENV} || true
                    ${CONDA_HOME}/bin/conda run -n ${CONDA_ENV} pytest --maxfail=1 --disable-warnings
                """
                echo 'Tests completed.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. All tests passed!'
        }
        failure {
            echo 'Pipeline failed. Please check the test results or console output for details.'
        }
    }
}

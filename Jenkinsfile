pipeline {
    agent any

    environment {
        CONDA_ENV = 'pyspark'  // Name of the Conda environment you want to use
        CONDA_HOME = '/home/ubuntu/miniconda3'  // Path to your Conda installation
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                // Clone the repository
                checkout scm
                echo 'Repository cloned successfully.'
            }
        }

        stage('Setup Conda Environment') {
            steps {
                script {
                    echo "Checking if the Conda environment ${CONDA_ENV} exists..."
                    // Check if the Conda environment already exists
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
                // Activate the Conda environment and install dependencies
                sh """
                    source ${CONDA_HOME}/bin/activate ${CONDA_ENV}
                    pip install -r requirements.txt
                """
                echo 'Dependencies installed successfully.'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with pytest...'
                // Run pytest with warnings disabled
                sh """
                    source ${CONDA_HOME}/bin/activate ${CONDA_ENV}
                    pytest --maxfail=1 --disable-warnings
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

    // Specify branch condition manually
    when {
        branch 'master'  // Only run this pipeline on the 'master' branch
    }
}

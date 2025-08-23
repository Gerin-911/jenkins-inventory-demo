pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Update Inventory') {
            steps {
                echo "Trừ kho dựa trên đơn hàng..."
                bat '"C:/Users/lieuv/AppData/Local/Programs/Python/Python313/python.exe" scripts/update_inventory.py'
            }
        }

        stage('Generate Report') {
            steps {
                echo "Generate Report skipped (chỉ demo)"
            }
        }

        stage('Send Notification (demo)') {
            steps {
                echo "Send Notification skipped (chỉ demo)"
            }
        }
    }
}

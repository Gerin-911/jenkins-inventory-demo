pipeline {
    agent any

    environment {
        PYTHON = "C:/Users/lieuv/AppData/Local/Programs/Python/Python313/python.exe"
        INVENTORY_FILE = "inventory.txt"
        ORDERS_FILE = "orders.txt"
        REPORT_FILE = "report.txt"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/Gerin-911/jenkins-inventory-demo.git', branch: 'main'
            }
        }

        stage('Update Inventory') {
            steps {
                // Chuyển console sang UTF-8 để tránh lỗi Unicode
                bat 'chcp 65001'

                // Chạy script Python để update inventory
                bat "\"${env.PYTHON}\" scripts/update_inventory.py"
            }
        }

        stage('Generate Report') {
            steps {
                bat 'chcp 65001'
                bat "\"${env.PYTHON}\" scripts/generate_report.py"
            }
        }

        stage('Send Notification') {
            steps {
                echo "✅ Pipeline hoàn tất. Kiểm tra ${REPORT_FILE} để xem báo cáo."
            }
        }
    }
}


bat 'chcp 65001' // đổi sang UTF-8
bat '"C:/Users/lieuv/AppData/Local/Programs/Python/Python313/python.exe" scripts/update_inventory.py'
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
                echo 'Trừ kho dựa trên đơn hàng...'
                bat '"C:/Users/lieuv/AppData/Local/Programs/Python/Python313/python.exe" scripts/update_inventory.py'
            }
        }

        stage('Generate Report') {
            steps {
                echo 'Tạo báo cáo...'
                bat '"C:/Users/lieuv/AppData/Local/Programs/Python/Python313/python.exe" scripts/generate_report.py'
            }
        }
    }
}

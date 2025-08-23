pipeline {
    agent any

    triggers {
        // chạy hằng ngày 23:59
        cron('59 23 * * *')
    }

    stages {
        stage('Update Inventory') {
            steps {
                echo "Trừ kho dựa trên đơn hàng..."
                bat '"C:\Users\lieuv\AppData\Local\Programs\Python\Python313\python.exe" scripts/update_inventory.py'
            }
        }

        stage('Generate Report') {
            steps {
                echo "Tạo báo cáo cuối ngày..."
                bat '"C:\Users\lieuv\AppData\Local\Programs\Python\Python313\python.exe" scripts/generate_report.py'
            }
        }

        stage('Send Notification (demo)') {
            steps {
                echo "Gửi báo cáo cho nhà cung cấp (giả lập)..."
                bat 'cat reports/daily_report.csv'
            }
        }
    }
}


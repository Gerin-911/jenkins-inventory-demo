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
                sh 'python3 scripts/update_inventory.py'
            }
        }

        stage('Generate Report') {
            steps {
                echo "Tạo báo cáo cuối ngày..."
                sh 'python3 scripts/generate_report.py'
            }
        }

        stage('Send Notification (demo)') {
            steps {
                echo "Gửi báo cáo cho nhà cung cấp (giả lập)..."
                sh 'cat reports/daily_report.csv'
            }
        }
    }
}


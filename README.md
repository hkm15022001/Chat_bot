Cài đặt theo hướng dẫn sau

# Mở terminal tại thư mục gốc của dự án và chạy lệnh sau:

pip install -r requirements.txt

# Hãy kiểm tra xem trong các thư mục LogisticRegression, NaiveBayes đã có file.pkl chưa nếu chưa hãy train lại theo hướng dẫn sau. Cụ thể mỗi thư mục của thuật toán sẽ có file trainning_algorimth.py hãy chạy file này

Ví dụ: Từ thư mục gốc của dự án ta chạy các lệnh terminal sau:

cd NaiveBayes

python training_NaiveBayes.py

cd ..

cd LogisticRegression

python training_LogisticRegression.py

cd ..

cd PhoBert

python training_PhoBert.py

# Sau đó để chạy chương trình

cd ..

python usingChatBot.py

# Do trainning với PhoBert khá lâu cần GPU để train nên link dưới đây là file weight đã được train sẵn của PhoBert. Hãy tải file này và đặt vào folder PhoBert với tên là PhoBert_weight.pth

link PhoBert_weight https://drive.google.com/file/d/1LBT2gha91lMcY4oBYD27uSxMyccjXMZV/view?usp=drive_link

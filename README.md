# JARVIS (Sản phẩm về trợ lý giọng nói)

## Mô tả chung

Ứng dụng trợ lý ảo Jarvis có thể giúp người dùng thực hiện việc tra cứu thông tin, hoặc làm một số thao tác cơ bản trên máy tính. Chỉ bằng một lời nói, ứng dụng sẽ chuyển đổi giọng nói của người dùng thành văn bản, thông qua việc tiền xử lý dữ liệu (để phân loại yêu cầu từ người dùng: tra google, xem youtube hay tra cứu từ điển,...) và xử lý dữ liệu (dùng google API để lấy thông tin cần thiết do người dùng yêu cầu)

## Demo

- Chạy ứng dụng [Jarvis](https://www.youtube.com/watch?v=6ncxw0XDeoI)

## Chức năng của app

Ứng dụng có những chức năng sau:

- Chào hỏi
- Tìm kiếm bất cứ điều gì trên Google 
- Chơi nhạc, phát video trên YouTube
- Cung cấp thông tin về ngày, giờ
- Cung cấp thông tin thời tiết tại bất cứ thành phố nào trên thế giới
- Tra cứu ý nghĩa của một cụm từ nào đó
- Chụp ảnh màn hình và lưu ảnh tại folder của project
- Tắt máy, khởi động lại máy

 
## Cấu trúc code

    ├── src                              # main folder for source codes 
    │   ├── core_interaction             # Contains all secret API Keys
    │   │   ├── __init__.py              # classify the preprocessed sentence into 4 categories
    │   │   ├── browser_interface.py     # browse google or youtube for anything
    │   │   ├── info_interface.py        # get info about time, date, weather, or look up any word
    │   │   ├── media_interface.py       # search any thing on youtube
    │   │   └── system_interface.py      # to shutdown, reboot, or take a screenshot
    │   ├── GUI                          # for graphical user interface
    │   ├── speech_to_text               # model that converts input speech to text
    │   ├── text_to_speech               # model that converts text to speech (then speak it out)
    │   ├── interpreter.py               # processing an input sentence after preprocessing it
    │   ├── preprocess.py                # format an input sentence to make it more explicit for the model
    │   └── sr_main.py                   # main driver program of Jarvis
    └── requirements.txt                 # all dependencies of the program
    
## Cách thức hoạt động

- Đầu tiên khi chạy app, một giao diện sẽ hiện ra, hệ thống sẵn sàng để nhận input (tiếng nói của người dùng)
- Trong trường hợp hệ thống đã nhận diện được giọng nói và chuyển giọng nói thành câu lệnh bằng văn bản
- Văn bản đó sẽ được tiền xử lý để phân loại câu lệnh đó thành 1 trong 4 loại: 
  - Tra cứu bằng Google
  - Xem trên Youtube
  - Trích thông tin về ngày tháng, thời tiết, tra cứu từ điển
  - Một số thao tác trên máy tính như chụp màn hình, tắt máy, khởi động lại máy
- Với mỗi loại sẽ có một hàm/model riêng để xử lý câu lệnh và đưa ra thông tin cần thiết cho người dùng
  - Nếu là tra cứu trên Google, Youtube thì hệ thống sẽ tự động mở trình duyệt với thông tin tương ứng
  - Nếu là tra cứu từ điển hoặc xem thông tin về ngày tháng, thời tiết, hệ thống sẽ chuyển văn bản đầu ra thành giọng nói
  - Nếu là thao tác trên máy tính, hệ thống sẽ được thực hiện thao tác đó luôn

## Thư viện

- Mô hình nhận dạng giọng nói và chuyển giọng nói thành văn bản [speech_recognition](https://pypi.org/project/SpeechRecognition/2.1.3)
- Mô hình chuyển từ văn bản thành giọng nói: [gTTS](https://readthedocs.org/projects/gtts/downloads/pdf/latest)
   
## Cài đặt

- Clone repo bằng lệnh ```git clone https://github.com/o2buzzle/SR-Homework3``` hoặc download zip & giải nén
- Trong command line/terminal, điều hướng tới thư mục chứa dự án này
- Cài đặt các thư viện của python bằng lệnh ```pip install -r requirements.txt```
- Riêng PyAudio sau phiên bản python 3.6 không thể cài đặt bằng pip, có thể cài trực tiếp thông qua file wheel của PyAudio ở [đây](https://stackoverflow.com/a/55630212)
- Chạy dự án bằng 2 lệnh ```cd src``` và ```python main.py```
- Enjoy !!!!



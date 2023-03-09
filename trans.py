import os

# 取得當前工作目錄
current_dir = os.getcwd()
out_dir = "finish_transparent"

# 用來判斷檔案是否為png圖片
def is_png(filename):
    return filename.lower().endswith('.png')

# 建立 finish 資料夾
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

count = 1

# 搜尋資料夾中的png圖片，逐一進行處理
for filename in os.listdir(current_dir):
    if is_png(filename):
        count = count + 1
        print(count)
        print("Processing {filename}")
        command = f'backgroundremover -i "{filename}" -o "./{out_dir}/{count}.png"'
        print(command)
        os.system(command)
from PIL import Image
import numpy as np
import os

if __name__ == '__main__':
    work_dir = "labels" # 图像所处文件夹
    target_dir = 'masks'
    file_names = os.listdir(work_dir)
    count = 0
    for file_name in file_names:
        # print(file_name)
        file_path = os.path.join(work_dir,file_name)

        image = Image.open(file_path)
        img = np.array(image)
        img[img!=0] = 1

        # 重新保存
        image = Image.fromarray(img)
        # print(np.array(image).shape)
        # print(np.array(image))
        target_file_path = os.path.join(target_dir,file_name)
        image.save(f'{target_file_path}') 
        count+=1
    print(count)
        
       

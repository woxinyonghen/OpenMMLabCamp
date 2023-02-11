1. 训练模型的配置文件【**pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_satellite_building.py**】
2. 训练好的模型文件【**iter_8000.pth**】

​			百度云盘链接：https://pan.baidu.com/s/1DncJ-hA_C21QyCVxHNreyw提取码：cl8k

​			模型性能如下：

|   Class    |  IoU  |  Acc  |
| :--------: | :---: | :---: |
| background | 90.28 | 94.53 |
|  building  | 66.12 | 80.86 |

 3. 其他作业相关的文件（log文件等）

    a.数据集  卫星建筑物：https://www.kaggle.com/datasets/hyyyrwang/buildings-dataset

    ​		划分训练集和数据集【scripts/split_data.py】

    ​		label图片数据转mask图片数据【scripts/label_to_mask.py】

    b.训练

    ​		训练python脚本【scripts/train_data.py】

    ​		训练GPU任务脚本【scripts/run_satellite_building.sh】

    ​		训练日志文件【**20230211_201914.log**】、训练JSON日志文件 【**logs/20230211_201914.json**】

    ​		训练服务器日志文件【**logs/slurm-300830.out**】

    c.测试

    ​		imgs/分割预测结果01.png、imgs/分割预测结果02.png、imgs/连通域分析03.png

    ​		imgs/连通域分析04.png、imgs/测试集标注05.png、imgs/测试集标注06.png

    ​		imgs/测试集标注07.png、imgs/混淆矩阵.jpg

    d.评估

    ​	评估GPU任务脚本【scripts/run_test_satellite.sh】

    ​	评估服务器日志【logs/slurm-300869.out】
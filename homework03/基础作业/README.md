1. 训练模型的配置文件【**pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_mouse.py**】

2. 训练好的模型文件【**iter_800.pth**】

    百度云盘链接：https://pan.baidu.com/s/1gyPPMe6wyno68PJOD1rr_g 提取码：9ct7

    模型性能如下：

    |   Class    |  IoU  |  Acc  |
    | :--------: | :---: | :---: |
    | background | 99.14 | 99.62 |
    | glomeruili | 62.88 | 75.19 |

    aAcc: 99.1600  mIoU: 81.0100  mAcc: 87.4000

 3. 其他作业相关的文件（log文件等）

    a.探索数据集【scripts/explore_data.py】

    ​		相关可视化见imgs目录

    b.划分训练集和数据集 【scripts/split_data.py】

    c.MMSeg训练语义分割模型

    ​		训练python脚本【scripts/train_data.py】、训练GPU任务脚本【run_mouse_glomeruli.sh】

    ​		训练日志文件【**20230210_153801.log**】、训练JSON日志文件 【**20230210_153801.json**】

    ​		训练服务器日志文件【**slurm-299694.out**】

    d.用训练得到的模型预测

    ​		imgs/分割预测结果01.png、imgs/分割预测结果02.png、imgs/连通域分析03.png

    ​		imgs/连通域分析04.png、imgs/测试集标注05.png、imgs/测试集标注06.png

    ​		imgs/测试集标注07.png、imgs/混淆矩阵.jpg

    e.测试集性能评估

    ​		性能评估【run_test.sh】日志文件【**logs/slurm-299856.out**】

    ​		+------------+-------+-------+
    ​		|   Class    |  IoU  |  Acc  |
    ​		+------------+-------+-------+
    ​		| background | 99.14 | 99.62 |
    ​		| glomeruili | 62.88 | 75.19 |
    ​		+------------+-------+-------+
    ​		02/10 15:56:48 - mmengine - INFO - Iter(test) [515/515]  aAcc: 99.1600  mIoU: 81.0100  mAcc: 87.4000

    ​		速度评估【run_test_speed.sh】日志文件【**logs/slurm-299896.out**】

    ​		Loads checkpoint by local backend from path: work/mouse_glomeruli/iter_800.pth
    ​		Done image [50 / 200], fps: 93.80 img / s
    ​		Done image [100/ 200], fps: 94.84 img / s
    ​		Done image [150/ 200], fps: 95.21 img / s
    ​		Done image [200/ 200], fps: 95.32 img / s
    ​		Overall fps: 95.32 img / s

    ​		Average fps of 1 evaluations: 95.32
    ​		The variance of 1 evaluations: 0.0

    
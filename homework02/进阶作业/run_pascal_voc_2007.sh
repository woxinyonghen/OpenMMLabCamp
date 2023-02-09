#!/bin/bash
# 加载模块
module load anaconda/2021.05
module load cuda/11.1
module load gcc/7.3

# 激活环境
source activate opennmmlab_mmdetection

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1
# 训练模型
python tools/train.py configs/pascal_voc_2007/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_pascal_voc2007.py --work-dir work/pascal_voc2007
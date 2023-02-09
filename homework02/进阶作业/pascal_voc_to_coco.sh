#!/bin/bash
# 加载模块
module load anaconda/2021.05
module load cuda/11.1
module load gcc/7.3

# 激活环境
source activate opennmmlab_mmdetection

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1

python tools/dataset_converters/pascal_voc.py /HOME/scz0ara/run/OpenMMLabCamp/homework2/mmdetection/data/VOCdevkit --out-dir ./data --out-format coco

#!/bin/bash
# 加载模块
module load anaconda/2021.05
module load cuda/11.3
module load gcc/9.3

# 激活环境
source activate opennmmlab_mmsegmentation

# 刷新⽇志缓存
export PYTHONUNBUFFERED=1

# 训练模型
python train_data.py
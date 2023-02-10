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
python tools/analysis_tools/benchmark.py configs/mouse_glomeruli/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024_mouse.py work/mouse_glomeruli/iter_800.pth
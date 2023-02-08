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
python demo/video_balloon.py --out result.mp4 test_video.mp4 configs/balloon/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_balloon.py work/balloon/best_bbox_mAP_epoch_95.pth
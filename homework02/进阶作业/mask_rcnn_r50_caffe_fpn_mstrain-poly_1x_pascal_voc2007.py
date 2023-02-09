# The new config inherits a base config to highlight the necessary modification
_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=20),
        mask_head=dict(num_classes=20)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
               'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
               'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train',
               'tvmonitor')
data_root = "/HOME/scz0ara/run/OpenMMLabCamp/homework2/mmdetection/data/VOCdevkit"

data = dict(
    train=dict(
        img_prefix=data_root,
        classes=classes,
        ann_file='data/voc07_train.json'),
    val=dict(
        img_prefix=data_root,
        classes=classes,
        ann_file='data/voc07_val.json'),
    test=dict(
        img_prefix=data_root,
        classes=classes,
        ann_file='data/voc07_val.json'))

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.001,
    step=[8, 11])

runner = dict(type='EpochBasedRunner', max_epochs=100)
checkpoint_config = dict(interval=10)
evaluation = dict(interval=1, metric='bbox', save_best='auto')

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
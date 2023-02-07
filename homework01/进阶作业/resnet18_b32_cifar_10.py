_base_ = ['../_base_/models/resnet18.py', '../_base_/datasets/imagenet_bs32.py', '../_base_/default_runtime.py']

model = dict(
    head=dict(
        num_classes=10,
        topk = (1, )
    ))

data = dict(
    samples_per_gpu = 32,
    workers_per_gpu=2,
    train = dict(
        data_prefix = 'data/cifar-10/train',
        ann_file = 'data/cifar-10/train.txt',
        classes = 'data/cifar-10/classes.txt'
),
    val = dict(
        data_prefix = 'data/cifar-10/val',
        ann_file = 'data/cifar-10/val.txt',
        classes = 'data/cifar-10/classes.txt'
    ),
)

optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

lr_config = dict(
    policy='step',
    step=[1])

runner = dict(type='EpochBasedRunner', max_epochs=100)

load_from ='/HOME/scz0ara/run/OpenMMLabCamp/homework1/mmclassification/checkpoints/resnet18_batch256_imagenet_20200708-34ab8f90.pth'
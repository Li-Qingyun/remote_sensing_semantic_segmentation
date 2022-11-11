_base_ = [
    '../_base_/models/fcn_r50-d8.py', '../_base_/datasets/potsdam-IRRG-all.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=5),
    auxiliary_head=dict(num_classes=5))

default_hook = dict(checkpoint=dict(interval=10000))

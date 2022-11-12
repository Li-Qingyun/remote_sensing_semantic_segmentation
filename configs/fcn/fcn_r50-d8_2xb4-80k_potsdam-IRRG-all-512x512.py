_base_ = [
    '../_base_/models/fcn_r50-d8.py', '../_base_/datasets/potsdam-IRRG-all.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_80k.py'
]
ignore_index = 5
crop_size = (512, 512)
data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=5, ignore_index=ignore_index),
    auxiliary_head=dict(num_classes=5, ignore_index=ignore_index))

default_hook = dict(checkpoint=dict(interval=10000))

_base_ = './potsdam.py'
# dataset settings
train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='img_IRRG/train', seg_map_path='ann_all/train')))
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='img_IRRG/val', seg_map_path='ann_all/val')))

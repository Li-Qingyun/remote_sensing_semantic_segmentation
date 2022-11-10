_base_ = './potsdam.py'
# dataset settings
ignore_index = 5
train_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='img_IRRG/train', seg_map_path='ann_all/train'),
        ignore_index=ignore_index))
val_dataloader = dict(
    dataset=dict(
        data_prefix=dict(
            img_path='img_IRRG/val', seg_map_path='ann_all/val')),
    ignore_index=ignore_index)
test_dataloader = val_dataloader
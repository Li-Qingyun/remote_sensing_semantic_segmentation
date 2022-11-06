# Remote Sensing Semantic Segmentation

Semantic segmentation on remote sensing data sets with the mmsegmentation of OpenMMLab 2.0.

Explore benchmark for comparison.

Personal maintenance and use.

### Support Dataset

- Potsdam

### Support Model

- 



## Prepare Env

```shell
# create env
conda create -n mmseg_rs python=3.8
conda activate mmseg_rs

# install pytorch
conda install -c pytorch pytorch torchvision
# or
pip3 install torch torchvision

# install mmseg of OpenMMLab 2.0
pip install openmim
mim install mmengine 'mmcv>=2.0.0rc0' 'mmsegmentation>=1.0.0rc0'
```



## Launch Experiments

Using [mim](https://github.com/open-mmlab/mim) to deal with experiments.

```shell
# training
mim train mmseg {config}  # train on single gpu
mim train mmseg {config} --cfg-options train_dataloader.batch_size=1  # modify cfg options
mim train mmseg {config} --gpus {num_gpus} --launcher pytorch  # train on distributed mode

# testing
mim test mmseg {config} --checkpoint {checkpont}  # test on single gpu
mim test mmseg {config} --checkpoint {checkpont} --gpus {num_gpus} --launcher pytorch  # test on distributed mode
```



## Results

| Segmentor | OA   | mFscore | mIoU |
| --------- | ---- | ------- | ---- |
|           |      |         |      |
|           |      |         |      |
|           |      |         |      |


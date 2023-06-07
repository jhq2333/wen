import sys
import torch
import wenetruntime as wenet
# 下载https://github.com/wenet-e2e/wenet/releases/download/v2.0.1/chs.tar.gz
# 并解压缩到/root/.wenet/chs目录下
decoder = wenet.Decoder(model_dir="/root/.wenet/chs/chs/",lang='chs')

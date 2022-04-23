# LightgGBM

## Installation

For Linux

```bash
git clone --recursive https://github.com/microsoft/LightGBM /tmp/LightGBM
cd /tmp/LightGBM
mkdir build
cd build
cmake ..
make -j4
```

GPU version: 未测试

```shell
git clone --recursive https://github.com/microsoft/LightGBM
cd LightGBM
mkdir build
cd build
cmake -DUSE_GPU=1 ..
# if you have installed NVIDIA CUDA to a customized location, you should specify paths to OpenCL headers and library like the following:
# cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=/usr/local/cuda/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=/usr/local/cuda/include/ ..
make -j4
```

### Python API

```shell
pip install lightgbm
```

## Links

- [lightgbm docs](https://lightgbm.readthedocs.io/en/latest/Quick-Start.html)
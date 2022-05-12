# kaggle

```bash
conda create -nkaggle python=3.8
conda activate kaggle

# for autogluon
pip3 install -U pip setuptools wheel
python3 -m pip install "mxnet_cu101<2.0.0, >=1.7.0"  # auto install cudatoolkit

pip install -r requirements.txt -i"https://pypi.tuna.tsinghua.edu.cn/simple/"

pip install umap-learn[plot]  # umap with plot

```

[cudf](https://github.com/rapidsai/cudf)

```bash
conda install -c rapidsai cudf
```


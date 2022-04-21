# kaggle

## APIs

```shell
pip install kaggle
```

[验证](https://github.com/Kaggle/kaggle-api#api-credentials)

```shell
kaggle competitions list
kaggle competitions download -c [COMPETITION]
kaggle competitions submit -c [COMPETITION] -f [FILE] -m [MESSAGE]
kaggle competitions submit -c [COMPETITION NAME] -f [FILE PATH]
kaggle competitions submissions -c [COMPETITION NAME]
```

```shell
kaggle datasets list -s [KEYWORD]  # search for datasets
kaggle datasets download -d [DATASET]

kaggle datasets init -p /path/to/dataset  # Create a folder containing the files you want to upload
# Add your dataset’s metadata to the generated file, datapackage.json
kaggle datasets create -p /path/to/dataset  # create the dataset
```

# Interacting with Notebooks

```shell
kaggle kernels list -s [KEYWORD]
kaggle kernels push -k [KERNEL] -p /path/to/kernel
kaggle kernels pull [KERNEL] -p /path/to/download -m  # download code files and metadata associated with a Notebook
```

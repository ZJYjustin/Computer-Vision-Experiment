# 实验三：图像关键点检测与图像拼接

- [中文实验报告](实验报告.md)
- [分步骤实验代码（已执行）](实验代码.ipynb)
- [原始 Notebook（保留原样）](code.ipynb)

## 目录

```text
3rd.exp/
├── README.md              # 导航和运行说明
├── 实验报告.md            # 原理、步骤、实测结果与分析
├── 实验代码.ipynb         # 从空白内核运行的整理版
├── code.ipynb             # 原始文件，供追溯
├── requirements.txt
├── img/                   # a.jpg、b.jpg
└── result/                # 历史结果及每次运行的新结果
```

## 运行

在 Anaconda Prompt 或 PowerShell 中，切换到仓库根目录，激活需要使用的 Python 环境后执行：

```powershell
python -m pip install -r 3rd.exp/requirements.txt
python -m jupyterlab
```

打开 `3rd.exp/实验代码.ipynb`，选择同一个 Python 环境的内核，执行“重启内核并运行全部单元格”。
也可以从 `3rd.exp` 目录启动，此时安装命令使用 `python -m pip install -r requirements.txt`。
如果缺少 `cv2.SIFT_create`，请确认选择了安装依赖的内核，并在该环境只保留一种 OpenCV 包。

无需重新下载图片或预先运行其他文件。Notebook 支持中文路径；读取不到图片时会提示检查启动目录。
全部运行约需数秒到几十秒，取决于设备。测试环境为 Python 3.14.6、OpenCV 4.13.0、NumPy 2.4.6、Matplotlib 3.11.0。

原始 `code.ipynb` 缺少起始读图和部分导入步骤，保留它用于追溯；日常运行使用整理版。

## 结果与复现

报告对应的验证结果为 `result/20261022-211351-749832/`，统计见该目录的 `metrics.json`。
每次运行新建目录，不改写旧图或报告。若调整输入或参数，可将新结果写入自己的新报告，保留当前记录。
OpenCV 固定随机种子与单线程计算减少波动，但不同版本或平台的 FLANN 匹配数仍可能略有不同。

本实验保留直接覆盖拼接，尚未进行曝光补偿或融合；调暗对照中的亮度接缝是实验观察内容。

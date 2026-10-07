# Computer-Vision-Experiment
## 实验目的：
 本实验旨在通过系统配置关键的开发环境与库，为深入探索计算机视觉领域做好必要准备。我们通过安装Anaconda来建立稳定的项目管理基础，以此作为安装核心组件的平台。继而，我们配置了PyTorch深度学习框架，旨在为后续实现复杂的图像识别模型提供核心支持；安装了OpenCV库以胜任基础的图像处理和视频分析任务；并引入了Scikit-learn工具包来补充传统机器学习算法能力。这套环境的成功搭建，标志着我们已经具备了开展从理论到实践的全流程计算机视觉学习与研究的先决条件。

## 实验内容：
### 1.安装anaconda：
<img width="1071" height="159" alt="2d9eb0769343b48291b1578b6eebc993" src="https://github.com/user-attachments/assets/9c45f7b9-6cfe-459f-aad6-d48b8669dfdd" />

### 2.创建虚拟环境 + 安装 OpenCV：
<img width="1272" height="453" alt="image" src="https://github.com/user-attachments/assets/a773b42b-3388-4bd2-bfd3-abfbb41dba97" />

### 3.CUDA Toolkit + cuDNN：
<img width="1452" height="369" alt="d9d6d0e7b642dffc1660700c429d0e18" src="https://github.com/user-attachments/assets/e168a791-58b5-4efa-9157-41a74b3405d7" />
PyTorch 预编译包已内置 CUDA runtime 与 cuDNN，无需单独安装。

### 4.安装 PyTorch GPU 版：
<img width="1095" height="78" alt="image" src="https://github.com/user-attachments/assets/8e4a6655-a072-4870-8c50-23e0e3ba8c4c" />

### 5.GPU 加速环境验证：
<img width="1425" height="660" alt="image" src="https://github.com/user-attachments/assets/e470338a-6b85-4adc-be68-cda3730b07c6" />

## 实验总结：
本次实验完成了计算机视觉实验环境的搭建。安装了 Anaconda 并熟悉了虚拟环境管理；在 PyCharm 中创建了 Python 虚拟环境并成功安装了 OpenCV 5.0.0；安装了 GPU 版 PyTorch（torch 2.14.1+cu126），该版本已内置对应 CUDA 12.6 的 runtime 与 cuDNN，无需单独安装 CUDA Toolkit；通过 torch.cuda.is_available() 验证结果为 True，torch.backends.cudnn.is_available() 同样可用，说明 GPU 加速环境配置成功，为后续计算机视觉实验的深层网络训练奠定了基础。

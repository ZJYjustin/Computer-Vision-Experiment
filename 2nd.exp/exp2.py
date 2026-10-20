import cv2
import numpy as np
from skimage.util import random_noise
from matplotlib import pyplot as plt

# 1. 读取原始图像
img = cv2.imread("p1.jpg")

# 检查图像是否读取成功
if img is None:
    raise FileNotFoundError("没有找到 p1.jpg，请检查图片路径和文件名")

# 2. 查看图像尺寸
print("图像尺寸（高、宽、通道）:", img.shape)

# 3. 获取 [100, 100] 位置的像素值
b, g, r = img[100, 100]
print("该像素的 BGR 值:", b, g, r)
print("该像素的 RGB 值:", r, g, b)

# 4. 将 BGR 转换为 RGB
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 5. 转换为灰度图
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 6. 显示原图和灰度图
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(rgb_img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray_img, cmap="gray")
plt.title("Gray Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# ==================== 添加噪声 ====================

# 添加椒盐噪声
sp_noise_img = random_noise(
    rgb_img,
    mode='s&p',
    amount=0.4
)
# 添加高斯噪声
gus_noise_img = random_noise(
    rgb_img,
    mode='gaussian',
    mean=0.2,
    var=0.03
)
# ==================== 显示噪声对比图 ====================
plt.figure(figsize=(12, 4))
# 原图
plt.subplot(1, 3, 1)
plt.imshow(rgb_img)
plt.title("Original Image")
plt.axis("off")
# 椒盐噪声图
plt.subplot(1, 3, 2)
plt.imshow(sp_noise_img)
plt.title("Salt & Pepper Noise")
plt.axis("off")
# 高斯噪声图
plt.subplot(1, 3, 3)
plt.imshow(gus_noise_img)
plt.title("Gaussian Noise")
plt.axis("off")

plt.tight_layout()
plt.show()


# ==================== 图像滤波 ====================

# 将噪声图像转换为 0~255 的 uint8 格式
sp_noise_u8 = (sp_noise_img * 255).clip(0, 255).astype(np.uint8)
gus_noise_u8 = (gus_noise_img * 255).clip(0, 255).astype(np.uint8)

# 1. 均值滤波
mean_sp = cv2.blur(sp_noise_u8, (5, 5))
mean_gus = cv2.blur(gus_noise_u8, (5, 5))

# 2. 中值滤波
mid_sp = cv2.medianBlur(sp_noise_u8, 5)
mid_gus = cv2.medianBlur(gus_noise_u8, 5)

# 3. 高斯滤波
gauss_sp = cv2.GaussianBlur(sp_noise_u8, (5, 5), 0)
gauss_gus = cv2.GaussianBlur(gus_noise_u8, (5, 5), 0)

# ==================== 显示滤波对比图 ====================

plt.figure(figsize=(14, 8))

# 第一行：椒盐噪声
plt.subplot(2, 3, 1)
plt.imshow(mean_sp)
plt.title("S&P Noise - Mean Filter")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(mid_sp)
plt.title("S&P Noise - Median Filter")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(gauss_sp)
plt.title("S&P Noise - Gaussian Filter")
plt.axis("off")

# 第二行：高斯噪声
plt.subplot(2, 3, 4)
plt.imshow(mean_gus)
plt.title("Gaussian Noise - Mean Filter")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(mid_gus)
plt.title("Gaussian Noise - Median Filter")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(gauss_gus)
plt.title("Gaussian Noise - Gaussian Filter")
plt.axis("off")

plt.tight_layout()
plt.savefig("filter_comparison.png", dpi=300, bbox_inches="tight")
plt.show()



# ==================== 手动实现中值滤波 ====================

def manual_median_filter_color(image, kernel_size=5):
    # 计算窗口向外扩展的像素数量
    pad = kernel_size // 2

    # 创建与原图形状相同的空图像
    filtered_img = np.zeros_like(image)

    # 对 B、G、R 三个通道分别处理
    for c in range(3):
        channel = image[:, :, c]

        # 对图像边缘进行填充
        padded_channel = np.pad(
            channel,
            pad_width=pad,
            mode="edge"
        )

        # 遍历图像中的每一个像素
        for i in range(channel.shape[0]):
            for j in range(channel.shape[1]):

                # 提取当前像素周围的 5×5 窗口
                region = padded_channel[
                    i:i + kernel_size,
                    j:j + kernel_size
                ]

                # 计算窗口内像素的中位数
                filtered_img[i, j, c] = np.median(region)

    return filtered_img


# 对椒盐噪声图像进行手动中值滤波
manual_mid = manual_median_filter_color(
    sp_noise_u8,
    kernel_size=5
)

# ==================== 显示处理前后的对比 ====================

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(sp_noise_u8)
plt.title("Salt & Pepper Noise")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(manual_mid)
plt.title("Manual Median Filter")
plt.axis("off")

plt.tight_layout()
plt.savefig(
    "manual_median_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

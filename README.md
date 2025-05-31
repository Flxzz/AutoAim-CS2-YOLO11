# AutoAim-CS2-YOLO11

> 🎯 基于 YOLOv11 的 CS2 实时敌人检测与自动瞄准项目

---

## 📌 项目简介

本项目基于 YOLOv11 实现了对 CS2 游戏中敌人的实时检测，并结合控制逻辑实现自动将准心移动到敌人位置，从而辅助瞄准，提升游戏精准度与反应速度。

---

## 🚀 项目功能

- 使用训练后的 YOLOv11 模型对游戏画面中的敌人进行实时检测  
- 自动将鼠标瞄准到检测到的敌人位置  
- 支持可视化预测结果，便于调试与演示  
- 支持自定义检测区域与灵敏度配置

---


## 🧩 使用说明

### ✅ 环境安装

建议使用 Python 3.10+，安装依赖：

```bash
pip install -r requirements.txt  # 若你未写，可使用 pip install 逐个安装
```

### ✅ 配置

- 修改 `config.yaml` 文件中的 `screen_region`，设定你希望检测的屏幕区域  
- 设置系统鼠标速度为 10（暂时为硬编码，未来可优化）

### ✅ 运行

```bash
python main.py
```

如需运行带可视化窗口的版本（推荐调试时使用）：

```bash
python visial.py
```

---

## 📷 项目演示

![AWP](E:\projects\CS_YOLO_AimEnemy\media\AWP.gif)

![M4](E:\projects\CS_YOLO_AimEnemy\media\M4.gif)

---

## 📊 训练数据说明

- 本项目训练数据来自游戏实战录屏，抽帧提取约 300 张图片  
- 在 Roboflow 平台进行标注、扩增后生成约 1000 张数据  


---

## 📄 License

本项目仅供学习与研究使用，禁止用于任何违反游戏条款的行为。

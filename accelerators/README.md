# 加速卡适配层 | Accelerator Adapters

本目录包含对各种AI加速卡的适配实现，提供统一的硬件抽象层。

## 🎯 设计目标

1. **硬件抽象**：屏蔽不同加速卡的底层差异
2. **性能优化**：针对不同硬件特性进行优化
3. **易于扩展**：便于添加新的加速卡支持
4. **国产化支持**：重点支持国产AI芯片

## 📁 目录结构

### nvidia/
Nvidia GPU 适配实现（完全支持）。

**支持型号：**
- A100/A800 (80GB/40GB)
- H100/H800
- L40S
- RTX 4090/3090

**子目录：**
- `cuda/` - CUDA 相关实现
- `triton/` - Triton 自定义内核

### hygon/
海光 DCU 适配实现（适配中）。

**支持型号：**
- 海光 Z100
- 海光 K100
- 海光 K100-AI
- 海光 BW1000

**技术栈：** ROCm

**子目录：**
- `dcu/` - DCU 相关实现

### ascend/
华为昇腾适配实现（适配中）。

**支持型号：**
- 昇腾 910B
- 昇腾 310P

**技术栈：** CANN (Compute Architecture for Neural Networks)

**子目录：**
- `cann/` - CANN 相关实现

### cambricon/
寒武纪 MLU 适配实现（适配中）。

**支持型号：**
- 寒武纪 MLU370
- 寒武纪 MLU590

**技术栈：** BANG (Basic Algebra Next Generation)

**子目录：**
- `mlu/` - MLU 相关实现

### common/
通用硬件抽象层。

**内容：**
- `interface.py` - 硬件接口定义
- `factory.py` - 硬件工厂类
- `utils.py` - 通用工具函数

## 🔧 使用示例

```python
from accelerators.common.factory import AcceleratorFactory

# 自动检测并创建加速卡实例
accelerator = AcceleratorFactory.create_auto()

# 或指定特定加速卡
accelerator = AcceleratorFactory.create("nvidia")

# 获取硬件信息
info = accelerator.get_device_info()
print(f"设备: {info.name}")
print(f"显存: {info.memory_total} GB")
print(f"计算能力: {info.compute_capability}")

# 内存管理
accelerator.allocate_memory(size_gb=20)
accelerator.clear_cache()
```

## 📊 硬件对比

| 加速卡 | 显存 | 算力(FP16) | 功耗 | 适配状态 |
|--------|------|------------|------|---------|
| Nvidia A100 | 80GB | 312 TFLOPS | 400W | ✅ 完全支持 |
| Nvidia H100 | 80GB | 1000 TFLOPS | 700W | ✅ 完全支持 |
| 海光 Z100 | 64GB | 180 TFLOPS | 350W | 🚧 适配中 |
| 昇腾 910B | 64GB | 256 TFLOPS | 310W | 🚧 适配中 |
| 寒武纪 MLU370 | 32GB | 128 TFLOPS | 250W | 🚧 适配中 |

## 🚀 适配进度

### Q1 2026
- [x] Nvidia GPU 完全支持
- [ ] 海光 DCU 基础功能
- [ ] 昇腾基础功能

### Q2 2026
- [ ] 海光 DCU 优化
- [ ] 昇腾优化
- [ ] 寒武纪基础功能

### Q3 2026
- [ ] 所有硬件性能对齐
- [ ] 自动调优工具
- [ ] 混合精度优化

## 📝 适配指南

如需添加新的加速卡支持，请参考：
1. 实现 `common/interface.py` 中定义的接口
2. 在 `common/factory.py` 中注册新的加速卡
3. 编写单元测试和性能测试
4. 更新文档和示例


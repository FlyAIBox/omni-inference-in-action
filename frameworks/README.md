# 推理框架 | Inference Frameworks

本目录包含对主流大模型推理框架的封装和适配。

## 🎯 设计目标

1. **统一接口**：为不同推理框架提供统一的调用接口
2. **硬件适配**：支持多种加速卡的无缝切换
3. **性能优化**：针对不同场景进行性能调优
4. **易于扩展**：便于添加新的推理框架支持

## 📁 目录结构

### vllm/
vLLM 推理框架的封装实现。

**特点：**
- PagedAttention 内存管理
- 连续批处理
- 高吞吐量优化

**子目录：**
- `engines/` - 推理引擎实现
- `schedulers/` - 请求调度器
- `adapters/` - 硬件适配器

### sglang/
SGLang 推理框架的封装实现。

**特点：**
- 结构化生成语言
- 高效的运行时调度
- 灵活的控制流

**子目录：**
- `runtime/` - 运行时实现
- `backends/` - 后端引擎
- `adapters/` - 硬件适配器

### common/
通用组件和工具。

**内容：**
- `interfaces/` - 统一接口定义
- `utils/` - 工具函数
- `monitoring/` - 监控组件

## 🔧 使用示例

```python
from frameworks.common.interfaces import InferenceEngine

# 创建推理引擎
engine = InferenceEngine.create(
    framework="vllm",
    model_name="Qwen/Qwen2-7B",
    accelerator="nvidia"
)

# 执行推理
response = engine.generate(
    prompt="你好，请介绍一下自己",
    max_tokens=100
)
```

## 📊 框架对比

| 特性 | vLLM | SGLang |
|------|------|--------|
| 吞吐量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| 延迟 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 灵活性 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 易用性 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

## 🚀 后续计划

- [ ] 支持 TensorRT-LLM
- [ ] 支持 LMDeploy
- [ ] 优化批处理策略
- [ ] 添加自适应调度


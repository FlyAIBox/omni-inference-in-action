# 示例代码 | Examples

本目录包含各种使用场景的示例代码，帮助快速上手和理解项目。

## 📁 目录结构

### basic/
基础示例，适合初学者。

**内容包括：**
- 模型加载和初始化
- 简单文本生成
- 批量推理
- 流式输出
- 参数配置

### advanced/
高级示例，展示复杂功能。

**内容包括：**
- 多轮对话管理
- 自定义采样策略
- 并发请求处理
- 性能监控
- 错误处理

### production/
生产环境示例，展示实际部署方案。

**内容包括：**
- API服务部署
- 负载均衡
- 日志监控
- 容错机制
- 自动扩缩容

## 🚀 快速开始

### 1. 基础文本生成

```python
from frameworks.vllm import VLLMEngine

# 初始化引擎
engine = VLLMEngine(
    model_name="Qwen/Qwen2-7B",
    tensor_parallel_size=1
)

# 生成文本
prompt = "请介绍一下人工智能的发展历史"
output = engine.generate(
    prompt=prompt,
    max_tokens=200,
    temperature=0.7
)

print(output.text)
```

### 2. 流式输出

```python
from frameworks.vllm import VLLMEngine

engine = VLLMEngine(model_name="Qwen/Qwen2-7B")

prompt = "写一篇关于春天的散文"

for token in engine.generate_stream(prompt=prompt, max_tokens=200):
    print(token, end="", flush=True)
```

### 3. 批量推理

```python
from frameworks.vllm import VLLMEngine

engine = VLLMEngine(model_name="Qwen/Qwen2-7B")

prompts = [
    "什么是机器学习？",
    "什么是深度学习？",
    "什么是强化学习？"
]

outputs = engine.generate_batch(
    prompts=prompts,
    max_tokens=100
)

for prompt, output in zip(prompts, outputs):
    print(f"Q: {prompt}")
    print(f"A: {output.text}\n")
```

### 4. API服务

```python
from fastapi import FastAPI
from frameworks.vllm import VLLMEngine

app = FastAPI()
engine = VLLMEngine(model_name="Qwen/Qwen2-7B")

@app.post("/generate")
async def generate(prompt: str, max_tokens: int = 100):
    output = engine.generate(
        prompt=prompt,
        max_tokens=max_tokens
    )
    return {"text": output.text}

# 启动服务
# uvicorn api:app --host 0.0.0.0 --port 8000
```

## 📖 示例列表

### Basic Examples
- `basic/01_simple_generation.py` - 简单文本生成
- `basic/02_stream_generation.py` - 流式输出
- `basic/03_batch_inference.py` - 批量推理
- `basic/04_parameter_tuning.py` - 参数调优
- `basic/05_model_comparison.py` - 模型对比

### Advanced Examples
- `advanced/01_multi_turn_chat.py` - 多轮对话
- `advanced/02_custom_sampling.py` - 自定义采样
- `advanced/03_concurrent_requests.py` - 并发处理
- `advanced/04_monitoring.py` - 性能监控
- `advanced/05_error_handling.py` - 错误处理

### Production Examples
- `production/01_api_server.py` - API服务
- `production/02_load_balancing.py` - 负载均衡
- `production/03_logging.py` - 日志系统
- `production/04_health_check.py` - 健康检查
- `production/05_auto_scaling.py` - 自动扩缩容

## 🎯 最佳实践

### 1. 模型加载优化
```python
# 使用预加载减少首次推理延迟
engine = VLLMEngine(
    model_name="Qwen/Qwen2-7B",
    tensor_parallel_size=2,
    max_model_len=4096,
    gpu_memory_utilization=0.90  # 提高GPU利用率
)
```

### 2. 批处理优化
```python
# 动态批处理提高吞吐量
outputs = engine.generate_batch(
    prompts=prompts,
    max_tokens=100,
    use_beam_search=False,  # 关闭束搜索加速
    temperature=0.7
)
```

### 3. 并发控制
```python
import asyncio
from frameworks.vllm import VLLMEngine

async def process_request(engine, prompt):
    return await engine.generate_async(prompt)

async def main():
    engine = VLLMEngine(model_name="Qwen/Qwen2-7B")
    
    tasks = [
        process_request(engine, prompt)
        for prompt in prompts
    ]
    
    results = await asyncio.gather(*tasks)
    return results
```

## 📞 获取帮助

如果在使用示例时遇到问题：
1. 查看相关文档
2. 在 [Issues](https://github.com/your-org/omni-inference-in-action/issues) 中搜索
3. 创建新的 Issue 提问


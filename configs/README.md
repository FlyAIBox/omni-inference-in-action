# 配置文件 | Configuration Files

本目录包含项目各个组件的配置文件模板和示例。

## 📁 目录结构

### models/
模型配置文件。

**配置内容：**
- 模型路径和版本
- 模型参数设置
- 量化配置
- 特殊token配置

### servers/
服务器配置文件。

**配置内容：**
- API服务配置
- 并发和超时设置
- 日志配置
- 安全设置

### hardware/
硬件配置文件。

**配置内容：**
- GPU/加速卡配置
- 显存分配策略
- 张量并行配置
- 通信优化

### applications/
应用场景配置文件。

**配置内容：**
- 场景特定参数
- 业务逻辑配置
- 数据处理配置

## 📝 配置文件格式

我们使用 YAML 格式作为主要配置文件格式，清晰易读。

### 模型配置示例

```yaml
# configs/models/qwen2-7b.yaml
model:
  name: "Qwen/Qwen2-7B"
  revision: "main"
  trust_remote_code: true
  
  # 模型加载配置
  loading:
    dtype: "float16"  # float16, bfloat16, float32
    quantization: null  # awq, gptq, null
    max_model_len: 4096
    
  # 生成参数
  generation:
    temperature: 0.7
    top_p: 0.9
    top_k: 50
    max_tokens: 2048
    repetition_penalty: 1.1
    
  # 特殊token
  special_tokens:
    bos_token: "<|im_start|>"
    eos_token: "<|im_end|>"
    pad_token: "<|endoftext|>"
```

### 服务器配置示例

```yaml
# configs/servers/api_server.yaml
server:
  host: "0.0.0.0"
  port: 8000
  workers: 4
  
  # 并发配置
  concurrency:
    max_concurrent_requests: 100
    request_timeout: 300  # 秒
    max_queue_size: 1000
    
  # 日志配置
  logging:
    level: "INFO"  # DEBUG, INFO, WARNING, ERROR
    format: "json"
    output: "logs/server.log"
    rotation: "100 MB"
    
  # API配置
  api:
    enable_cors: true
    api_key_required: false
    rate_limit: 100  # 每分钟请求数
    
  # 监控配置
  monitoring:
    enable_prometheus: true
    prometheus_port: 9090
    enable_health_check: true
    health_check_interval: 30  # 秒
```

### 硬件配置示例

```yaml
# configs/hardware/nvidia_a100.yaml
hardware:
  type: "nvidia"
  device_ids: [0, 1, 2, 3]
  
  # 并行配置
  parallelism:
    tensor_parallel_size: 2
    pipeline_parallel_size: 1
    
  # 显存配置
  memory:
    gpu_memory_utilization: 0.90
    max_num_seqs: 256
    max_num_batched_tokens: 8192
    
  # 性能优化
  optimization:
    enable_cuda_graph: true
    enable_prefix_caching: true
    swap_space: 4  # GB
    
  # CUDA配置
  cuda:
    cuda_visible_devices: "0,1,2,3"
    nccl_socket_ifname: "eth0"
```

### 应用配置示例

```yaml
# configs/applications/chatbot.yaml
application:
  name: "customer_service_bot"
  type: "chatbot"
  
  # 对话配置
  conversation:
    max_turns: 10
    context_window: 4096
    system_prompt: "你是一个专业的客服助手..."
    
  # 知识库配置
  knowledge_base:
    enabled: true
    type: "vector_db"
    index_path: "data/kb_index"
    top_k: 3
    
  # 安全配置
  safety:
    enable_content_filter: true
    sensitive_word_list: "configs/sensitive_words.txt"
    max_output_length: 500
    
  # 业务配置
  business:
    enable_intent_recognition: true
    enable_sentiment_analysis: true
    fallback_response: "抱歉，我没有理解您的问题..."
```

## 🔧 使用配置

### Python 代码中加载配置

```python
import yaml
from pathlib import Path

def load_config(config_path: str) -> dict:
    """加载配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

# 使用示例
model_config = load_config("configs/models/qwen2-7b.yaml")
server_config = load_config("configs/servers/api_server.yaml")

# 访问配置
model_name = model_config['model']['name']
server_port = server_config['server']['port']
```

### 命令行指定配置

```bash
# 使用默认配置
python main.py

# 指定配置文件
python main.py --config configs/production.yaml

# 覆盖特定配置项
python main.py \
    --config configs/production.yaml \
    --model.name Qwen2-14B \
    --server.port 8080
```

## 📋 配置模板

### 开发环境配置
```yaml
# configs/environments/development.yaml
environment: "development"
debug: true

model:
  name: "Qwen/Qwen2-7B"
  dtype: "float16"

server:
  host: "127.0.0.1"
  port: 8000
  workers: 1

hardware:
  device_ids: [0]
  gpu_memory_utilization: 0.80
```

### 生产环境配置
```yaml
# configs/environments/production.yaml
environment: "production"
debug: false

model:
  name: "Qwen/Qwen2-7B"
  dtype: "float16"
  quantization: "awq"

server:
  host: "0.0.0.0"
  port: 8000
  workers: 4

hardware:
  device_ids: [0, 1, 2, 3]
  gpu_memory_utilization: 0.95
  tensor_parallel_size: 4

monitoring:
  enable_prometheus: true
  enable_logging: true
  log_level: "WARNING"
```

## 🔒 安全配置

### 敏感信息处理

不要在配置文件中直接存储敏感信息，使用环境变量：

```yaml
# configs/servers/secure.yaml
server:
  api_key: ${API_KEY}  # 从环境变量读取
  
database:
  host: ${DB_HOST}
  password: ${DB_PASSWORD}
```

加载时替换环境变量：

```python
import os
import re

def load_config_with_env(config_path: str) -> dict:
    with open(config_path, 'r') as f:
        content = f.read()
    
    # 替换环境变量
    pattern = r'\$\{([^}]+)\}'
    def replace_env(match):
        env_var = match.group(1)
        return os.getenv(env_var, match.group(0))
    
    content = re.sub(pattern, replace_env, content)
    return yaml.safe_load(content)
```

## ✅ 配置验证

### 配置校验脚本

```python
from pydantic import BaseModel, validator

class ModelConfig(BaseModel):
    name: str
    dtype: str
    max_model_len: int
    
    @validator('dtype')
    def validate_dtype(cls, v):
        allowed = ['float16', 'bfloat16', 'float32']
        if v not in allowed:
            raise ValueError(f'dtype must be one of {allowed}')
        return v

# 使用示例
config_data = load_config('configs/models/qwen2-7b.yaml')
model_config = ModelConfig(**config_data['model'])
```

## 📞 获取帮助

如有配置相关问题：
1. 查看示例配置文件
2. 查看相关文档
3. 在 Issues 中提问


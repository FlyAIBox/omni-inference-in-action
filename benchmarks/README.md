# 性能测试 | Performance Benchmarks

本目录包含各种场景下的性能基准测试代码和结果。

## 🎯 测试目标

1. **延迟测试**：评估推理响应时间
2. **吞吐量测试**：评估系统处理能力
3. **显存占用测试**：评估内存使用效率
4. **对比分析**：不同框架和硬件的性能对比

## 📁 目录结构

### latency/
延迟测试相关代码和结果。

**测试指标：**
- 首Token延迟 (Time to First Token, TTFT)
- 每Token延迟 (Time per Output Token, TPOT)
- 端到端延迟 (End-to-End Latency)

### throughput/
吞吐量测试相关代码和结果。

**测试指标：**
- 每秒处理请求数 (Requests per Second, RPS)
- 每秒生成Token数 (Tokens per Second, TPS)
- 并发处理能力

### memory/
显存占用测试相关代码和结果。

**测试指标：**
- 模型加载显存
- 推理时显存峰值
- KV Cache 显存占用
- 批处理显存效率

### reports/
性能测试报告和分析。

**报告内容：**
- 测试环境描述
- 测试方法说明
- 测试数据和图表
- 结论和建议

## 🔧 运行测试

### 延迟测试
```bash
python benchmarks/latency/benchmark_latency.py \
    --model Qwen2-7B \
    --framework vllm \
    --accelerator nvidia \
    --num_requests 1000
```

### 吞吐量测试
```bash
python benchmarks/throughput/benchmark_throughput.py \
    --model Qwen2-7B \
    --framework vllm \
    --accelerator nvidia \
    --concurrent_requests 100
```

### 显存测试
```bash
python benchmarks/memory/benchmark_memory.py \
    --model Qwen2-7B \
    --framework vllm \
    --accelerator nvidia \
    --batch_sizes 1,4,8,16,32
```

## 📊 基准测试结果

### Qwen2-7B 性能对比

| 框架 | 硬件 | TTFT (ms) | TPOT (ms) | TPS | 显存 (GB) |
|------|------|-----------|-----------|-----|----------|
| vLLM | A100 | 待测试 | 待测试 | 待测试 | 待测试 |
| vLLM | H100 | 待测试 | 待测试 | 待测试 | 待测试 |
| SGLang | A100 | 待测试 | 待测试 | 待测试 | 待测试 |
| vLLM | 昇腾910B | 待测试 | 待测试 | 待测试 | 待测试 |

*注：详细报告请查看 `reports/` 目录*

## 🧪 测试环境

### 标准测试配置
- **输入长度**：512 tokens
- **输出长度**：128 tokens
- **批处理大小**：1, 4, 8, 16, 32
- **并发请求数**：1, 10, 50, 100
- **测试轮数**：3轮取平均值

### 测试数据集
- ShareGPT 数据集
- 自定义领域数据集
- 压力测试数据集

## 📈 性能优化建议

基于测试结果，我们提供以下优化建议：

1. **延迟优化**
   - 减少首Token延迟：使用预热、优化模型加载
   - 减少每Token延迟：使用量化、优化计算kernel

2. **吞吐量优化**
   - 增加批处理大小
   - 使用连续批处理（Continuous Batching）
   - 优化调度策略

3. **显存优化**
   - 使用PagedAttention
   - 应用量化技术
   - 优化KV Cache管理

## 🚀 持续更新

我们会持续更新性能测试结果，跟踪最新的优化技术。


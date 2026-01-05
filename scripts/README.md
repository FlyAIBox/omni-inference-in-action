# 工具脚本 | Utility Scripts

本目录包含项目开发、部署和运维相关的工具脚本。

## 📁 目录结构

### setup/
环境设置相关脚本。

**脚本列表：**
- `install_dependencies.sh` - 安装项目依赖
- `setup_vllm.sh` - 安装和配置 vLLM
- `setup_sglang.sh` - 安装和配置 SGLang
- `setup_nvidia.sh` - 配置 Nvidia GPU 环境
- `setup_hygon.sh` - 配置海光 DCU 环境
- `setup_ascend.sh` - 配置昇腾环境
- `setup_cambricon.sh` - 配置寒武纪环境

### deployment/
部署相关脚本。

**脚本列表：**
- `build_docker.sh` - 构建 Docker 镜像
- `deploy_k8s.sh` - 部署到 Kubernetes
- `deploy_local.sh` - 本地部署
- `update_service.sh` - 更新服务
- `rollback_service.sh` - 回滚服务

### monitoring/
监控相关脚本。

**脚本列表：**
- `monitor_gpu.py` - GPU 监控
- `monitor_service.py` - 服务监控
- `collect_metrics.py` - 指标收集
- `alert_manager.py` - 告警管理
- `generate_report.py` - 生成报告

### optimization/
优化相关脚本。

**脚本列表：**
- `profile_model.py` - 模型性能分析
- `tune_parameters.py` - 参数调优
- `optimize_memory.py` - 显存优化
- `benchmark_configs.py` - 配置基准测试

## 🚀 使用指南

### 环境设置

#### 1. 安装基础依赖
```bash
bash scripts/setup/install_dependencies.sh
```

#### 2. 配置推理框架
```bash
# 安装 vLLM
bash scripts/setup/setup_vllm.sh

# 或安装 SGLang
bash scripts/setup/setup_sglang.sh
```

#### 3. 配置加速卡
```bash
# Nvidia GPU
bash scripts/setup/setup_nvidia.sh

# 海光 DCU
bash scripts/setup/setup_hygon.sh

# 昇腾
bash scripts/setup/setup_ascend.sh

# 寒武纪
bash scripts/setup/setup_cambricon.sh
```

### 部署

#### 1. Docker 部署
```bash
# 构建镜像
bash scripts/deployment/build_docker.sh \
    --framework vllm \
    --accelerator nvidia \
    --tag v1.0.0

# 运行容器
docker run -d --gpus all \
    -p 8000:8000 \
    omni-inference:v1.0.0
```

#### 2. Kubernetes 部署
```bash
# 部署到 K8s 集群
bash scripts/deployment/deploy_k8s.sh \
    --namespace inference \
    --replicas 3 \
    --config configs/production.yaml

# 查看状态
kubectl get pods -n inference

# 扩缩容
kubectl scale deployment inference-server \
    --replicas=5 -n inference
```

#### 3. 本地部署
```bash
# 启动服务
bash scripts/deployment/deploy_local.sh \
    --model Qwen2-7B \
    --port 8000 \
    --gpu-ids 0,1
```

### 监控

#### 1. GPU 监控
```bash
# 实时监控 GPU 使用情况
python scripts/monitoring/monitor_gpu.py \
    --interval 5 \
    --output logs/gpu_metrics.log
```

#### 2. 服务监控
```bash
# 监控服务状态和性能
python scripts/monitoring/monitor_service.py \
    --url http://localhost:8000 \
    --interval 10 \
    --alert-threshold 1000  # 延迟阈值(ms)
```

#### 3. 指标收集
```bash
# 收集和存储性能指标
python scripts/monitoring/collect_metrics.py \
    --prometheus-url http://localhost:9090 \
    --output metrics/
```

### 优化

#### 1. 性能分析
```bash
# 分析模型性能瓶颈
python scripts/optimization/profile_model.py \
    --model Qwen2-7B \
    --framework vllm \
    --output reports/profile.html
```

#### 2. 参数调优
```bash
# 自动调优推理参数
python scripts/optimization/tune_parameters.py \
    --model Qwen2-7B \
    --objective latency  # 或 throughput
    --trials 100
```

#### 3. 显存优化
```bash
# 分析和优化显存使用
python scripts/optimization/optimize_memory.py \
    --model Qwen2-7B \
    --target-memory 40  # GB
    --strategies quantization,paged_attention
```

## 📊 常用命令

### 快速诊断
```bash
# 检查环境配置
bash scripts/setup/check_environment.sh

# 测试推理服务
curl -X POST http://localhost:8000/generate \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Hello", "max_tokens": 100}'

# 查看服务日志
docker logs -f inference-server

# 查看 K8s 日志
kubectl logs -f deployment/inference-server -n inference
```

### 性能测试
```bash
# 压力测试
python scripts/optimization/benchmark_configs.py \
    --url http://localhost:8000 \
    --concurrent-users 100 \
    --duration 300  # 秒
```

## ⚠️ 注意事项

1. **权限要求**：某些脚本需要 sudo 权限
2. **环境变量**：确保设置了必要的环境变量
3. **依赖检查**：运行前检查依赖是否安装
4. **配置验证**：部署前验证配置文件
5. **备份数据**：重要操作前备份数据

## 🔧 自定义脚本

你可以基于现有脚本创建自定义脚本：

```bash
# 复制模板
cp scripts/setup/template.sh scripts/setup/my_script.sh

# 编辑脚本
vim scripts/setup/my_script.sh

# 添加执行权限
chmod +x scripts/setup/my_script.sh

# 运行
bash scripts/setup/my_script.sh
```

## 📞 获取帮助

如果脚本运行出现问题：
1. 查看脚本内的帮助信息：`bash script.sh --help`
2. 查看日志文件
3. 在 Issues 中提问


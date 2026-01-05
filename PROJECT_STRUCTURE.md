# 项目结构说明 | Project Structure

## 📂 完整目录结构

```
omni-inference-in-action/
├── README.md                    # 项目主文档
├── LICENSE                      # 开源协议
├── CONTRIBUTING.md              # 贡献指南
├── PROJECT_STRUCTURE.md         # 本文件 - 项目结构说明
├── requirements.txt             # Python依赖列表
├── setup.py                     # 安装配置
├── .gitignore                   # Git忽略配置
│
├── docs/                        # 📚 文档
│   ├── README.md
│   ├── getting-started/        # 快速入门
│   ├── deployment/             # 部署指南
│   │   ├── docker/
│   │   ├── kubernetes/
│   │   └── bare-metal/
│   ├── benchmarks/             # 性能测试文档
│   ├── tutorials/              # 教程
│   │   ├── vllm/
│   │   ├── sglang/
│   │   └── optimization/
│   └── api/                    # API文档
│
├── frameworks/                  # 🔧 推理框架
│   ├── README.md
│   ├── vllm/                   # vLLM框架封装
│   │   ├── engines/           # 推理引擎
│   │   ├── schedulers/        # 调度器
│   │   └── adapters/          # 硬件适配器
│   ├── sglang/                 # SGLang框架封装
│   │   ├── runtime/           # 运行时
│   │   ├── backends/          # 后端实现
│   │   └── adapters/          # 硬件适配器
│   └── common/                 # 通用组件
│       ├── interfaces/        # 统一接口
│       ├── utils/             # 工具函数
│       └── monitoring/        # 监控组件
│
├── accelerators/                # 🎮 加速卡适配
│   ├── README.md
│   ├── nvidia/                 # Nvidia GPU
│   │   ├── cuda/
│   │   └── triton/
│   ├── hygon/                  # 海光DCU
│   │   └── dcu/
│   ├── ascend/                 # 华为昇腾
│   │   └── cann/
│   ├── cambricon/              # 寒武纪MLU
│   │   └── mlu/
│   └── common/                 # 通用硬件抽象层
│
├── applications/                # 🏢 行业应用
│   ├── README.md
│   ├── internet/               # 互联网场景
│   │   ├── chatbot/           # 智能客服
│   │   ├── content-generation/ # 内容生成
│   │   └── search/            # 智能搜索
│   ├── education/              # 科教场景
│   │   ├── tutoring/          # 智能辅导
│   │   ├── assessment/        # 智能评测
│   │   └── knowledge-graph/   # 知识图谱
│   ├── finance/                # 金融场景
│   │   ├── risk-control/      # 风险控制
│   │   ├── advisory/          # 智能投顾
│   │   └── compliance/        # 合规审查
│   └── healthcare/             # 医疗场景
│       ├── diagnosis/         # 辅助诊断
│       ├── medical-record/    # 病历分析
│       └── drug-discovery/    # 药物研发
│
├── examples/                    # 💡 示例代码
│   ├── README.md
│   ├── basic/                  # 基础示例
│   ├── advanced/               # 高级示例
│   └── production/             # 生产环境示例
│
├── benchmarks/                  # 📊 性能测试
│   ├── README.md
│   ├── latency/                # 延迟测试
│   ├── throughput/             # 吞吐量测试
│   ├── memory/                 # 显存测试
│   └── reports/                # 测试报告
│
├── scripts/                     # 🛠️ 工具脚本
│   ├── README.md
│   ├── setup/                  # 环境设置
│   ├── deployment/             # 部署脚本
│   ├── monitoring/             # 监控脚本
│   └── optimization/           # 优化工具
│
├── configs/                     # ⚙️ 配置文件
│   ├── README.md
│   ├── models/                 # 模型配置
│   ├── servers/                # 服务器配置
│   ├── hardware/               # 硬件配置
│   └── applications/           # 应用配置
│
├── tests/                       # 🧪 测试代码
│   ├── unit/                   # 单元测试
│   ├── integration/            # 集成测试
│   └── e2e/                    # 端到端测试
│
├── docker/                      # 🐳 Docker相关
│   ├── base/                   # 基础镜像
│   ├── frameworks/             # 框架镜像
│   └── applications/           # 应用镜像
│
└── kubernetes/                  # ☸️ K8s配置
    ├── deployments/            # Deployment配置
    ├── services/               # Service配置
    └── helm/                   # Helm Charts
```

## 🎯 核心模块说明

### 1. 推理框架层 (frameworks/)
**目的：** 封装和适配主流推理框架

**关键组件：**
- `vllm/` - 高吞吐量推理框架
- `sglang/` - 结构化生成语言框架
- `common/` - 统一接口和工具

**下一步工作：**
- [ ] 实现统一的推理接口
- [ ] 封装 vLLM 核心功能
- [ ] 封装 SGLang 核心功能
- [ ] 添加性能监控组件

### 2. 加速卡适配层 (accelerators/)
**目的：** 支持多种AI加速卡

**支持硬件：**
- Nvidia GPU (CUDA) - ✅ 优先级最高
- 海光DCU (ROCm) - 🔄 第二批
- 昇腾 (CANN) - 🔄 第二批
- 寒武纪MLU (BANG) - 🔄 第三批

**下一步工作：**
- [ ] 定义统一硬件接口
- [ ] 实现 Nvidia GPU 适配
- [ ] 添加硬件检测和自动配置
- [ ] 国产芯片逐步适配

### 3. 行业应用层 (applications/)
**目的：** 提供场景化解决方案

**应用场景：**
- 互联网：客服、内容生成、搜索
- 科教：辅导、评测、知识图谱
- 金融：风控、投顾、合规
- 医疗：诊断、病历、药物研发

**下一步工作：**
- [ ] 开发互联网场景demo
- [ ] 开发科教场景demo
- [ ] 收集行业最佳实践
- [ ] 编写场景化文档

### 4. 示例代码 (examples/)
**目的：** 帮助用户快速上手

**示例分类：**
- Basic：入门级示例
- Advanced：高级功能示例
- Production：生产环境示例

**下一步工作：**
- [ ] 编写基础使用示例
- [ ] 编写高级功能示例
- [ ] 编写部署实战示例
- [ ] 添加详细注释

### 5. 性能测试 (benchmarks/)
**目的：** 建立性能基准

**测试维度：**
- 延迟测试
- 吞吐量测试
- 显存占用测试
- 跨框架对比

**下一步工作：**
- [ ] 设计性能测试方案
- [ ] 实现自动化测试脚本
- [ ] 建立性能基准数据
- [ ] 生成对比报告

## 📋 开发优先级

### Phase 1: 基础设施 (优先)
1. ✅ 项目结构初始化
2. ✅ 文档框架搭建
3. ⏳ 统一接口设计
4. ⏳ vLLM框架集成
5. ⏳ Nvidia GPU适配

### Phase 2: 核心功能 (次要)
1. ⏳ SGLang框架集成
2. ⏳ 基础示例代码
3. ⏳ 性能测试框架
4. ⏳ 配置管理系统

### Phase 3: 场景应用 (中期)
1. ⏳ 互联网场景示例
2. ⏳ 科教场景示例
3. ⏳ 国产芯片适配
4. ⏳ 容器化部署

### Phase 4: 生产就绪 (长期)
1. ⏳ K8s编排方案
2. ⏳ 监控告警系统
3. ⏳ 金融/医疗场景
4. ⏳ 完整文档和教程

## 🚀 快速开始指南

### 1. 开发环境准备
```bash
# 克隆仓库
git clone <your-repo-url>
cd omni-inference-in-action

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
pip install -e .
```

### 2. 查看文档
- 项目总览：`README.md`
- 贡献指南：`CONTRIBUTING.md`
- 各模块说明：各目录下的 `README.md`

### 3. 运行示例
```bash
# 等待示例代码完成后执行
python examples/basic/01_simple_generation.py
```

## 📞 相关资源

- **vLLM**: https://github.com/vllm-project/vllm
- **SGLang**: https://github.com/sgl-project/sglang
- **Nvidia GPU**: https://developer.nvidia.com/
- **海光DCU**: https://www.hygon.cn/
- **昇腾**: https://www.hiascend.com/
- **寒武纪**: https://www.cambricon.com/

## 💡 设计理念

1. **统一接口**：不同框架提供一致的调用方式
2. **硬件抽象**：屏蔽底层硬件差异
3. **场景优先**：以实际应用场景为导向
4. **易于扩展**：便于添加新框架和硬件支持
5. **性能优先**：始终关注推理性能优化

## 📝 注意事项

1. 当前项目处于初始化阶段，大部分代码还未实现
2. 文档结构已经搭建，需要逐步填充内容
3. 优先完成 vLLM + Nvidia GPU 的基础功能
4. 国产芯片适配需要相应硬件环境
5. 欢迎社区贡献代码和文档

---

**最后更新时间：** 2026-01-05


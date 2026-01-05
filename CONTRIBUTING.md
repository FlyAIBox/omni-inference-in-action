# 贡献指南 | Contributing Guide

感谢你对 Omni-Inference-in-Action 项目的关注！我们欢迎所有形式的贡献。

## 🤝 贡献方式

### 1. 报告问题 (Bug Report)

如果你发现了 bug，请：
1. 在 [Issues](https://github.com/your-org/omni-inference-in-action/issues) 中搜索是否已有相关问题
2. 如果没有，创建新的 Issue，包含：
   - 清晰的标题
   - 详细的问题描述
   - 复现步骤
   - 期望行为
   - 实际行为
   - 环境信息（操作系统、Python版本、硬件配置等）
   - 错误日志（如果有）

### 2. 功能建议 (Feature Request)

如果你有新功能建议，请：
1. 创建新的 Issue，标记为 `enhancement`
2. 描述你的需求场景
3. 说明期望的功能
4. 解释为什么这个功能有用

### 3. 提交代码 (Pull Request)

#### 准备工作

```bash
# Fork 项目并克隆到本地
git clone https://github.com/your-username/omni-inference-in-action.git
cd omni-inference-in-action

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
pip install -e .

# 创建新分支
git checkout -b feature/your-feature-name
```

#### 代码规范

1. **Python 代码风格**
   - 遵循 [PEP 8](https://pep8.org/) 规范
   - 使用 `black` 格式化代码：`black .`
   - 使用 `flake8` 检查代码：`flake8 .`
   - 使用 `mypy` 进行类型检查：`mypy .`

2. **命名规范**
   - 文件名：小写字母+下划线（如：`inference_engine.py`）
   - 类名：大驼峰（如：`InferenceEngine`）
   - 函数/变量名：小写字母+下划线（如：`load_model`）
   - 常量：大写字母+下划线（如：`MAX_BATCH_SIZE`）

3. **注释规范**
   ```python
   def generate_text(prompt: str, max_tokens: int = 100) -> str:
       """
       生成文本
       
       Args:
           prompt: 输入提示词
           max_tokens: 最大生成token数
           
       Returns:
           生成的文本
           
       Raises:
           ValueError: 当prompt为空时抛出
       """
       pass
   ```

4. **测试要求**
   - 为新功能编写单元测试
   - 确保所有测试通过：`pytest tests/`
   - 保持测试覆盖率 > 80%

#### 提交流程

1. **编写代码**
   ```bash
   # 进行你的修改
   # ...
   ```

2. **运行测试**
   ```bash
   # 代码格式化
   black .
   
   # 代码检查
   flake8 .
   mypy .
   
   # 运行测试
   pytest tests/
   ```

3. **提交更改**
   ```bash
   git add .
   git commit -m "feat: 添加XXX功能"
   ```

   提交信息格式：
   - `feat:` 新功能
   - `fix:` 修复bug
   - `docs:` 文档更新
   - `style:` 代码格式调整
   - `refactor:` 重构
   - `test:` 测试相关
   - `chore:` 构建/工具相关

4. **推送到你的仓库**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **创建 Pull Request**
   - 在 GitHub 上创建 PR
   - 填写 PR 描述模板
   - 关联相关 Issue
   - 等待代码审查

### 4. 改进文档

文档改进也是重要的贡献！你可以：
- 修复文档中的错误
- 完善现有文档
- 添加新的教程或示例
- 翻译文档

### 5. 分享使用经验

你可以通过以下方式分享：
- 在 [Discussions](https://github.com/your-org/omni-inference-in-action/discussions) 中分享使用经验
- 撰写博客文章
- 制作视频教程
- 在社交媒体上推广

## 📋 开发指南

### 项目结构

请参考 [README.md](README.md) 中的项目架构部分。

### 添加新的推理框架

1. 在 `frameworks/` 下创建新目录
2. 实现 `frameworks/common/interfaces.py` 中定义的接口
3. 添加单元测试
4. 更新文档

### 添加新的加速卡支持

1. 在 `accelerators/` 下创建新目录
2. 实现 `accelerators/common/interface.py` 中定义的接口
3. 在 `accelerators/common/factory.py` 中注册
4. 添加性能测试
5. 更新文档

### 添加新的应用场景

1. 在 `applications/` 下创建新目录
2. 提供完整的端到端示例
3. 编写详细的使用文档
4. 提供性能基准测试

## 🔍 代码审查标准

我们会从以下方面审查代码：
1. **功能性**：代码是否实现了预期功能
2. **代码质量**：是否遵循代码规范
3. **测试**：是否有充分的测试覆盖
4. **文档**：是否有清晰的注释和文档
5. **性能**：是否考虑了性能优化
6. **兼容性**：是否与现有代码兼容

## 📞 联系方式

如有任何问题，欢迎通过以下方式联系：
- GitHub Issues
- GitHub Discussions
- 邮件：contact@example.com

## 🙏 致谢

感谢所有为项目做出贡献的开发者！

---

**再次感谢你的贡献！🎉**


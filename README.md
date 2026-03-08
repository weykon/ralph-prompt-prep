# Ralph Loop Unit - Ralph Wiggum Prompt 準備工具

這個項目提供了一套完整的工具和指南，幫助你準備高質量的 Ralph Wiggum Loop prompts。

## 📁 文件結構

```
raplh-loop-unit/
├── README.md                    # 本文件
├── quick_reference.md           # 快速參考指南（⭐ 從這裡開始）
├── ralph-prompt-builder.md      # 完整的準備框架文檔
├── ralph_prompt_builder.py      # 互動式 prompt 生成工具
└── examples_improved.md         # 改進範例（你的兩段 prompt）
```

## 🚀 快速開始

### 一鍵安裝（推薦）

```bash
curl -fsSL https://raw.githubusercontent.com/weykon/ralph-prompt-prep/main/install.sh | bash
```

或者手動安裝：

```bash
git clone https://github.com/weykon/ralph-prompt-prep.git
cd ralph-prompt-prep
./install.sh
```

### 使用方法

#### 方法 1: Claude Code Skill（最簡單）

```bash
/ralph-prompt-prep "I want to implement user authentication"
```

Skill 會引導你完成 prompt 準備過程。

#### 方法 2: Python 互動式工具

```bash
python3 ralph_prompt_builder.py
```

跟隨提示回答問題，自動生成結構化的 Ralph prompt。

#### 方法 3: 查看範例學習

```bash
cat examples_improved.md
```

查看實際的 prompt 改進案例，學習最佳實踐。

#### 方法 4: 使用模板（熟練用戶）

1. 打開 `quick_reference.md`
2. 複製模板
3. 填寫每個部分
4. 執行 Ralph Loop

## 📚 文檔說明

### 1. quick_reference.md ⭐
**最重要的文檔，從這裡開始！**

包含：
- Ralph Wiggum 核心概念
- 好的 prompt 特徵
- 常見錯誤和改進方法
- 快速開始指南
- Prompt 模板
- 調試技巧
- 最佳實踐

**適合**：所有用戶，特別是第一次使用 Ralph Loop 的人

### 2. ralph-prompt-builder.md
**完整的準備框架文檔**

包含：
- 五步準備流程
- 每一步的詳細說明
- 範例和建議
- 使用場景指導

**適合**：需要深入理解 prompt 結構的用戶

### 3. examples_improved.md
**你的兩段 prompt 的改進版本**

包含：
- 原始 prompt 的問題分析
- 改進後的完整 prompt
- 關鍵改進點總結
- 使用建議

**適合**：想看實際案例的用戶

### 4. ralph_prompt_builder.py
**互動式工具**

功能：
- 引導式問答
- 自動生成結構化 prompt
- 保存到文件
- 提供執行命令

**適合**：喜歡互動式工具的用戶

## 🎯 你的兩段 Prompt 改進總結

### 原始 Prompt 1: 遠程協助功能
**問題**：
- ❌ 細節混亂，缺乏優先級
- ❌ 沒有明確的完成標準
- ❌ 缺少驗證步驟

**改進後**：
- ✅ 清晰的成功標準（6個可測試的標準）
- ✅ 明確的範圍（In/Out Scope）
- ✅ 具體的驗證步驟（測試命令、檢查清單）
- ✅ 階段性里程碑（4個階段）
- ✅ 完成承諾：`<promise>REMOTE_SESSION_COMPLETE</promise>`

### 原始 Prompt 2: Bots 系統優化
**問題**：
- ❌ 範圍太大（5個bots + docker + skills + mcps）
- ❌ 目標模糊（"更好"、"更完整"）
- ❌ 沒有具體的驗證步驟

**改進後**：
- ✅ 拆分成多個小 Loop（Loop 1: 穩定性，Loop 2: 網站優化）
- ✅ 量化目標（成功率 >85%，24小時無崩潰）
- ✅ 數據驅動（SQL查詢、分析腳本）
- ✅ 具體的驗證步驟和成功指標
- ✅ 完成承諾：`<promise>BOTS_STABILITY_COMPLETE</promise>`

查看 `examples_improved.md` 獲取完整的改進版本。

## 💡 核心概念

Ralph Wiggum 技術的本質：

```
同一個 prompt 重複執行
    ↓
Claude 看到自己之前的工作（通過文件和 git 歷史）
    ↓
持續改進直到完成
    ↓
輸出 <promise>COMPLETE</promise>
```

**不是** Claude 跟自己對話，**而是** Claude 看到自己的工作成果並持續改進。

## ✅ 好的 Ralph Prompt 檢查清單

在執行 `/ralph-loop` 之前，確保你的 prompt 有：

- [ ] 明確的目標（一句話說清楚）
- [ ] 可測試的成功標準（不是"更好"，而是"測試通過"）
- [ ] 清晰的範圍（In Scope / Out of Scope）
- [ ] 具體的驗證步驟（運行什麼命令，檢查什麼）
- [ ] 完成承諾標記（`<promise>TASK_COMPLETE</promise>`）
- [ ] 合理的迭代次數（5-20次）
- [ ] 優先級劃分（P0/P1/P2）
- [ ] 階段性里程碑（可選但推薦）

## 🎓 使用流程

### 第一次使用 Ralph Loop

1. **閱讀快速參考**
   ```bash
   cat quick_reference.md
   ```

2. **查看改進範例**
   ```bash
   cat examples_improved.md
   ```

3. **使用互動式工具**
   ```bash
   python3 ralph_prompt_builder.py
   ```

4. **執行 Ralph Loop**
   ```bash
   /ralph-loop "$(cat ralph_prompt_generated.md)" --max-iterations 10 --completion-promise "YOUR_PROMISE"
   ```

### 已經熟悉 Ralph Loop

1. **複製模板**（從 `quick_reference.md`）
2. **填寫內容**
3. **執行 Ralph Loop**

## 🔧 工具使用

### ralph_prompt_builder.py

```bash
# 運行互動式工具
python3 ralph_prompt_builder.py

# 工具會引導你完成：
# 1. 任務定義（目標、成功標準、完成承諾）
# 2. 範圍控制（In/Out Scope、優先級）
# 3. 驗證策略（測試方法、驗證步驟）
# 4. 迭代策略（迭代次數、階段劃分）
# 5. 生成最終 prompt

# 輸出：ralph_prompt_generated.md
```

## 📊 迭代次數建議

| 任務複雜度 | 迭代次數 | 範例 |
|-----------|---------|------|
| 簡單 | 5 | 修復單個 bug、添加簡單功能 |
| 中等 | 10 | 實現新功能、重構模塊 |
| 複雜 | 20 | 大型重構、系統優化 |
| 非常複雜 | 30 | 架構改造、多模塊協調 |

## 🆘 常見問題

### Q: Ralph Loop 一直運行不停止？
**A**: 檢查是否輸出了 `<promise>` 標記，確保 promise 文本與 `--completion-promise` 參數匹配。

### Q: Loop 過早停止？
**A**: 增加 `--max-iterations` 或檢查是否意外觸發了 promise。

### Q: 每次迭代都重複同樣的錯誤？
**A**: 在 prompt 中添加更詳細的錯誤處理指導和調試步驟。

### Q: 如何取消正在運行的 Loop？
**A**: 執行 `/cancel-ralph`

### Q: 如何監控 Loop 進度？
**A**: 查看 `.claude/.ralph-loop.local.md` 和 git 歷史。

## 🎯 最佳實踐

### 1. 小步快跑
拆分成多個小 Loop，而不是一個大 Loop。

### 2. 數據驅動
使用量化指標，而不是模糊的"更好"。

### 3. 明確驗證
提供具體的測試命令和檢查步驟。

### 4. 合理範圍
明確 In Scope 和 Out of Scope。

## 📚 相關資源

- **原始技術**: https://ghuntley.com/ralph/
- **Ralph Orchestrator**: https://github.com/mikeyobrien/ralph-orchestrator
- **Claude Code**: https://github.com/anthropics/claude-code

## 🤝 下一步

1. **如果你是新手**：
   - 閱讀 `quick_reference.md`
   - 查看 `examples_improved.md`
   - 運行 `python3 ralph_prompt_builder.py`

2. **如果你想深入理解**：
   - 閱讀 `ralph-prompt-builder.md`
   - 研究改進範例的每個部分
   - 嘗試改進你自己的 prompt

3. **如果你已經熟練**：
   - 直接使用模板
   - 根據項目需求調整
   - 執行 Ralph Loop

## 💬 溝通和反饋

如果你有任何問題或建議，歡迎：
- 查看文檔中的範例
- 使用互動式工具
- 參考快速參考指南

祝你使用 Ralph Loop 愉快！🚀

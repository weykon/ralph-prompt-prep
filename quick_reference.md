# Ralph Loop 快速參考指南

## 🎯 核心概念

Ralph Wiggum 技術 = **同一個 prompt 重複執行** + **Claude 看到自己的工作** + **持續改進**

```
迭代 1: Prompt → Claude 工作 → 修改文件
迭代 2: Prompt → Claude 看到迭代1的修改 → 繼續改進
迭代 3: Prompt → Claude 看到迭代1+2的修改 → 繼續改進
...
直到: <promise>COMPLETE</promise>
```

---

## ✅ 好的 Ralph Prompt 特徵

```markdown
✅ 明確的目標（一句話說清楚）
✅ 可測試的成功標準（不是"更好"，而是"測試通過"）
✅ 清晰的範圍（包含什麼，不包含什麼）
✅ 具體的驗證步驟（運行什麼命令，檢查什麼）
✅ 完成承諾標記（<promise>TASK_COMPLETE</promise>）
✅ 合理的迭代次數（5-20次）
```

---

## ❌ 常見錯誤

```markdown
❌ 目標模糊："做好遠程協助"
   ✅ 改進："實現 Session 標識和控制請求處理"

❌ 範圍太大："優化整個系統"
   ✅ 改進："提升任務執行穩定性（成功率 >85%）"

❌ 沒有驗證："完成後檢查"
   ✅ 改進："運行 `cargo test`，檢查日誌，手動測試流程"

❌ 缺少完成標記
   ✅ 改進："<promise>FEATURE_COMPLETE</promise>"

❌ 迭代次數不合理：--max-iterations 100
   ✅ 改進：--max-iterations 10（簡單任務5次，複雜任務20次）
```

---

## 🚀 快速開始

### 方法 1: 使用互動式工具

```bash
cd /Users/weykon/Desktop/p/raplh-loop-unit
python3 ralph_prompt_builder.py
```

跟隨提示回答問題，自動生成結構化 prompt。

### 方法 2: 使用模板

1. 複製 `ralph-prompt-builder.md` 中的模板
2. 填寫每個部分
3. 保存為 `my_task_prompt.md`
4. 執行：
   ```bash
   /ralph-loop "$(cat my_task_prompt.md)" --max-iterations 10 --completion-promise "MY_TASK_COMPLETE"
   ```

### 方法 3: 參考範例

查看 `examples_improved.md` 中的改進範例，學習如何優化你的 prompt。

---

## 📋 Prompt 模板（複製使用）

```markdown
# 任務：[一句話描述]

## 目標
[詳細描述要完成什麼]

## 成功標準
- [ ] [可測試的標準1]
- [ ] [可測試的標準2]
- [ ] [可測試的標準3]

## 範圍
### 包含 (In Scope)
✅ [功能1]
✅ [功能2]

### 不包含 (Out of Scope)
❌ [不做的事1]
❌ [不做的事2]

## 優先級
### P0 (必須完成)
- [核心功能]

### P1 (重要)
- [重要功能]

### P2 (可選)
- [可選功能]

## 實現步驟
1. [步驟1]
2. [步驟2]
3. [步驟3]

## 驗證策略
### 測試方法
- [測試類型1]
- [測試類型2]

### 每次迭代後驗證
1. 運行測試：`[測試命令]`
2. 檢查日誌：`[日誌位置]`
3. 手動驗證：[驗證步驟]

## 迭代階段
- **階段 1 (迭代 1-3)**: [階段1目標]
- **階段 2 (迭代 4-6)**: [階段2目標]
- **階段 3 (迭代 7-10)**: [階段3目標]

## 完成條件
當 [具體條件] 時，輸出：
<promise>[COMPLETION_PROMISE]</promise>

## 執行指令
```bash
/ralph-loop "$(cat THIS_PROMPT.md)" --max-iterations [N] --completion-promise "[COMPLETION_PROMISE]"
```
```

---

## 🎯 迭代次數建議

| 任務複雜度 | 迭代次數 | 範例 |
|-----------|---------|------|
| 簡單 | 5 | 修復單個 bug、添加簡單功能 |
| 中等 | 10 | 實現新功能、重構模塊 |
| 複雜 | 20 | 大型重構、系統優化 |
| 非常複雜 | 30 | 架構改造、多模塊協調 |

---

## 🏷️ Completion Promise 命名建議

```
功能開發：FEATURE_COMPLETE, LOGIN_COMPLETE, API_COMPLETE
測試相關：TESTS_PASS, COVERAGE_COMPLETE
重構相關：REFACTOR_DONE, CLEANUP_COMPLETE
優化相關：OPTIMIZATION_COMPLETE, PERFORMANCE_IMPROVED
修復相關：BUG_FIXED, ISSUE_RESOLVED
```

**規則**：
- 全大寫
- 使用下劃線分隔
- 簡短明確（2-3個詞）
- 反映任務本質

---

## 🔍 調試 Ralph Loop

### 問題：Loop 一直運行不停止

**可能原因**：
1. 沒有輸出 `<promise>` 標記
2. Promise 文本不匹配
3. 成功標準無法達成

**解決方法**：
```bash
# 檢查是否有 promise 輸出
grep -r "<promise>" .

# 檢查 promise 文本是否匹配
# 確保 --completion-promise 參數與 prompt 中的一致

# 降低成功標準或增加迭代次數
/ralph-loop "..." --max-iterations 20
```

### 問題：Loop 過早停止

**可能原因**：
1. 迭代次數太少
2. 成功標準設置過低
3. 意外輸出了 promise 標記

**解決方法**：
```bash
# 增加迭代次數
/ralph-loop "..." --max-iterations 30

# 檢查 promise 是否被意外觸發
# 確保 promise 標記只在真正完成時輸出
```

### 問題：每次迭代都在重複同樣的錯誤

**可能原因**：
1. Prompt 沒有提供足夠的上下文
2. 驗證步驟不夠具體
3. 錯誤處理指導不清晰

**解決方法**：
- 在 prompt 中添加更詳細的錯誤處理指導
- 提供具體的調試步驟
- 添加失敗時的檢查清單

---

## 📊 監控 Ralph Loop 進度

### 查看迭代狀態
```bash
# 查看 Ralph Loop 狀態文件
cat .claude/.ralph-loop.local.md

# 查看 git 歷史（每次迭代的修改）
git log --oneline -10

# 查看文件變化
git diff HEAD~5
```

### 分析迭代效果
```bash
# 統計測試通過率
pytest --tb=short | grep "passed"

# 檢查代碼質量
cargo clippy --all-targets

# 查看日誌錯誤
grep ERROR logs/*.log | wc -l
```

---

## 🎓 最佳實踐

### 1. 小步快跑
```
❌ 一個大 Loop：實現整個系統（30次迭代）
✅ 多個小 Loop：
   - Loop 1: 核心功能（10次）
   - Loop 2: 測試覆蓋（5次）
   - Loop 3: 優化性能（10次）
```

### 2. 數據驅動
```
❌ "優化性能"
✅ "將響應時間從 500ms 降低到 200ms"

❌ "提高穩定性"
✅ "將任務成功率從 60% 提升到 85%"
```

### 3. 明確驗證
```
❌ "檢查功能是否正常"
✅ "運行 `cargo test`，檢查 `logs/app.log` 無 ERROR，手動測試登錄流程"
```

### 4. 合理範圍
```
❌ In Scope: 所有功能
✅ In Scope: Session 管理、基本顯示、控制請求
   Out of Scope: 權限系統、加密、多人協作
```

---

## 🆘 需要幫助？

### 使用互動式工具
```bash
python3 ralph_prompt_builder.py
```

### 查看範例
```bash
cat examples_improved.md
```

### 查看完整文檔
```bash
cat ralph-prompt-builder.md
```

### 取消當前 Loop
```bash
/cancel-ralph
```

---

## 📚 相關資源

- 原始技術：https://ghuntley.com/ralph/
- Ralph Orchestrator：https://github.com/mikeyobrien/ralph-orchestrator
- Claude Code 文檔：https://github.com/anthropics/claude-code

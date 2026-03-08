# Task: 為 ralph-prompt-prep skill 創建完整的開源項目和展示網站

## Objective
將當前的 ralph-prompt-prep skill 打包成一個完整的開源項目，包括：
1. 初始化 Git 倉庫並推送到 GitHub
2. 創建一個簡單的展示網站，介紹這個 skill 的用途、使用方法和價值
3. 提供簡單的安裝和部署方案
4. 編寫清晰的文檔，包含故事化的介紹和實際使用場景

## Success Criteria
- [ ] Git 倉庫已初始化，所有文件已提交
- [ ] GitHub 公開倉庫已創建並推送成功
- [ ] 展示網站已創建，包含：介紹、使用場景、安裝指南、示例
- [ ] 網站可以本地運行並正常顯示
- [ ] 部署方案已研究並實現（GitHub Pages 或其他簡單方案）
- [ ] README.md 包含完整的項目說明和快速開始指南
- [ ] 有至少一個實際的使用示例/演示

## Scope
### In Scope
✅ Git 倉庫初始化和 GitHub 創建
✅ 簡單的靜態網站（HTML/CSS/JS 或簡單框架）
✅ 通俗易懂的項目介紹和故事
✅ 使用場景和示例
✅ 一鍵安裝/部署方案研究和實現
✅ 基本的文檔（README、使用指南）
✅ GitHub Pages 或類似的免費部署方案

### Out of Scope
❌ 複雜的後端系統
❌ 用戶認證和數據庫
❌ 多語言支持（先專注英文/中文）
❌ 高級的 CI/CD 流程
❌ 商業化功能

## Priority
### P0 (Must Complete)
- Git 倉庫和 GitHub 創建
- 基本的 README 文檔
- 簡單的展示網站（單頁即可）
- 部署到 GitHub Pages

### P1 (Important)
- 詳細的使用指南和示例
- 故事化的介紹（為什麼需要這個 skill）
- 一鍵安裝腳本或清晰的安裝步驟
- 視覺設計優化

### P2 (Optional)
- 互動式演示
- 視頻教程或 GIF 演示
- 社區貢獻指南
- 更多使用場景示例

## Implementation Steps
1. **初始化 Git 和創建 GitHub 倉庫**
   - 初始化 Git 倉庫
   - 創建 .gitignore
   - 提交現有文件
   - 使用 `gh` CLI 創建 GitHub 公開倉庫
   - 推送到 GitHub

2. **研究部署方案**
   - 搜索當前流行的 skill 展示網站部署方案
   - 研究 GitHub Pages 的最佳實踐
   - 研究一鍵安裝方案（如 npm install、curl 腳本等）
   - 選擇最簡單易用的方案

3. **創建展示網站**
   - 設計簡單的單頁網站結構
   - 編寫通俗易懂的介紹（包含故事和使用場景）
   - 添加使用示例和代碼片段
   - 添加安裝指南
   - 確保響應式設計（手機和桌面都能看）

4. **完善文檔**
   - 更新 README.md（項目介紹、快速開始、貢獻指南）
   - 創建 USAGE.md（詳細使用指南）
   - 添加 LICENSE 文件
   - 創建 CONTRIBUTING.md（如果需要）

5. **部署和測試**
   - 配置 GitHub Pages
   - 測試網站在不同設備上的顯示
   - 測試安裝流程
   - 驗證所有鏈接和資源

## Validation
### After Each Iteration
1. **檢查 Git 狀態**：`git status` 和 `git log`
2. **測試網站**：本地運行網站，檢查所有頁面和鏈接
3. **驗證部署**：訪問 GitHub Pages URL，確認正常顯示
4. **測試安裝**：在乾淨的環境測試安裝流程
5. **檢查文檔**：確保 README 和其他文檔清晰完整

### Success Indicators
- GitHub 倉庫可訪問：https://github.com/[username]/ralph-prompt-prep
- 網站可訪問：https://[username].github.io/ralph-prompt-prep
- 安裝流程可以在5分鐘內完成
- 文檔清晰，新用戶可以快速上手

## Research Tasks
在實現過程中需要搜索和研究：
1. **部署方案**：
   - "GitHub Pages deployment best practices 2026"
   - "simple static site deployment options"
   - "skill installation methods Claude Code"

2. **展示網站參考**：
   - "open source project landing page examples"
   - "skill documentation website examples"
   - "simple one-page project showcase"

3. **一鍵安裝**：
   - "Claude Code skill installation methods"
   - "one-click install script examples"
   - "skill package distribution best practices"

## Iteration Phases
- **Phase 1 (iterations 1-2)**: Git 倉庫創建、GitHub 推送、基本 README
- **Phase 2 (iterations 3-4)**: 研究部署方案、創建展示網站、配置 GitHub Pages
- **Phase 3 (iterations 5)**: 完善文檔、優化網站、測試安裝流程、最終驗證

## Completion Condition
當以下條件全部滿足時，輸出：
<promise>PROJECT_PUBLISHED</promise>

條件：
- GitHub 倉庫已創建並包含所有文件
- 展示網站已部署到 GitHub Pages 並可正常訪問
- README 包含完整的項目說明和快速開始指南
- 至少有一個清晰的使用示例
- 安裝/部署流程已測試並正常工作

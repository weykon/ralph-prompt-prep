#!/usr/bin/env python3
"""
Ralph Prompt Builder - 互動式工具
幫助用戶準備結構化的 Ralph Loop prompts
"""

import sys
from typing import List, Dict

class RalphPromptBuilder:
    def __init__(self):
        self.data = {
            "core_goal": "",
            "success_criteria": [],
            "completion_promise": "",
            "in_scope": [],
            "out_scope": [],
            "priorities": {"P0": [], "P1": [], "P2": []},
            "test_methods": [],
            "validation_steps": [],
            "iteration_phases": [],
            "max_iterations": 10
        }

    def ask(self, question: str, multiline: bool = False) -> str:
        """詢問用戶輸入"""
        print(f"\n📝 {question}")
        if multiline:
            print("   (輸入空行結束)")
            lines = []
            while True:
                line = input("   ")
                if not line:
                    break
                lines.append(line)
            return "\n".join(lines)
        else:
            return input("   > ")

    def ask_list(self, question: str) -> List[str]:
        """詢問列表輸入"""
        print(f"\n📝 {question}")
        print("   (每行一項，輸入空行結束)")
        items = []
        while True:
            item = input("   - ")
            if not item:
                break
            items.append(item)
        return items

    def step1_task_definition(self):
        """第一步：任務定義"""
        print("\n" + "="*60)
        print("🎯 第一步：任務定義")
        print("="*60)

        self.data["core_goal"] = self.ask(
            "用一句話描述你要完成什麼？",
            multiline=False
        )

        self.data["success_criteria"] = self.ask_list(
            "列出成功標準（必須可測試）："
        )

        self.data["completion_promise"] = self.ask(
            "選擇一個完成標記（全大寫，如 FEATURE_COMPLETE）：",
            multiline=False
        ).upper()

    def step2_scope_control(self):
        """第二步：範圍控制"""
        print("\n" + "="*60)
        print("🎯 第二步：範圍控制")
        print("="*60)

        self.data["in_scope"] = self.ask_list(
            "包含什麼功能？（In Scope）"
        )

        self.data["out_scope"] = self.ask_list(
            "不包含什麼功能？（Out of Scope）"
        )

        print("\n📝 設置優先級：")
        self.data["priorities"]["P0"] = self.ask_list("P0 (必須完成)：")
        self.data["priorities"]["P1"] = self.ask_list("P1 (重要)：")
        self.data["priorities"]["P2"] = self.ask_list("P2 (可選)：")

    def step3_validation(self):
        """第三步：驗證策略"""
        print("\n" + "="*60)
        print("🎯 第三步：驗證策略")
        print("="*60)

        self.data["test_methods"] = self.ask_list(
            "測試方法（如：單元測試、集成測試、E2E測試）："
        )

        self.data["validation_steps"] = self.ask_list(
            "每次迭代後的驗證步驟："
        )

    def step4_iteration(self):
        """第四步：迭代策略"""
        print("\n" + "="*60)
        print("🎯 第四步：迭代策略")
        print("="*60)

        max_iter = self.ask(
            "預計需要多少次迭代？（建議：簡單5次，中等10次，複雜20次）",
            multiline=False
        )
        self.data["max_iterations"] = int(max_iter) if max_iter.isdigit() else 10

        print("\n📝 劃分階段（可選，直接回車跳過）：")
        phase_num = 1
        while True:
            phase = self.ask(
                f"階段 {phase_num} 描述（如：迭代1-3: 實現核心功能）：",
                multiline=False
            )
            if not phase:
                break
            self.data["iteration_phases"].append(phase)
            phase_num += 1

    def generate_prompt(self) -> str:
        """生成最終的 Ralph prompt"""
        prompt = f"""# 任務：{self.data['core_goal']}

## 目標
{self.data['core_goal']}

## 成功標準
"""
        for criterion in self.data['success_criteria']:
            prompt += f"- [ ] {criterion}\n"

        prompt += "\n## 範圍\n"
        prompt += "### 包含 (In Scope)\n"
        for item in self.data['in_scope']:
            prompt += f"✅ {item}\n"

        prompt += "\n### 不包含 (Out of Scope)\n"
        for item in self.data['out_scope']:
            prompt += f"❌ {item}\n"

        prompt += "\n## 優先級\n"
        for priority, items in self.data['priorities'].items():
            if items:
                prompt += f"### {priority}\n"
                for item in items:
                    prompt += f"- {item}\n"

        prompt += "\n## 驗證策略\n"
        prompt += "### 測試方法\n"
        for method in self.data['test_methods']:
            prompt += f"- {method}\n"

        prompt += "\n### 每次迭代後驗證\n"
        for step in self.data['validation_steps']:
            prompt += f"{step}\n"

        if self.data['iteration_phases']:
            prompt += "\n## 迭代階段\n"
            for phase in self.data['iteration_phases']:
                prompt += f"- {phase}\n"

        prompt += f"""
## 完成條件
當所有成功標準達成時，輸出：
<promise>{self.data['completion_promise']}</promise>

## 執行指令
```bash
/ralph-loop "$(cat THIS_PROMPT.md)" --max-iterations {self.data['max_iterations']} --completion-promise "{self.data['completion_promise']}"
```
"""
        return prompt

    def run(self):
        """運行完整流程"""
        print("\n" + "="*60)
        print("🚀 Ralph Prompt Builder")
        print("="*60)
        print("\n這個工具會幫助你準備結構化的 Ralph Loop prompt")
        print("讓我們開始吧！\n")

        try:
            self.step1_task_definition()
            self.step2_scope_control()
            self.step3_validation()
            self.step4_iteration()

            print("\n" + "="*60)
            print("✅ 準備完成！生成 prompt...")
            print("="*60)

            prompt = self.generate_prompt()

            # 保存到文件
            filename = "ralph_prompt_generated.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(prompt)

            print(f"\n✅ Prompt 已保存到：{filename}")
            print("\n" + "="*60)
            print("📋 生成的 Prompt：")
            print("="*60)
            print(prompt)

            print("\n" + "="*60)
            print("🎯 下一步：")
            print("="*60)
            print(f"1. 檢查生成的 prompt：{filename}")
            print("2. 根據需要調整內容")
            print("3. 執行 Ralph Loop：")
            print(f"   /ralph-loop \"$(cat {filename})\" --max-iterations {self.data['max_iterations']} --completion-promise \"{self.data['completion_promise']}\"")

        except KeyboardInterrupt:
            print("\n\n❌ 已取消")
            sys.exit(0)
        except Exception as e:
            print(f"\n\n❌ 錯誤：{e}")
            sys.exit(1)

if __name__ == "__main__":
    builder = RalphPromptBuilder()
    builder.run()

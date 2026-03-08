# Usage Guide

## Installation

### Method 1: Claude Code Skill (Recommended)

The ralph-prompt-prep skill is available in the `.claude/skills/` directory. To use it:

1. Ensure the skill is in your Claude Code skills directory:
   ```bash
   ls ~/.claude/skills/ralph-prompt-prep/
   ```

2. Invoke the skill:
   ```bash
   /ralph-prompt-prep "Your task description here"
   ```

### Method 2: Clone and Use Python Tool

```bash
# Clone the repository
git clone https://github.com/weykon/ralph-prompt-prep.git
cd ralph-prompt-prep

# Run the interactive tool
python3 ralph_prompt_builder.py
```

### Method 3: Manual Template

1. Read the quick reference:
   ```bash
   cat quick_reference.md
   ```

2. Copy the template and fill in your details

3. Save as `my_prompt.md`

4. Execute Ralph Loop:
   ```bash
   /ralph-wiggum:ralph-loop "$(cat my_prompt.md)" --max-iterations 10 --completion-promise "YOUR_PROMISE"
   ```

## Using the Skill

### Interactive Mode

When you invoke `/ralph-prompt-prep`, the skill will:

1. **Analyze Context**: Check your current project and conversation history
2. **Ask Questions**: Guide you through defining your task
3. **Generate Prompt**: Create a structured Ralph Loop prompt
4. **Provide Command**: Give you the exact command to run

### Example Session

```
You: /ralph-prompt-prep "I want to add authentication to my app"

Claude: Got it! Let me help you prepare a solid prompt for that.

From what you've described, it sounds like you want to implement
authentication with user login/logout. Is that the core goal?

A few quick questions:
1. What specific things can we check to verify this is working?
2. Are there things we should NOT include in this loop?
3. How many iterations do you think this needs?

[Continue conversation...]

[Claude generates structured prompt]

You can now run:
/ralph-wiggum:ralph-loop "[generated prompt]" --max-iterations 10 --completion-promise "AUTH_COMPLETE"
```

## Prompt Structure

A good Ralph prompt includes:

### 1. Task (One Sentence)
Clear, focused goal statement

### 2. Objective
Detailed description of what needs to be accomplished

### 3. Success Criteria
- [ ] Testable criterion 1
- [ ] Testable criterion 2
- [ ] Testable criterion 3

### 4. Scope
**In Scope:**
- Feature 1
- Feature 2

**Out of Scope:**
- Thing we're NOT doing 1
- Thing we're NOT doing 2

### 5. Priority
- **P0 (Must Complete)**: Core functionality
- **P1 (Important)**: Important features
- **P2 (Optional)**: Nice-to-have features

### 6. Implementation Steps
1. Step 1
2. Step 2
3. Step 3

### 7. Validation
Commands to run and things to check after each iteration

### 8. Completion Condition
```
<promise>TASK_COMPLETE</promise>
```

## Tips for Success

### Do's ✅
- **Be Specific**: "Tests pass" not "works well"
- **Set Boundaries**: Clear In/Out scope
- **Validate Often**: Check after each iteration
- **Use Metrics**: "Success rate >85%" not "better"
- **Small Scope**: Focus on one thing at a time

### Don'ts ❌
- **Vague Goals**: "Improve the system"
- **Too Broad**: Trying to do everything
- **No Validation**: Can't verify success
- **Missing Promise**: Loop runs forever
- **Subjective Criteria**: "Looks good"

## Troubleshooting

### Loop Won't Stop
**Problem**: Ralph Loop keeps running
**Solution**: Check that your `<promise>` tag matches `--completion-promise` exactly

### Loop Stops Too Early
**Problem**: Loop exits before completion
**Solution**: Increase `--max-iterations` or check if promise was accidentally triggered

### Repeated Errors
**Problem**: Same error every iteration
**Solution**: Add more detailed error handling guidance in your prompt

### Can't Find Skill
**Problem**: `/ralph-prompt-prep` not found
**Solution**: Check skill is in `~/.claude/skills/ralph-prompt-prep/SKILL.md`

## Advanced Usage

### Splitting Large Tasks

If your task is too large, split it into multiple loops:

```bash
# Loop 1: Core functionality
/ralph-wiggum:ralph-loop "[prompt 1]" --max-iterations 10 --completion-promise "CORE_COMPLETE"

# Loop 2: Additional features
/ralph-wiggum:ralph-loop "[prompt 2]" --max-iterations 10 --completion-promise "FEATURES_COMPLETE"
```

### Monitoring Progress

Check Ralph Loop state:
```bash
cat .claude/.ralph-loop.local.md
```

View git history:
```bash
git log --oneline -10
```

### Canceling a Loop

```bash
/cancel-ralph
```

## Resources

- **Quick Reference**: `quick_reference.md` - Templates and best practices
- **Examples**: `examples_improved.md` - Real prompt improvements
- **Framework**: `ralph-prompt-builder.md` - Complete preparation guide
- **Ralph Technique**: https://ghuntley.com/ralph/
- **Claude Code**: https://github.com/anthropics/claude-code

## Support

- GitHub Issues: https://github.com/weykon/ralph-prompt-prep/issues
- Documentation: https://weykon.github.io/ralph-prompt-prep/
- Examples: See `examples_improved.md` in the repository

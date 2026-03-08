#!/bin/bash
# Ralph Prompt Prep - Installation Script
# Installs the ralph-prompt-prep skill for Claude Code

set -e

echo "🎯 Ralph Prompt Prep - Installation Script"
echo "=========================================="
echo ""

# Check if Claude Code is installed
if ! command -v claude &> /dev/null; then
    echo "❌ Error: Claude Code CLI not found"
    echo "Please install Claude Code first: https://www.anthropic.com/claude-code"
    exit 1
fi

echo "✓ Claude Code CLI found"

# Determine skills directory
SKILLS_DIR="${HOME}/.claude/skills"

# Create skills directory if it doesn't exist
if [ ! -d "$SKILLS_DIR" ]; then
    echo "Creating skills directory: $SKILLS_DIR"
    mkdir -p "$SKILLS_DIR"
fi

echo "✓ Skills directory: $SKILLS_DIR"

# Check if skill already exists
if [ -d "$SKILLS_DIR/ralph-prompt-prep" ]; then
    echo ""
    echo "⚠️  ralph-prompt-prep skill already exists"
    read -p "Do you want to overwrite it? (y/N): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Installation cancelled"
        exit 0
    fi
    rm -rf "$SKILLS_DIR/ralph-prompt-prep"
fi

# Clone or copy the skill
echo ""
echo "Installing ralph-prompt-prep skill..."

# Check if we're running from the repo directory
if [ -f "ralph-prompt-prep/SKILL.md" ]; then
    echo "✓ Installing from local directory"
    cp -r ralph-prompt-prep "$SKILLS_DIR/"
elif [ -f ".claude/skills/ralph-prompt-prep/SKILL.md" ]; then
    echo "✓ Installing from .claude/skills directory"
    cp -r .claude/skills/ralph-prompt-prep "$SKILLS_DIR/"
else
    echo "Cloning from GitHub..."
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 https://github.com/weykon/ralph-prompt-prep.git "$TEMP_DIR"

    if [ -f "$TEMP_DIR/ralph-prompt-prep/SKILL.md" ]; then
        cp -r "$TEMP_DIR/ralph-prompt-prep" "$SKILLS_DIR/"
    elif [ -f "$TEMP_DIR/.claude/skills/ralph-prompt-prep/SKILL.md" ]; then
        cp -r "$TEMP_DIR/.claude/skills/ralph-prompt-prep" "$SKILLS_DIR/"
    else
        echo "❌ Error: Could not find SKILL.md in repository"
        rm -rf "$TEMP_DIR"
        exit 1
    fi

    rm -rf "$TEMP_DIR"
fi

# Verify installation
if [ -f "$SKILLS_DIR/ralph-prompt-prep/SKILL.md" ]; then
    echo ""
    echo "✅ Installation successful!"
    echo ""
    echo "The ralph-prompt-prep skill is now installed at:"
    echo "  $SKILLS_DIR/ralph-prompt-prep/"
    echo ""
    echo "Usage:"
    echo "  /ralph-prompt-prep \"Your task description\""
    echo ""
    echo "For more information:"
    echo "  - Documentation: https://weykon.github.io/ralph-prompt-prep/"
    echo "  - GitHub: https://github.com/weykon/ralph-prompt-prep"
    echo "  - Quick Reference: cat $SKILLS_DIR/ralph-prompt-prep/../../../quick_reference.md"
    echo ""
else
    echo "❌ Installation failed: SKILL.md not found"
    exit 1
fi

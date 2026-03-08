# Contributing to Ralph Prompt Prep

Thank you for your interest in contributing to Ralph Prompt Prep! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Issues

If you find a bug or have a suggestion:

1. Check if the issue already exists in [GitHub Issues](https://github.com/weykon/ralph-prompt-prep/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Claude Code version)

### Suggesting Enhancements

We welcome suggestions for:
- Improvements to the skill's guidance
- Better prompt templates
- Additional examples
- Documentation improvements
- Website enhancements

### Pull Requests

1. **Fork the repository**
   ```bash
   git clone https://github.com/weykon/ralph-prompt-prep.git
   cd ralph-prompt-prep
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow existing code style
   - Update documentation if needed
   - Test your changes

4. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of your changes"
   ```

5. **Push and create PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Then create a Pull Request on GitHub

## Development Guidelines

### Skill Development

When modifying the `ralph-prompt-prep` skill:

- **Maintain conversational tone**: The skill should feel natural, not robotic
- **Keep it focused**: Help users create good Ralph prompts, don't try to do everything
- **Test thoroughly**: Try the skill with various scenarios
- **Update examples**: If you change the template, update examples too

### Documentation

- Use clear, concise language
- Include examples for complex concepts
- Keep README.md as the main entry point
- Update USAGE.md for detailed instructions

### Website

- Maintain responsive design (mobile + desktop)
- Keep the design simple and clean
- Ensure fast loading times
- Test on multiple browsers

## Code Style

### Markdown
- Use ATX-style headers (`#` not underlines)
- One sentence per line in paragraphs
- Code blocks with language specification

### Shell Scripts
- Use `#!/bin/bash` shebang
- Include error handling (`set -e`)
- Add comments for complex logic
- Make scripts executable (`chmod +x`)

### HTML/CSS
- Use semantic HTML5 elements
- Mobile-first responsive design
- Inline CSS for single-page sites
- Comment complex CSS rules

## Testing

Before submitting a PR:

1. **Test the skill**
   ```bash
   /ralph-prompt-prep "test task description"
   ```

2. **Verify documentation**
   - Check all links work
   - Ensure examples are accurate
   - Verify installation instructions

3. **Test website locally**
   ```bash
   python3 -m http.server 8000
   # Visit http://localhost:8000
   ```

4. **Check for typos**
   - Run spell check on documentation
   - Review commit messages

## Project Structure

```
ralph-prompt-prep/
├── .claude/
│   └── skills/
│       └── ralph-prompt-prep/
│           └── SKILL.md          # Main skill file
├── examples_improved.md          # Before/after examples
├── quick_reference.md            # Quick start guide
├── ralph-prompt-builder.md       # Detailed framework
├── ralph_prompt_builder.py       # Interactive tool
├── README.md                     # Project overview
├── USAGE.md                      # Detailed usage guide
├── index.html                    # Website
├── install.sh                    # Installation script
└── LICENSE                       # MIT License
```

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
Add: new feature or file
Update: modify existing feature
Fix: bug fix
Docs: documentation changes
Style: formatting, no code change
Refactor: code restructuring
Test: add or update tests
```

Examples:
- `Add: installation script for easy setup`
- `Update: skill template with better examples`
- `Fix: typo in quick reference guide`
- `Docs: clarify validation steps in USAGE.md`

## Questions?

If you have questions about contributing:

- Open a [GitHub Discussion](https://github.com/weykon/ralph-prompt-prep/discussions)
- Check existing [Issues](https://github.com/weykon/ralph-prompt-prep/issues)
- Review the [documentation](https://weykon.github.io/ralph-prompt-prep/)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- GitHub contributors page
- Release notes (for significant contributions)
- README.md (for major features)

Thank you for helping make Ralph Prompt Prep better! 🎯

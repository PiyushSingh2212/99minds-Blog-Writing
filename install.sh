#!/usr/bin/env bash
# 99minds-Blog-Writing installer for Unix/macOS
# Usage: chmod +x install.sh && ./install.sh

set -euo pipefail

REPO_NAME="99minds-blog-writing"
SKILLS_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
AGENTS_DIR="${CLAUDE_AGENTS_DIR:-$HOME/.claude/agents}"
PLUGINS_DIR="${CLAUDE_PLUGINS_DIR:-$HOME/.claude/plugins}"

echo "Installing ${REPO_NAME}..."

# Create directories
mkdir -p "$SKILLS_DIR"
mkdir -p "$AGENTS_DIR"
mkdir -p "$PLUGINS_DIR"

# Copy skills
if [ -d "skills" ]; then
  cp -r skills/* "$SKILLS_DIR/"
  echo "Skills installed to $SKILLS_DIR"
fi

# Copy agents
if [ -d "agents" ]; then
  cp -r agents/* "$AGENTS_DIR/"
  echo "Agents installed to $AGENTS_DIR"
fi

# Copy plugin metadata
if [ -d ".claude-plugin" ]; then
  cp -r .claude-plugin "$PLUGINS_DIR/${REPO_NAME}"
  echo "Plugin metadata installed to $PLUGINS_DIR/${REPO_NAME}"
fi

echo ""
echo "Installation complete!"
echo "Restart Claude Code to activate ${REPO_NAME}."
echo ""
echo "Available commands:"
echo "  /blog write <topic>       - Write a new blog post"
echo "  /blog rewrite <file>      - Optimize an existing post"
echo "  /blog analyze <file>      - Quality audit (0-100 score)"
echo "  /blog seo-check <file>    - SEO validation"
echo "  /blog brief <topic>       - Generate a content brief"
echo "  /blog calendar            - Editorial calendar"
echo "  /blog strategy <niche>    - Blog strategy and topics"
echo "  /blog outline <topic>     - Content outline"
echo "  /blog schema <file>       - JSON-LD schema markup"
echo "  /blog repurpose <file>    - Repurpose for social/email"
echo "  /blog audit [dir]         - Full site health check"
echo "  /blog persona [cmd]       - Manage writing personas"
echo "  /blog factcheck <file>    - Verify statistics"

# 99minds-Blog-Writing installer for Windows PowerShell
# Usage: .\install.ps1

$ErrorActionPreference = "Stop"

$RepoName = "99minds-blog-writing"
$SkillsDir = if ($env:CLAUDE_SKILLS_DIR) { $env:CLAUDE_SKILLS_DIR } else { "$env:USERPROFILE\.claude\skills" }
$AgentsDir = if ($env:CLAUDE_AGENTS_DIR) { $env:CLAUDE_AGENTS_DIR } else { "$env:USERPROFILE\.claude\agents" }
$PluginsDir = if ($env:CLAUDE_PLUGINS_DIR) { $env:CLAUDE_PLUGINS_DIR } else { "$env:USERPROFILE\.claude\plugins" }

Write-Host "Installing $RepoName..." -ForegroundColor Cyan

# Create directories
New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null
New-Item -ItemType Directory -Force -Path $AgentsDir | Out-Null
New-Item -ItemType Directory -Force -Path $PluginsDir | Out-Null

# Copy skills
if (Test-Path "skills") {
    Copy-Item -Recurse -Force "skills\*" $SkillsDir
    Write-Host "Skills installed to $SkillsDir" -ForegroundColor Green
}

# Copy agents
if (Test-Path "agents") {
    Copy-Item -Recurse -Force "agents\*" $AgentsDir
    Write-Host "Agents installed to $AgentsDir" -ForegroundColor Green
}

# Copy plugin metadata
if (Test-Path ".claude-plugin") {
    $pluginTarget = Join-Path $PluginsDir $RepoName
    Copy-Item -Recurse -Force ".claude-plugin" $pluginTarget
    Write-Host "Plugin metadata installed to $pluginTarget" -ForegroundColor Green
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Cyan
Write-Host "Restart Claude Code to activate $RepoName."
Write-Host ""
Write-Host "Available commands:"
Write-Host "  /blog write <topic>       - Write a new blog post"
Write-Host "  /blog rewrite <file>      - Optimize an existing post"
Write-Host "  /blog analyze <file>      - Quality audit (0-100 score)"
Write-Host "  /blog seo-check <file>    - SEO validation"
Write-Host "  /blog brief <topic>       - Generate a content brief"
Write-Host "  /blog calendar            - Editorial calendar"

# Release Guide

This document describes the automated release process for the Digital Casting System.

## Quick Release

### Using Invoke Tasks (Recommended for Development)

```bash
# Check everything is ready for release
invoke release-check

# Create a patch release (0.1.0 -> 0.1.1)
invoke release

# Create a minor release (0.1.0 -> 0.2.0)
invoke release --part minor

# Create a major release (0.1.0 -> 1.0.0)  
invoke release --part major

# Dry run to see what would happen
invoke release --dry-run
```

### Using GitHub Actions (Automated)

#### Manual Release
1. Go to Actions tab in GitHub repository
2. Select "Release" workflow  
3. Click "Run workflow"
4. Choose version part (patch/minor/major)
5. Run the workflow

#### Automatic Release (on commits to main)
The system automatically creates releases based on conventional commit messages:

- `feat:` → Minor release (new features)
- `fix:` → Patch release (bug fixes)  
- `feat!:` or `BREAKING CHANGE:` → Major release (breaking changes)
- `[release]` → Manual patch release trigger

## Version Management

The project uses [bump-my-version](https://pypi.org/project/bump-my-version/) for automated version management:

- **Current version**: Stored in `pyproject.toml` and `src/dcs/__init__.py`
- **Versioning scheme**: [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH)
- **Tags**: Automatically created as `vX.Y.Z`

## Changelog Management

The changelog follows [Keep a Changelog](https://keepachangelog.com/) format:

- **Location**: `CHANGELOG.md`
- **Format**: `## [Version] - YYYY-MM-DD`
- **Automatic updates**: Version headers are added automatically
- **Manual edits**: Add your changes under `## Unreleased` section

## GitHub Actions Workflows

### Release Workflow (`release.yml`)
- **Trigger**: Manual dispatch with version part selection
- **Features**: Pre-release checks, version bumping, tag creation, GitHub release
- **Dry run support**: Test releases without making changes

### Automated Release Workflow (`auto-release.yml`)  
- **Trigger**: Push to main/master with conventional commits
- **Features**: Automatic version detection, release creation
- **Smart detection**: Analyzes commit messages for release type

## Local Development Workflow

```bash
# 1. Make your changes
# 2. Update CHANGELOG.md under "Unreleased" section
# 3. Run pre-release checks
invoke release-check

# 4. Create release (if checks pass)
invoke release --part patch

# 5. Push changes and tags
git push origin main --follow-tags
```

## Publishing to PyPI

The automated workflows can publish to PyPI if `PYPI_API_TOKEN` secret is configured:

1. Go to repository Settings → Secrets and variables → Actions
2. Add secret named `PYPI_API_TOKEN` with your PyPI token
3. Releases will automatically publish to PyPI when pushed to main branch

## Available Invoke Tasks

```bash
invoke --list                    # List all available tasks
invoke clean                     # Clean build artifacts
invoke lint                      # Run linting
invoke lint --fix                # Fix linting issues  
invoke test                      # Run tests
invoke build                     # Build package
invoke docs                      # Build documentation
invoke docs --serve              # Serve docs locally
invoke release-check             # Pre-release validation
invoke version-bump --part minor # Bump version only
invoke release --part major      # Full release process
```

## Troubleshooting

### Working Directory Not Clean
```bash
git status                       # Check what's changed
git add . && git commit -m "..."  # Commit changes
# or
git stash                        # Stash changes temporarily
```

### Release Checks Fail
```bash
invoke lint --fix               # Fix linting issues
invoke test                     # Check test failures
invoke clean && invoke build    # Clean rebuild
```

### Version Conflicts
```bash
bump-my-version show current_version  # Check current version
git tag --list | tail -5             # Check recent tags
```
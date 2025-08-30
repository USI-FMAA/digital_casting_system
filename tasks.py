from pathlib import Path

from invoke import task

from _gen_ref_pages import generate_api_reference


@task
def format(ctx, fix: bool = False):
  """Format the code using ruff."""
  filepath = Path("./src") / "dcs"
  matches = list(filepath.rglob("*.py"))
  files = " ".join(str(f) for f in matches)
  cmd = f"ruff format {files}"
  if fix:
    cmd += " --fix"
  ctx.run(cmd, pty=True)


@task
def test(ctx, verbose: bool = False):
  """Run tests with pytest (0.3 seconds)."""
  cmd = "python -m pytest"
  if verbose:
    cmd += " -v"
  print("Running tests...")
  ctx.run(cmd, pty=True)


@task
def docs(ctx, serve: bool = False):
  """Build documentation with auto-generated API reference."""
  print("Building documentation with auto-generated API reference...")

  if serve:
    print("Serving documentation at http://127.0.0.1:8000")
    ctx.run("mkdocs serve", pty=True)
  else:
    generate_api_reference()
    ctx.run("mkdocs build", pty=True)
    print("Documentation built successfully!")


@task
def docs_clean(ctx):
  """Clean generated documentation files."""
  print("Cleaning generated documentation...")
  ctx.run("rm -rf docs/api/reference/", pty=True)
  ctx.run("rm -rf dist/", pty=True)
  print("Documentation cleaned!")


@task
def lint(ctx, fix: bool = False):
  """Run linting with ruff."""
  cmd = "ruff check"
  if fix:
    cmd += " --fix"
  ctx.run(cmd, pty=True)


@task
def clean(ctx):
  """Clean build artifacts and cache files."""
  print("Cleaning build artifacts...")
  ctx.run("rm -rf dist/", pty=True)
  ctx.run("rm -rf build/", pty=True)
  ctx.run("rm -rf *.egg-info/", pty=True)
  ctx.run("find . -type d -name __pycache__ -exec rm -rf {} +", pty=True)
  ctx.run("find . -type f -name '*.pyc' -delete", pty=True)
  print("Clean complete!")


@task
def build(ctx):
  """Build the package distribution."""
  print("Building package...")
  ctx.run("uv build", pty=True)
  print("Build complete!")


@task
def release_check(ctx):
  """Run all checks before release."""
  print("Running pre-release checks...")

  # Check if working directory is clean
  result = ctx.run("git status --porcelain", hide=True)
  if result.stdout.strip():
    print("Error: Working directory is not clean. Commit or stash changes first.")
    return False

  # Run linting
  print("Running linting...")
  ctx.run("ruff check", pty=True)

  # Run tests
  print("Running tests...")
  ctx.run("python -m pytest -v", pty=True)

  # Build package
  print("Building package...")
  ctx.run("uv build", pty=True)

  print("All pre-release checks passed!")
  return True


@task
def version_bump(ctx, part="patch"):
  """Bump version using bump-my-version.

  Args:
    part: Version part to bump (patch, minor, major)
  """
  if not release_check(ctx):
    return

  print(f"Bumping {part} version...")
  ctx.run(f"bump-my-version bump {part}", pty=True)

  # Get new version
  result = ctx.run("bump-my-version show current_version", hide=True)
  new_version = result.stdout.strip()
  print(f"Version bumped to: {new_version}")


@task
def release(ctx, part="patch", dry_run=False):
  """Create a release with version bump, changelog update, and tag.

  Args:
    part: Version part to bump (patch, minor, major)
    dry_run: Show what would be done without making changes
  """
  if dry_run:
    print(f"DRY RUN: Would bump {part} version and create release")
    return

  if not release_check(ctx):
    return

  print(f"Creating {part} release...")

  # Bump version and create tag
  version_bump(ctx, part)

  # Build package
  build(ctx)

  print("Release created successfully!")
  print("To publish to PyPI, run: twine upload dist/*")
  print("Don't forget to push the tag: git push origin --tags")

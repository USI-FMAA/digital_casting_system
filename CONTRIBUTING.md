# Contributing

Contributions are welcome and very much appreciated!

## Code contributions

We accept code contributions through pull requests.
In short, this is how that works.

1. Fork [the repository](https://github.com/USI-FMAA/dcs) and clone the fork.
2. Create a virtual environment using your tool of choice (e.g. `virtualenv`, `conda`, etc).
3. Install development dependencies:

   ```bash
   pip install -r requirements-dev.txt
   ```

4. Make sure all tests pass:

   ```bash
   invoke test
   ```

5. Start making your changes to the **master** branch (or branch off of it).
6. Make sure all tests still pass:

   ```bash
   invoke test
   ```

7. Add yourself to the *Contributors* section of `AUTHORS.md`.
8. Commit your changes and push your branch to GitHub.
9. Create a [pull request](https://help.github.com/articles/about-pull-requests/) through the GitHub website.

During development, use [pyinvoke](http://docs.pyinvoke.org/) tasks on the
command line to ease recurring operations:

* `invoke clean`: Clean all generated artifacts.
* `invoke check`: Run various code and documentation style checks.
* `invoke docs`: Generate documentation.
* `invoke test`: Run all tests and checks in one swift command.
* `invoke build`: Build the package for distribution.
* `invoke build-release`: Build a release with automatic version bumping and tagging.
* `invoke gh-release`: Create GitHub release using GitHub CLI - automatically detects tag.
* `invoke`: Show available tasks.

## Releases

Releases are automated via GitHub Actions. To create a new release:

1. **Manual Release Process**:
   ```bash
   # Bump version and create tag (patch/minor/major)
   invoke build-release --part=patch
   
   # Push tags to trigger automated release
   git push origin --tags
   ```

2. **Automated Release Process**:
   - The GitHub Actions workflow (`.github/workflows/release.yml`) automatically triggers on tag pushes
   - Builds the package using `uv build`
   - Creates a GitHub release with changelog notes using `invoke gh-release`
   - Uploads wheel and source distribution as release assets

3. **Release Artifacts**:
   - Python wheel (`.whl`)
   - Source distribution (`.tar.gz`)
   - Automated release notes from changelog

## Bug reports

When [reporting a bug](https://github.com/USI-FMAA/dcs/issues) please include:

* Operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

## Feature requests

When [proposing a new feature](https://github.com/USI-FMAA/dcs/issues) please include:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

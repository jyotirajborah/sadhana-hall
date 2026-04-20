# Push to GitHub Instructions

Your local repository is ready! Follow these steps:

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `upasana-landing-page` (or your choice)
3. Description: "UPASANA - Integrated Yoga, Meditation & Cultural Education Centre"
4. Choose Public or Private
5. **DO NOT** check "Initialize with README" (we already have one)
6. Click "Create repository"

## Step 2: Connect and Push

After creating the repository on GitHub, run these commands:

```bash
# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/upasana-landing-page.git

# Rename branch to main (GitHub's default)
git branch -M main

# Push to GitHub
git push -u origin main
```

## Alternative: Using GitHub CLI

If you have GitHub CLI installed:

```bash
gh repo create upasana-landing-page --public --source=. --remote=origin --push
```

## Step 3: Verify

After pushing, visit your repository URL:
https://github.com/YOUR_USERNAME/upasana-landing-page

## Future Updates

After making changes to your files:

```bash
# Stage all changes
git add .

# Commit with a message
git commit -m "Your commit message here"

# Push to GitHub
git push
```

## Current Status

✓ Git repository initialized
✓ All files committed locally
✓ Ready to push to GitHub

## Files Committed (20 files):

- index.html (main landing page)
- README.md (project documentation)
- All documentation files (CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, etc.)
- All images in pics/ folder (8 images + chariot.jpeg)
- Configuration files (.gitignore, .gitattributes, CITATION.cff)
- Helper scripts (download-video.bat, VIDEO-SETUP.md)

## Note About Video File

The video file (video/hero-video.mp4) is excluded by .gitignore because it's too large for GitHub.
Users will need to download it separately using the instructions in VIDEO-SETUP.md.

## Need Help?

If you encounter authentication issues:
1. GitHub may ask for credentials
2. Use a Personal Access Token instead of password
3. Generate token at: https://github.com/settings/tokens
4. Or use GitHub Desktop app for easier authentication

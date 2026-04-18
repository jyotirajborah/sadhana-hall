@echo off
echo ========================================
echo UPASANA Chariot Video Downloader
echo ========================================
echo.

REM Check if yt-dlp is installed
where yt-dlp >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: yt-dlp is not installed!
    echo.
    echo Please install yt-dlp first:
    echo   1. Run: winget install yt-dlp
    echo   2. Or download from: https://github.com/yt-dlp/yt-dlp/releases
    echo.
    pause
    exit /b 1
)

REM Create video folder if it doesn't exist
if not exist "video" mkdir video

echo Downloading video from YouTube...
echo URL: https://www.youtube.com/watch?v=0Tnge4d0Vw0
echo Saving to: video\chariot-video.mp4
echo.

yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "video/chariot-video.mp4" https://www.youtube.com/watch?v=0Tnge4d0Vw0

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo SUCCESS! Video downloaded successfully!
    echo ========================================
    echo.
    echo File saved as: video\chariot-video.mp4
    echo The video will now loop seamlessly in the chariot section.
    echo.
) else (
    echo.
    echo ========================================
    echo ERROR: Download failed!
    echo ========================================
    echo.
    echo Please try:
    echo   1. Check your internet connection
    echo   2. Verify the YouTube URL is accessible
    echo   3. Use an online converter instead
    echo.
)

pause

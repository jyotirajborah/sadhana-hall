# Hero Video Background Setup

The hero section is configured to use a video background. Follow these steps to add the video:

## Option 1: Download from YouTube (Recommended)

### Using yt-dlp (Command Line)

1. **Install yt-dlp:**
   ```bash
   # Windows (using winget)
   winget install yt-dlp
   
   # Or download from: https://github.com/yt-dlp/yt-dlp/releases
   ```

2. **Download the video:**
   ```bash
   yt-dlp -f "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best" -o "video/hero-video.mp4" https://www.youtube.com/watch?v=xg7dmFsVEZ4
   ```

3. **Place the video:**
   - Save the downloaded `hero-video.mp4` in the `video` folder
   - Create the `video` folder if it doesn't exist

### Using Online Converter

1. Go to one of these sites:
   - https://y2mate.com
   - https://ytmp3.cc
   - https://savefrom.net

2. Paste the YouTube URL: `https://www.youtube.com/watch?v=xg7dmFsVEZ4`

3. Download as MP4 (1080p or 720p recommended)

4. Rename the file to `hero-video.mp4`

5. Place it in the `video` folder (create the folder if needed)

## Option 2: Use Your Own Video

If you have your own video file:

1. Convert it to MP4 format (if needed)
2. Rename it to `hero-video.mp4`
3. Place it in the `video` folder
4. Recommended specs:
   - Format: MP4 (H.264 codec)
   - Resolution: 1920x1080 or 1280x720
   - File size: Under 10MB for faster loading
   - Duration: 10-30 seconds (it will loop)

## Video Optimization Tips

For better performance, compress your video:

```bash
# Using ffmpeg (if installed)
ffmpeg -i original-video.mp4 -vcodec h264 -acodec aac -b:v 2M -b:a 128k hero-video.mp4
```

## Fallback Behavior

If the video file is not found or fails to load:
- The page will automatically fall back to the static image background
- No errors will be shown to users
- The page will function normally

## Current Setup

- Video file expected: `video/hero-video.mp4`
- Video opacity: 25% (subtle background effect)
- Video settings: Autoplay, muted, looping
- Fallback image: Unsplash meditation image

## Testing

After adding the video:
1. Open `index.html` in your browser
2. The video should play automatically in the background
3. Check browser console (F12) for any errors
4. If video doesn't play, check:
   - File name is exactly `hero-video.mp4`
   - File is in the `video` folder
   - File format is MP4
   - Browser supports the video codec

## Browser Compatibility

The video background works in:
- ✓ Chrome/Edge (all versions)
- ✓ Firefox (all versions)
- ✓ Safari (all versions)
- ✓ Mobile browsers (with autoplay restrictions)

Note: Some mobile browsers may not autoplay videos. The fallback image will show instead.

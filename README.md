# yuv2rgb
You can use `https://convertio.co/` to convert JPEG to YUV in order to get I420 YUV file.

Or use ffmpeg:
ffmpeg.exe -i test.png -s 1920x1080 -pix_fmt nv12 test_nv12.yuv
ffmpeg.exe -i test.png -s 1920x1080 -pix_fmt nv21 test_nv21.yuv

Use this I420 YUV file to convert to RGB image and display.

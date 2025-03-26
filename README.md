# YouTube字幕获取工具

这是一个简单的Python工具，用于获取YouTube视频的字幕内容。

## 功能特点

- 支持获取中文和英文字幕
- 自动格式化字幕输出
- 简单易用的命令行界面

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 运行程序：
```bash
python main.py
```

2. 输入YouTube视频ID（可以从视频URL中获取，例如：https://www.youtube.com/watch?v=VIDEO_ID）

3. 程序会自动获取并显示字幕内容

## 注意事项

- 视频必须有可用的字幕
- 优先获取中文字幕，如果没有则尝试获取英文字幕
- 需要稳定的网络连接 
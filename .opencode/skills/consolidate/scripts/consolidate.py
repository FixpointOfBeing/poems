import os
import re
from pathlib import Path
from datetime import datetime

def consolidate_poems():
    # 获取当前工作目录
    workspace =  Path.home() / "Workspace/poems"
    build_dir = workspace / ".build"
    output_file = build_dir / "consolidated_poems.txt"

    # 确保 .build 文件夹存在
    build_dir.mkdir(exist_ok=True)

    # 匹配文件名格式：<文件名>_YYYY-MM-DD.txt
    # 允许月份和日期为一位或两位数
    pattern = re.compile(r"(.+)_(\d{4}-\d{1,2}-\d{1,2})\.txt$")

    poem_data = []

    # 扫描当前目录下的文件
    for file_path in workspace.iterdir():
        if file_path.is_file():
            match = pattern.match(file_path.name)
            if match:
                poem_name = match.group(1)
                date_str = match.group(2)
                try:
                    # 将日期字符串转换为 datetime 对象以便排序
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    poem_data.append({
                        "path": file_path,
                        "date": date_obj,
                        "title": poem_name
                    })
                except ValueError:
                    print(f"跳过日期格式错误的文件: {file_path.name}")

    # 按时间顺序排序
    poem_data.sort(key=lambda x: x["date"])

    if not poem_data:
        print("未找到符合格式的诗歌文件。")
        return

    # 写入合并文件
    size = 0
    with open(output_file, "w", encoding="utf-8") as outfile:
        for entry in poem_data:
            with open(entry["path"], "r", encoding="utf-8") as infile:
                content = infile.read()
                if not content:
                    continue
                # 写入标题和日期作为分隔
                outfile.write(f"--- {entry['title']} ({entry['date'].strftime('%Y-%m-%d')}) ---\n\n")
                outfile.write(content)
                outfile.write("\n\n") # 诗歌间的空行
                size += 1

    print(f"已成功将 {size} 首诗歌整合至: {output_file}")

if __name__ == "__main__":
    consolidate_poems()

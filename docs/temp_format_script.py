#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to format markdown files with proper headings and bullet points.
Preserves all content, only adds markdown formatting.
"""

import re

def format_file_7_2():
    """Format file 7.2 腸胃問題.md"""
    with open('/Users/chris/drochiu/docs/7. 長期病/7.2 腸胃問題.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add main title
    content = re.sub(r'^食道炎 Oesophagitis', r'# 食道炎 Oesophagitis', content)

    # Add section headings
    content = re.sub(r'\n症狀 :\s*\n', r'\n## 症狀\n', content)
    content = re.sub(r'\n成因 :\s*\n', r'\n## 成因\n', content)
    content = re.sub(r'\n食道炎的併發症 :\s*\n', r'\n## 食道炎的併發症\n', content)

    # Format lists after 成因
    content = re.sub(
        r'(## 成因\n\n)(胃酸逆流.*?\n\n)(感染：.*?\n\n)(藥物：.*?\n\n)(過敏：.*?\n\n)(其他因素：.*?\n)',
        r'\1- **\2- **\3- **\4- **\5- **\6',
        content, flags=re.DOTALL
    )

    #Add main heading for 胃炎
    content = re.sub(r'\n胃炎、胃潰瘍和十二指腸潰瘍\n', r'\n# 胃炎、胃潰瘍和十二指腸潰瘍\n', content)

    # Add section for symptoms
    content = re.sub(r'\n胃炎、胃潰瘍和十二指腸潰瘍症狀：\n', r'\n## 胃炎、胃潰瘍和十二指腸潰瘍症狀\n', content)

    # Add section for causes
    content = re.sub(r'\n胃炎、胃潰瘍和十二指腸潰瘍成因：\n', r'\n## 胃炎、胃潰瘍和十二指腸潰瘍成因\n', content)

    # Add treatment heading
    content = re.sub(r'\n治療 :\s*\n', r'\n## 治療\n', content)

    # Add subsections
    content = re.sub(r'\n生活方式改變 :', r'\n### 生活方式改變', content)
    content = re.sub(r'\n戒食引發胃酸分泌過多 和 胃酸逆流的食物, 例如 :\s*\n', r'\n### 戒食引發胃酸分泌過多和胃酸逆流的食物\n\n例如：\n', content)

    # Add 便秘 heading
    content = re.sub(r'\n\s*便秘\n', r'\n# 便秘\n', content)
    content = re.sub(r'\n便秘的成因 :\s*\n', r'\n## 便秘的成因\n', content)
    content = re.sub(r'\n常見的症狀：\n', r'\n## 常見的症狀\n', content)
    content = re.sub(r'\n便秘的併發症：\n', r'\n## 便秘的併發症\n', content)
    content = re.sub(r'\n治療 :\s*\n', r'\n## 治療\n', content, count=1)

    # Add IBS heading
    content = re.sub(r'\n腸易激綜合症 Irritable Bowel Syndrome（IBS）\n', r'\n# 腸易激綜合症 Irritable Bowel Syndrome（IBS）\n', content)

    # Add lactose intolerance heading
    content = re.sub(r'\n乳糖不耐症 Lactose intolerance\n', r'\n# 乳糖不耐症 Lactose intolerance\n', content)

    with open('/Users/chris/drochiu/docs/7. 長期病/7.2 腸胃問題.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("File 7.2 formatted successfully")

def format_file_7_3():
    """Format file 7.3 精神健康問題.md"""
    with open('/Users/chris/drochiu/docs/7. 長期病/7.3 精神健康問題.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Add main titles
    content = re.sub(r'^頭痛\s*\n', r'# 頭痛\n', content)
    content = re.sub(r'\n緊張型頭痛 Tension Headache\s*\n', r'\n# 緊張型頭痛 Tension Headache\n', content)
    content = re.sub(r'\n偏頭痛 Migraine\n', r'\n# 偏頭痛 Migraine\n', content)
    content = re.sub(r'\n抑鬱症 Depression\n', r'\n# 抑鬱症 Depression\n', content)
    content = re.sub(r'\n焦慮症 Anxiety Disorder\n', r'\n# 焦慮症 Anxiety Disorder\n', content)
    content = re.sub(r'\n球狀癥狀 Globus Hystericus\n', r'\n# 球狀癥狀 Globus Hystericus\n', content)
    content = re.sub(r'\n神經衰弱 Neurasthenia\n', r'\n# 神經衰弱 Neurasthenia\n', content)
    content = re.sub(r'\n暗瘡 \(痤瘡\) Acne\n', r'\n# 暗瘡 (痤瘡) Acne\n', content)

    # Add section headings
    content = re.sub(r'\n頭痛的原因：\n', r'\n## 頭痛的原因\n', content)
    content = re.sub(r'\n生活方式的原因：\n', r'\n### 生活方式的原因\n', content)
    content = re.sub(r'\n原因 :\s*\n', r'\n## 原因\n', content)
    content = re.sub(r'\n症狀 :\s*\n', r'\n## 症狀\n', content)
    content = re.sub(r'\n治療方法 :\s*\n', r'\n## 治療方法\n', content)
    content = re.sub(r'\n病因 :\s*\n', r'\n## 病因\n', content)
    content = re.sub(r'\n治療方式 :\s*\n', r'\n## 治療方式\n', content)
    content = re.sub(r'\n治療 :\s*\n', r'\n## 治療\n', content)

    with open('/Users/chris/drochiu/docs/7. 長期病/7.3 精神健康問題.md', 'w', encoding='utf-8') as f:
        f.write(content)

    print("File 7.3 formatted successfully")

if __name__ == '__main__':
    format_file_7_2()
    format_file_7_3()
    print("All files formatted!")

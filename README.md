# DeepSeek 96MB TXT 样本：沈策古风剧情设定

本仓库收录一份被称为“DeepSeek 96MB TXT”的文本样本，文件名为 **沈策古风剧情设定完整版.txt**。文件内容是一套虚构的古风／武侠人物档案，围绕沈策展开。

> **来源说明：**“DeepSeek 96MB TXT”是用于识别和检索这份样本的传播标签，不是来源证明。仅凭文件内容无法独立确认它由 DeepSeek、其他模型、人工创作或多种方式共同生成，也无法据此证明它来自任何平台的数据泄露。

## 文件信息

| 项目 | 信息 |
| --- | --- |
| 文件 | [沈策古风剧情设定完整版.txt](./沈策古风剧情设定完整版.txt) |
| 编码 | UTF-8 |
| 大小 | 100,683,627 bytes（约 96.02 MiB） |
| 字符数 | 34,305,593 |
| 行数 | 935,682 |

## 内容概览

文本采用仿档案体，包含沈策的生平、逐日编年、旧案卷宗、人物关系、往来书信、武学、器物和江湖异闻。逐日记录从永嘉十四年延伸至永嘉八十八年，共解析出 26,910 个日期标题。

## Python 结构分析

对文本进行 UTF-8 解码、章节与日期正则解析、行频统计后，观察到：

- 去除首尾空白后，904,273 条非空行中有 98,685 条不同文本行，约占 10.91%；若干句子重复数千次。
- 全文有 925 处 `初undefined`；其中 897 处出现在逐日编年标题中，对应初十。另有 51 条“后人评”标题的序号含 `undefined`。
- 文件呈现出较强的模板化扩写特征；这些文本特征不能确定具体作者或生成模型。

这些统计描述的是文件本身，不构成对文件来源、作者身份或传播链的鉴定。

## English summary

This repository preserves a UTF-8 Chinese wuxia character dossier titled **沈策古风剧情设定完整版.txt** (Shen Ce: Complete Wuxia Character Setting). It is commonly labeled online as a “DeepSeek 96MB TXT” sample, but the file alone does not verify its origin or prove a data leak. The repository includes Python-derived statistics on its structure, repeated lines, chronology, and visible `undefined` artifacts.

**Search terms:** DeepSeek 96MB TXT, 沈策古风剧情设定, 沈策 TXT, Chinese wuxia character dossier.

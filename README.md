# 旅行决策手册

把每一次「即兴出发」的调研做成一页可分享的决策网站，长期留档、持续迭代。

**在线访问：**

- 决策手册（7 月即兴出发）：https://dylan-kong.github.io/travel-decision-book/
- 转角遇见世界（2026 夏季出发方案）：https://dylan-kong.github.io/travel-decision-book/travel-radar-2026.html
- 考证之夏（8 月潜水学习地对比）：https://dylan-kong.github.io/travel-decision-book/learn-dive-2026.html

## 这是什么

单文件静态网站（无任何依赖、无构建框架），一页内包含：

- 候选目的地棋盘：签证、航程、当季气候、主线契合度、预算，可筛选
- 深度方案：逐日行程、不开车的交通解法、预算明细、当地资源与联系人
- 预算对比图、项目制旅行平台库、出发前行动清单

第一期是 2026 年 7 月的北京出发计划（格鲁吉亚 / 土耳其 / 曼谷）。

## 目录结构

```
index.html          发布页（由 build.py 生成，图片已内嵌，勿手改）
src/template.html   页面源码（要改内容改这里）
src/img/            目的地照片（来自 Wikimedia Commons）
src/build.py        构建脚本：把图片以 base64 内嵌进模板，输出 index.html
```

## 怎么更新

```bash
# 1. 修改页面内容
open src/template.html

# 2. 重新生成 index.html
python3 src/build.py

# 3. 提交并推送（GitHub Pages 一两分钟后自动更新）
git add -A
git commit -m "更新行程"
git push
```

每次新的旅行计划建议走一个新分支加 Pull Request，这样每一期方案在 PR 历史里都有完整存档。

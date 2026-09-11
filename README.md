# python-practice · Python 练习 + Git 上手

这是你的第一个 GitHub 仓库。两个用途：

1. **练 Python**：8 个从易到难的练习（农业主题），用「模仿示例 → 自己改」的方式上手
2. **练 Git**：每天把练习代码提交到 GitHub，攒绿格子

---

## 第一部分：VS Code → GitHub 全流程（跟着做一遍就会了）

### 第 0 步：用 VS Code 打开这个文件夹

两种方式任选：

- 打开 VS Code → 文件(File) → 打开文件夹(Open Folder) → 选 `D:\Projects\python-practice`
- 或者打开 CMD，输入：`code D:\Projects\python-practice`

> 以后每天的流程都是：VS Code 打开这个文件夹 → 写代码 → 提交。

### 第 1 步：在 VS Code 里打开终端

菜单栏：**终端(Terminal) → 新建终端(New Terminal)**
然后点终端右上角的下拉箭头，选择 **Command Prompt（cmd）**。
（你习惯用 CMD，就这么选。如果默认就是 cmd 就跳过这步。）

### 第 2 步：检查 Git 认不认识你（你之前已经配好了，验证一下）

```cmd
git config --global user.name
git config --global user.email
```

如果输出是 `pptpppt` 和 `2322358814@qq.com`，说明身份没问题，直接下一步。

### 第 3 步：把这个文件夹变成 Git 仓库（只需要做一次）

在终端里输入：

```cmd
cd /d D:\Projects\python-practice
git init
git add .
git commit -m "first commit: python practice"
```

> 解释一下这三条命令：
> - `git init`：把当前文件夹变成 Git 仓库（会出现一个隐藏的 `.git` 文件夹，别删它）
> - `git add .`：把当前所有文件放进「待提交区」（临时放行李的地方）
> - `git commit -m "说明"`：正式存档一次，`-m` 后面写这次改了什么

**你以后每次写完代码，都重复 `git add .` + `git commit -m "..."`，这就是「存档」。**

### 第 4 步：去 GitHub 建一个空仓库（只需要做一次）

1. 浏览器打开 https://github.com → 登录 `pptpppt`
2. 右上角 + 号 → **New repository**
3. Repository name 填：`python-practice`
4. 选 **Public**（免费 + 作品集要给别人看）
5. **不要勾选** Add a README（我们本地已经有了，避免冲突）
6. 点 **Create repository**

建好后页面会显示几行命令，别照抄它的（那套不匹配你已有的文件），用下面的。

### 第 5 步：生成一个「访问令牌」（只需要做一次）

GitHub 现在不允许用密码 push，要用令牌（Token）：

1. 右上角头像 → **Settings**
2. 左侧最底下 **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. 点 **Generate new token (classic)**
4. Note 随便写（比如 `vs code push`），Expiration 选 90 天
5. 勾选 **repo** 那一整项（前两个 checkbox 全勾上）
6. 点 **Generate token** → **立刻复制保存**（只显示一次，关掉就没了）

### 第 6 步：连接远程仓库并推送（第一次 push）

回到 VS Code 终端，输入（先别急，看下面说明）：

```cmd
git remote add origin https://github.com/pptpppt/python-practice.git
git branch -M main
git push -u origin main
```

执行到 `git push` 时会弹窗让你登录 GitHub：
- 选 **Sign in with your browser**（浏览器登录最省事）
- 浏览器登录完成后，如果提示"无法登录/需要认证"，就改用下面这种手动方式：

```cmd
git push -u origin main
```
此时它提示输入用户名时填 `pptpppt`，密码那一栏**粘贴刚才的 Token**（不是你的 QQ 邮箱密码！）。

看到 `main -> main` 之类的输出，就成功了！去 https://github.com/pptpppt/python-practice 刷新，代码已经在上面了。

> 三条命令解释：
> - `git remote add origin <网址>`：告诉 Git「远程仓库在哪」（仓库名和 GitHub 用户名一致，如果第 4 步改名了要同步改）
> - `git branch -M main`：把默认分支命名为 `main`（GitHub 现在统一用 main）
> - `git push -u origin main`：把本地存档推到 GitHub，`-u` 记住以后直接 `git push` 就行

### 第 7 步：以后每天的固定流程（攒绿格子）

```cmd
cd /d D:\Projects\python-practice
git add .
git commit -m "day X: 完成了练习 X"
git push
```

每次 `git push` 成功，GitHub 上就多一个绿格子。**连着做，别断。**

---

## 常见问题

| 问题 | 原因 / 解决 |
|---|---|
| `git push` 一直要密码 | 密码框里粘贴 **Token**，不是 QQ 密码 |
| `remote: Repository not found` | 仓库名或用户名拼错了，检查第 4/6 步网址 |
| `fatal: Not a git repository` | 忘记 `git init`，或者不在 `python-practice` 目录下 |
| push 被拒 (rejected) | 远程有仓库里没有的东西，先 `git pull origin main` 再 push |
| 打错 commit 说明 | `git commit --amend -m "新说明"`（刚 commit 完、还没 push 时用） |
| 想看改了什么 | `git status`（红色=没存档，绿色=已进待提交区） |

---

## 第二部分：8 个 Python 练习

玩法：**每个文件先看「模仿示例」，理解它怎么写的，再完成下面的任务**。完成任务不用背语法，照猫画虎就行。

| 文件 | 主题 | 知识点 | 难度 |
|---|---|---|---|
| day01_variables.py | 计算田块产量 | 变量、print、f-string、input | ⭐ |
| day02_condition.py | 温室温度报警 | if / elif / else、比较运算 | ⭐ |
| day03_loop.py | 一周温度统计 | for 循环、列表、sum/max | ⭐⭐ |
| day04_function.py | 产量计算器 | 函数、参数、返回值 | ⭐⭐ |
| day05_dict.py | 传感器数据管理 | 字典、遍历 | ⭐⭐⭐ |
| day06_project.py | 灌溉决策小工具 | 综合运用全部知识点 | ⭐⭐⭐ |
| day07_while_file.py | 温度录入器 | while 循环、break、文件读写 | ⭐⭐⭐ |
| day08_split_try.py | 大棚环境日志解析 | split 拆字符串、try/except 防崩溃 | ⭐⭐⭐ |
| day09_list_stats.py | 温度日报·列表统计 | append 建列表、len/sum/max/min、sorted、切片 | ⭐⭐⭐ |
| day10_dict_group.py | 农产品市场日报 | 字典频次统计、分组汇总、按值排序、max(d,key=d.get) | ⭐⭐⭐ |
| day11_csv_nested.py | 温室传感器周报 | csv.writer/DictReader、字典嵌套两步法、random.seed | ⭐⭐⭐ |

运行方式：VS Code 打开文件 → 右上角 ▶ 按钮（或按 F5），或者在终端里：

```cmd
cd /d D:\Projects\python-practice
python day01_variables.py
```

做不出来就看 `solutions\` 里对应答案，看懂后**关掉答案自己再敲一遍**——敲一遍的效果远大于看十遍。

---

## 第三部分：路线图（2026.9.11 定档）

> 2026.9.11 校园网提前通了，GitHub 推送恢复。同日定下：**Python 基础到 day20 收尾，day21 起不再按 day 编号，转入真实项目实战。**

| 阶段 | 天数 | 内容 | 状态 |
|---|---|---|---|
| 基础语法 | day01-08 | 变量、条件、循环、函数、字典、文件 I/O | ✅ 已完成 |
| 数据统计 | day09-11 | 列表统计、字典分组、CSV + 嵌套字典 | 🔄 day11 进行中 |
| 补齐地基 | day12-20 | 类、异常进阶、推导式、模块 import | ⬜ 待做 |
| 农业实战 | day21 起 | pandas 传感器数据分析、matplotlib 绘图 | ⬜ 未来 |

### day12-20 预设主题（可微调，大方向不变）

| Day | 主题 | 农业场景 |
|---|---|---|
| day12 | 类（class）入门 | 温室类：属性（温度/湿度）+ 方法（报警判断） |
| day13 | 类进阶：多个对象 | 多个温室实例、互相比较、列表装对象 |
| day14 | 异常进阶 | try/except/else/finally + raise，传感器脏数据防御 |
| day15 | 推导式 | 列表/字典推导式，一行顶一个 for |
| day16 | 模块与 import | 把代码拆成 tools.py + sensor.py + main.py |
| day17 | 综合项目①：温室管理器 | 多文件组织，综合运用 day12-16 |
| day18 | 综合项目②：功能补全 | 给管理器加导出 CSV、排序、检索功能 |
| day19 | 机动 / 复盘 | 补漏 + 整理 day12-18 笔记 |
| day20 | 地基收尾考核 | 不看任何参考，独立完成一个小项目 |

### day21 起怎么玩（预告）

不再每天一个新语法点，而是**围绕一个真实数据集干活**：读入传感器 CSV → pandas 清洗 → 统计分析 → matplotlib 出图 → 输出结论。这是从「会 Python」到「用 Python 干活」的过渡，也是以后接手实验室数据、做毕业设计数据处理的预演。

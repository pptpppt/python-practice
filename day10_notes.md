# day10 学习笔记

> 2026.09.10 · 主题：字典统计（农产品市场日报）

---

## 一、Python 报错就 3 大类

```
报错
├── 1. 跑之前就炸 —— 语法错（Python 看不懂你写的）
├── 2. 跑到一半炸 —— 运行时错（Python 看懂了，但做不到）
└── 3. 跑完了结果不对 —— 逻辑错（Python 全做完了，但你要的不是这个）
```

**第 3 类没有专门报错类型**，最隐蔽。其它两类有名字，看名字能定位。

---

## 二、第 1 类 · 语法错（跑不起来）

| 报错 | 翻译 | 今天踩过 |
|---|---|---|
| `SyntaxError: invalid syntax` | 语法 Python 不认识 | ✅ |
| `IndentationError: unexpected indent` | 不该缩进的地方缩进了 | ✅ |
| `IndentationError: expected an indented block` | 该缩进的地方没缩进 | ✅ |
| `TabError` | Tab 和空格混用 | ❌（警惕）|
| `SyntaxError: EOL while scanning string literal` | 引号没配对 | ❌ |

> **小技巧**：SyntaxError 最后一行用 `^` 指向出错位置附近，但**真正的错误往往在箭头之上**（少了个括号，关引号那行才报错）。

---

## 三、第 2 类 · 运行时错（最常见）

| 报错 | 翻译 | 今天踩过 | 例子 |
|---|---|---|---|
| **`NameError`** | 这名字我没见过 | ✅ | `max[k]` 漏 s、把变量名拼错 |
| **`TypeError`** | 类型不对 | ✅ | 函数当字典用、列表当 key、列表+数字 |
| `ValueError` | 类型对但值不合理 | ❌ | `int("abc")`、`unhashable: list` |
| `KeyError: 'xxx'` | 字典没这个键 | ❌ | `avg["不存在的"]` |
| `IndexError: list index out of range` | 列表越界 | ❌ | `a[10]` 但只有 3 个元素 |
| `ZeroDivisionError` | 除以零 | ❌ | `10 / 0` |
| `AttributeError` | 对象没这个属性 | ❌ | `"abc".push()` |
| `FileNotFoundError` | 文件不存在 | ❌ | `open("xxx")` |
| `ModuleNotFoundError` | 模块没装 | ❌ | `import numpy` 没装 |

> **看报错三步走**：
> 1. 报错类型 → 知道问题维度
> 2. 行号 → 跳过去看
> 3. 冒号后的具体文字 → 比如 `'builtin_function_or_method' object is not subscriptable` 立刻知道"把函数当字典用了"

---

## 四、第 3 类 · 逻辑错（最隐蔽）

**没有报错！** 程序跑完了，输出不是你想要的。

**今天的逻辑错案例**：

| 现象 | 真 bug |
|---|---|
| 5 行日报均价全是 2.4 | `avgs = round(...)` 写成了数字变量，字典 `avg` 一直空着 |
| 任务3 整行打印一坨字典 | f-string 里 `{avg}` 不是 `{avg[k]}` |
| 番茄均价错乱 | 任务2 边算边打印，没存进字典，循环外只剩最后一个 |
| 注释掉 print 后还缩进 | for 后面空了，Python 报 IndentationError |
| 把字典当列表遍历输出 | 字典应该 `[k]` 直接定位，不用遍历 |

> **查法**：拿输出和预期一行行对比，定位不对的那一列/行。

---

## 五、debug 四步法（按顺序查）

```
报错/结果不对
  ↓
① 报错类型是什么？ → 在第 2 节/第 3 节表里查
  ↓
② 有行号 → 直接跳过去
  ↓
③ 没报错（结果不对）→ 拿输出和预期一行行对比
  ↓
④ 四件套检查：
   · 引号/括号配没配对
   · 缩进对不对（VS Code 看左侧灰条）
   · 变量名拼写（max vs maxs、avgs vs avg）
   · 撞了内置函数（max/min/sum 别当变量名）
```

---

## 六、今天 day10 踩的 12 个坑（按教学顺序）

> 重要观察：**12 个全是语法细节级（引号/括号/缩进/拼写/类型），0 个是逻辑级。**
> 你的 bug 90% 出在符号上，不是想不通逻辑。

| # | 坑 | 分类 | 教训 |
|---|---|---|---|
| 1 | `float(prices[k])` 当函数用 | 运行时 TypeError | 别把列表套 float()，要算均价时遍历列表 |
| 2 | `max={}` 把内置函数覆盖 | 运行时 TypeError | **永远别用 max/min/sum 做变量名** |
| 3 | `max[k]` 漏 s，把函数当字典 | 运行时 TypeError | 函数不能 `[]` 查值 |
| 4 | `avg["k"]="t"` 变量名加引号 | 逻辑错 | **变量不加引号，字符串要加引号**，边界别搞混 |
| 5 | print 缩进 4 格被吞进 for | 逻辑错 | 跳出 for 用 `Shift+Tab` 顶到 0 缩进 |
| 6 | 注释掉 print 但 for 还留 | 语法 IndentationError | for 不能空着，要么填代码要么整段删 |
| 7 | `avgs =` 数字变量 vs `avg[k] =` 字典赋值 | 逻辑错 | 一字之差：avg 字典 vs avgs 数字；**列表用遍历，字典用 [key] 直接定位** |
| 8 | f-string 里 `maxs[k]` 没包 `{}` | 逻辑错 | f-string 里只有 `{}` 才是表达式会执行 |
| 9 | f-string 里写了整个字典 `{avg}` | 逻辑错 | 想要某一项用 `{avg[k]}`，别打整坨字典 |
| 10 | `maxs[v]` 列表当 key | 运行时 TypeError | 字典 key 必须是字符串/数字/元组，**列表是可变的不能当 key** |
| 11 | `for r in records: r` 是什么 | 概念 | 取决于 records 是什么类型，print 一下 type() 立刻知道 |
| 12 | `sorted(counts.items(), key=lambda x: x[1], reverse=True)` 不会 | 概念 | lambda 临时函数，`x[1]` 取第二列（值）当排序依据 |

---

## 七、今天最值钱的 3 个认知升级

### 1. 字典 vs 列表：定位方式完全不同

| 结构 | 怎么找"番茄的均价" |
|---|---|
| 列表 `[4.2, 3.2, 7.0, ...]` | 不知道哪个是番茄，得**遍历整个列表** |
| 字典 `{'番茄':4.2, '黄瓜':3.2, ...}` | `avg['番茄']` 或 `avg[k]` **一查就到**，不用遍历 |

**字典的精髓：用 key 直接定位，不用挨个找。**

### 2. 永远别用内置函数名做变量名

`max`, `min`, `sum`, `len`, `sorted`, `print`, `list`, `dict`, `str`, `int` ……

起了同名变量，内置函数就被你**覆盖**了，后面想用就只能重启 Python。

### 3. f-string 的表达式规则

```python
name = "番茄"
print(f"产品是{name}")    # ✅ {name} 是变量，会求值
print(f"产品是name")      # ❌ 没 {}，原样输出 "产品是name"
print(f"最高价是{max(v)}")  # ✅ {max(v)} 表达式会执行
print(f"最高价是max(v)")    # ❌ 原样输出 "最高价是max(v)"
```

**只有 `{}` 包起来的才是表达式会执行。**

---

## 八、明天 day11 之前自检

- [ ] 删掉 day10 line 134 那行调试 print
- [ ] 跑最后一遍截图存档（可选）
- [ ] 今天的 12 个坑里，至少 3 个能在不翻笔记的情况下说出根因

---

_生成于 2026.09.10 16:53_ · 与 day10_dict_group.py 配套

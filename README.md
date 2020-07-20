# house

`scrapy startproject house_transaction`创建scrapy框架命名为house_transaction

`scrapy genspider a luzhou.58.com/chuzu`

## 设置main.py

主要用于运行scarpy框架

```python
from scrapy.cmdline import execute
import sys
import os
#得到地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "a"])
```

## a.py

### 获得字段

首先在parse方法中爬取所需信息，如当前页中每个房型的网页链接，标题，大小，类型，价格。由于其中的数字通过base64进行编码，因此需要导入base64库和TTFont库进行解码。

```python
import base64
from fontTools.ttLib import TTFont
```

由于需要解码，对象需要时html类型，因此需要对爬取到的response进行转换`res_html = response.text`再使用正则表达式获得相关信息。

提取时可在cmd中用`scrapy shell + 链接`进行调试，避免多次爬取


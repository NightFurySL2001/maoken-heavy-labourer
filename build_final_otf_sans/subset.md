## 猫啃网扛重族 | Maoken Heavy Labourer
# 子集字体／Subsetting the font

## 步骤区别 Steps that are different

> 1. 制作映射表  
Creating the Mapping Table

在这步时，将不需要的字符及其 CID 排出 `map.txt` 即可。此处使用 [`subset_map_list.py`](./subset_map_list.py) 抽取 GB/T 2312-1980，《现代汉语通用字表》及《通用规范汉字表》的总集简体字字形，共 8242 个汉字；详细请见 [`simp-char-only.txt`](./simp-char-only.txt)。  
During this step, remove any glyphs and their CID that are not needed out of `map.txt`. Here, the Simplified Chinese (SC) version uses a set of characters from GB/T 2312-1980, *现代汉语通用字表* and *通用规范汉字表* containing a total of 8242 Chinese characters and the mapping file is made using [`subset_map_list.py`](./subset_map_list.py); details for the set of characters please see [`simp-char-only.txt`](./simp-char-only.txt).

同文件夹里面的 [`main_subsetter.py`](./main_subsetter.py) 提供了子集字体的代码，但是【猜测】因为非 CID 字体且使用贝兹曲线(Bézier curve) 的字体不会在 Adobe 软件内显示在地化名称，因此放弃此方法。  
[`main_subsetter.py`](./main_subsetter.py) in this folder provides code for subsetting font, however (I guessed) non-CID fonts using Bézier curve will not display their localized names in Adobe softwares, thus this method is not used.
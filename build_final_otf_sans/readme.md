## 猫啃网扛重族 | Maoken Heavy Labourer
# 封装字体／Building the font

## 参考步骤 Sample steps

参考步骤如下：  
Sample steps are as follow:

1. 制作映射表  
Creating the Mapping Table
2. 将字体从字符名称换成 CID 编号名称  
Name-keyed to CID-keyed Conversion
3. 微调 CID 字体源文件  
Hinting the CIDFont Resource
4. 封装 CID OpenType 字体  
Building the CID-keyed OpenType Font
5. （特别）将 OTF 转为 TTF <- 猫啃反馈 OTF 版在 Adobe Photoshop CC 2020 无法使用，因此需要转换成 TTF  
(Extra) Convert OTF to TTF <- Maoken has given feedback that OTF version will crash in Adobe Photoshop CC 2020, thus convert to TTF

工具/Tools：[AFDKO](https://github.com/adobe-type-tools/afdko)

以下只提供大致讲解，详细操作请见[命令文件](./FULL/build_command.txt)。  
The following is a rough outline, see [build commands](./FULL/build_command.txt) for detailed command.

## 获得文件 Getting files

请到[思源黑体仓库](https://github.com/adobe-fonts/source-han-sans)下的主目录及 Heavy 文件夹下载需要的文件。  
Please visit [the repository of Source Han Sans](https://github.com/adobe-fonts/source-han-sans) and download required files from the main repo and Heavy folder.

## 脚本解析 Decoding scripts

* `combined_input_file_get_cjk_char_list.py` - 提取字体里面的字符列表。  
  Get the character list of a font.
* `combine_raw_map.py` - 将修烂后的字体字形表合并至思源黑体的 CID 表。  
  Merge glyph list from weathered font to CID list of Source Han Sans.
* `subset_map_list.py` - 提取子集使用的字形 - CID 映射表。  
  Make the glyph - CID mapping file for subset font.
* `main_subsetter.py`: `get_font_item_list.py`, `rename_font.py` - 原本提取子集使用的代码（未使用及测试）。  
  Originally used to subset the font (not used nor tested).

## 文件解析 Decoding files

* `raw.txt` - 字体文件的映射及字形顺序编码（给 CID 使用）。  
  (CID) Mapping and glyph ID for font file.
* `map.txt` - 字体文件的字形对 CID 编码映射。  
  Mapping of glyphs to CID number in font file.
* `font.pfa` - 向量外框文件。  
  Vector outline file.
* `cidfontinfo` - 字体文件资料。  
  Info for font file.
* `cidfont.raw` - 未进行字体微调（hinting）的字体文件。  
  Unhinted font file.
* `cidfont.ps` - 已进行字体微调的字体文件。  
  Hinted font file.

## 参考 Reference

*Dr. Ken Lunde - [Leveraging AFDKO Tools to Convert Name-keyed OpenType Fonts to CID-keyed (Part 1)](https://ccjktype.fonts.adobe.com/2011/12/leveraging-afdko-part-1.html) [(Part 2)](https://ccjktype.fonts.adobe.com/2012/01/leveraging-afdko-part-2.html) [(Part 3)](https://ccjktype.fonts.adobe.com/2012/01/leveraging-afdko-part-3.html) (英文/English)
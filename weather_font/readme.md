## 猫啃网扛重族 | Maoken Heavy Labourer
# 弄烂字体／Weathering the font

在猫啃网的请求下，本人开始研究如何制作一款破烂风格的字体。  
With request from Maoken.com, I start to research on making a weathered look font.

## 整体思路 Full thoughts

本人思路如下：  
My thoughts are as follow:

1. 导出字形为图片（PNG）  
Export glyphs as pictures (PNG)
2. 在图片上添加模糊白点  
Add blurring white dots onto picture
3. 描图回向量字形（SVG）  
Trace pictures back to vector glyphs (SVG)
4. 合并字形进字体  
Merge glyphs into font

## 第一步 Step 1：导出字形为图片 Export glyphs as pictures

因为需要进行破烂工作，因此本计划不在向量图上操作字形。如果只是进行基础修饰（如添加圆角），可直接导出 `.sfdir` 后修改向量图。  
As the project requires rottening, this project will not modify vector glyphs. If only basic modification (e.g. rounded corners) is required, exporting to `.sfdir` and then modifying the vector diagrams should work.

工具/Tools：[FontTools](https://github.com/fonttools/fonttools) (导出 SVG/Exporting SVG), [cairosvg](https://github.com/Kozea/CairoSVG) (转换 SVG 去 PNG/Converting SVG to PNG)

脚本/Scripts: [`export_glyph_to_svg.py`](export_glyph_to_svg.py), [`convert_svg_to_pic.py`](convert_svg_to_pic.py)

## 第二步 Step 2：在图片上添加模糊白点 Add blurring white dots onto picture

工具/Tool：[Pillow](https://github.com/python-pillow/Pillow) (修改 PNG/Modifying PNG)

脚本/Script: [`add_dot_to_pic.py`](add_dot_to_pic.py)

## 第三步 Step 3：描图回向量字形 Trace pictures back to vector glyphs

工具/Tool：[potrace](http://potrace.sourceforge.net/) (描绘 PNG 去 SVG/Tracing PNG to SVG)

> *或其他工具，如 FontForge 内建描图功能 `glyph.autoTrace()`。*  
> *or other tools, such as FontForge built-in `glyph.autoTrace()`.*

脚本/Script: [`trace_image_to_svg.py`](trace_image_to_svg.py)

## 第四步 Step 4：合并字形进字体 Merge glyphs into font

工具/Tools：[FontForge](https://github.com/fontforge/fontforge) (导入 SVG，导出 TTF/OTF 字体格式/Import SVG, export TTF/OTF font format)

脚本/Scripts: [`convert_svg_to_ttf.py`](convert_svg_to_ttf.py), [`convert_svg_to_ttf_break.py`](convert_svg_to_ttf_break.py)

## 备注 Notes

1. 基于添加模糊白点使用随机数值，可能无法重现同样效果，因此本仓库在 `SourceHanSansCN-Heavy.otf_png_bmp_edit` 里提供制作字体时随机添加模糊白点后的效果图，`SourceHanSansCN-Heavy.otf_svg_edit` 则是使用 `potrace` 描图后的向量图。（v1.001 修改成使用文件名为随机数种子方便重现效果；把种子删除可重现纯随机数值。）  
Due to blurring white dots are added with random values and may not be replicated, thus this repo has provided the effect pictures after adding white dots when making the font in the folder `SourceHanSansCN-Heavy.otf_png_bmp_edit`, while `SourceHanSansCN-Heavy.otf_svg_edit` provides vector images traced with `potrace`. (v1.001 uses the file names as the random generator seed to be able to recreate the same effects; deleting the seed can recreate pure randomness values.)

2. 因为描图的描点过多导致文件过大，FontForge 可能因此溢出内存而崩溃或导出字体失败。解决方式为下载 64 位元的 FontForge 操作上述过程。（FontForge 默认安装 32 位元。）  
As the points in traced image is numerous causing the file size to grow too big, FontForge might ran out of memory and crash, or failed to generate a font. Download 64-bit version of FontForge to solve this issue. (FontForge by default install 32-bit version.)  
参考网址 Reference: https://github.com/fontforge/fontforge/issues/3062 ; Windows 64-bit 下载链接 Download link: https://sourceforge.net/projects/fontforgebuilds/files/x86_64/Portable/

3. 部分文件过大已在[额外文件分支](https://github.com/NightFurySL2001/maoken-heavy-labourer/tree/supplement-files)拆分上传，列表如下：  
Some large source files are split and uploaded in [supplement files branch](https://github.com/NightFurySL2001/maoken-heavy-labourer/tree/supplement-files), which is the following:

* `shsans-maoken-heavy-labourer.sfd` (黑/Gothic) - supplement-files: `shsans-maoken-heavy-labourer.zip.00X`
* `shserif-maoken-heavy-labourer.sfd` (宋/Ming) - supplement-files: `shserif-maoken-heavy-labourer.zip.00X`
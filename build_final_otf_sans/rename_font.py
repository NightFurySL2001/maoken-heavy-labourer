from fontTools import ttLib
from fontTools.ttLib.tables._n_a_m_e import table__n_a_m_e as ttTableName
#from fontTools.ttLib.tables._n_a_m_e import NameRecord
import sys
import os

FAMILY_RELATED_IDS = dict(
    LEGACY_FAMILY=1,
    TRUETYPE_UNIQUE_ID=3,
    FULL_NAME=4,
    POSTSCRIPT_NAME=6,
    PREFERRED_FAMILY=16,
    WWS_FAMILY=21,
)

def add_font_suffix(font_path):
    # test for existence of font file on requested file path
    if not file_exists(font_path):
        sys.stderr.write(
            f"ERROR: the path '{font_path}' does not appear to be a valid file path.{os.linesep}"
        )
        sys.exit(1)

    #open file
    tt = ttLib.TTFont(font_path)
    
    for record in tt.names:
        name_id = record.nameID
        if name_id not in FAMILY_RELATED_IDS:
            continue
        print(record)
        #do modifications here
    
    #myRecord = NameRecord()
    #myRecord.nameID = 2
    #myRecord.platformID = 3
    #myRecord.platEncID = 1
    #myRecord.langID = 0x409
    #myRecord.string = lang_name

    #tt['name'].names.append(myRecord)
    #platform 1 encoding 0 lang 0, platform 3 (windows) encoding 1 (unicode) lang 0x409 (english), nameID = 2

    # write changes to the font file
    try:
        tt.save(font_path)
        print(f"Updated '{font_path}'.\nFont generated successfully.")
        tt.close()
        return
    except Exception as e:
        sys.stderr.write(
            f"ERROR: unable to write new name to OpenType name table for '{font_path}'. {os.linesep}"
        )
        sys.stderr.write(f"{e}{os.linesep}")
        sys.exit(1)

def file_exists(filepath):
    # Tests for existence of a file on the string filepath
    return os.path.exists(filepath) and os.path.isfile(filepath)

add_font_suffix("shs-maoken-heavy-labourer-src.ttf")
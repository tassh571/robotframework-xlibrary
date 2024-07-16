# conf.py

# ไฟล์การตั้งค่าสำหรับ Sphinx documentation builder

# ไฟล์นี้มีแค่ตัวเลือกที่ใช้บ่อยที่สุด หากต้องการดูตัวเลือกทั้งหมด
# ให้ดูที่เอกสาร:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# หากมีส่วนขยาย (หรือโมดูลที่จะใช้กับ autodoc) อยู่ในไดเรกทอรีอื่น,
# ให้เพิ่มไดเรกทอรีเหล่านั้นใน sys.path ที่นี่ หากไดเรกทอรีเป็นสัมพัทธ์
# กับรากของเอกสาร, ใช้ os.path.abspath เพื่อทำให้เป็นเส้นทางที่สมบูรณ์
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'RobotFramework-XLibrary'
author = 'Tassana Khrueawan'
copyright = '2024, Tassana Khrueawan'
# เวอร์ชันสั้น X.Y
version = '12.0.0'
# เวอร์ชันเต็ม, รวมถึง alpha/beta/rc tags
release = '12.0.0'

# -- General configuration ---------------------------------------------------

# เพิ่มชื่อโมดูลส่วนขยาย Sphinx ที่นี่, เป็นสตริง สามารถเป็น
# ส่วนขยายที่มาพร้อมกับ Sphinx (ชื่อ 'sphinx.ext.*') หรือส่วนขยายที่กำหนดเอง
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.autosectionlabel',
    'myst_parser',
]

# เพิ่มเส้นทางที่มีเทมเพลตที่นี่, เป็นสัมพัทธ์กับไดเรกทอรีนี้
templates_path = ['_templates']

# ส่วนขยายของชื่อไฟล์แหล่งที่มา
# สามารถระบุหลายส่วนขยายเป็นรายการของสตริง
source_suffix = ['.rst', '.md']

# เอกสาร master toctree
master_doc = 'index'

# ภาษาสำหรับเนื้อหาที่สร้างขึ้นอัตโนมัติโดย Sphinx ดูเอกสาร
# สำหรับรายการภาษาที่รองรับ
# ใช้สำหรับแปลเนื้อหาผ่าน gettext catalogs ด้วย
language = 'th'

# รายการรูปแบบ, สัมพัทธ์กับไดเรกทอรีแหล่งที่มา, ที่ตรงกับไฟล์และ
# ไดเรกทอรีที่จะละเว้นเมื่อมองหาไฟล์แหล่งที่มา
# รูปแบบนี้มีผลกับ html_static_path และ html_extra_path ด้วย
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# ธีมที่จะใช้สำหรับหน้า HTML และ HTML Help ดูเอกสารสำหรับ
# รายการธีมที่มีในตัว
html_theme = 'sphinx_rtd_theme'

# ตัวเลือกธีมเฉพาะตัวและปรับแต่งลักษณะและความรู้สึกของธีมเพิ่มเติม
# สำหรับรายการตัวเลือกที่มีสำหรับแต่ละธีม, ดูเอกสาร
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# เพิ่มเส้นทางที่มีไฟล์ static แบบกำหนดเอง (เช่น style sheets) ที่นี่,
# เป็นสัมพัทธ์กับไดเรกทอรีนี้ ไฟล์เหล่านี้จะถูกคัดลอกหลังจากไฟล์ static ที่มีอยู่
# ดังนั้นไฟล์ที่ชื่อ "default.css" จะเขียนทับ "default.css" ที่มีอยู่
html_static_path = ['_static']

# เทมเพลตของไซด์บาร์แบบกำหนดเอง ต้องเป็นพจนานุกรมที่แม็พชื่อเอกสารกับ
# ชื่อเทมเพลต
#
# ไซด์บาร์เริ่มต้น (สำหรับเอกสารที่ไม่ตรงกับรูปแบบใด ๆ) ถูกกำหนดโดยธีมเอง
# สามารถเขียนทับได้โดยการให้เทมเพลตของตัวเองและกำหนดให้กับ
# html_sidebars dictionary ซึ่งอาจมีประโยชน์ในการรวมบริการอื่น ๆ
# หรือโพสต์ข้อมูลที่เกี่ยวข้องกับโปรเจ็กต์
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # ต้องการ 'show_related': ตัวเลือกธีม True เพื่อแสดง
        'searchbox.html',
        'donate.html',
    ]
}

# -- Extension configuration -------------------------------------------------

# -- ตัวเลือกสำหรับส่วนขยาย intersphinx ---------------------------------------

# การตั้งค่าตัวอย่างสำหรับ intersphinx: อ้างอิงไลบรารีมาตรฐานของ Python
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- ตัวเลือกสำหรับส่วนขยาย todo ----------------------------------------------

# หากต้องการใช้ส่วนขยายนี้, ต้องตั้งค่านี้เป็น 'True'
todo_include_todos = True

# -- ตัวเลือกสำหรับส่วนขยาย autodoc -------------------------------------------

# ค่านี้ประกอบด้วยรายชื่อของโมดูลที่จะจำลองขึ้นมา ซึ่งมีประโยชน์เมื่อ
# มีการขาดแคลนการพึ่งพาภายนอกในขณะสร้างเอกสารและทำให้การสร้าง
# ล้มเหลว สามารถเพิ่มโมดูลได้มากเท่าที่ต้องการ หากหนึ่งใน
# โมดูลเหล่านี้ถูกนำเข้าในขณะสร้างเอกสารโดยส่วนขยาย Sphinx ใด ๆ หรือโดย
# โค้ด Python ที่ถูกจัดทำเอกสารอัตโนมัติ จะถูกแทนที่ด้วย mock โดยอัตโนมัติ
autodoc_mock_imports = []

# -- ตัวเลือกสำหรับส่วนขยาย linkcode --------------------------------------

# ค่านี้กำหนดวิธีการสร้างลิงก์ไปยังโค้ดต้นฉบับใน HTML output
# ฟีเจอร์นี้มีประโยชน์เป็นพิเศษสำหรับโปรเจ็กต์ที่ต้องการลิงก์ไปยังแท็ก
# หรือ commit ที่เฉพาะเจาะจงใน repository ฟังก์ชันต่อไปนี้สร้างลิงก์ที่
# สอดคล้องกับเวอร์ชันปัจจุบันของโปรเจ็กต์ใน GitHub
import subprocess
import re

# ต้องการ Git และ repository ที่พร้อมใช้งานในขณะสร้าง
try:
    git_tag = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
    # ลบคำนำหน้า 'v' หากมี (เช่น 'v1.0.1' -> '1.0.1')
    git_tag = re.sub('^v', '', git_tag)
except subprocess.CalledProcessError:
    git_tag = 'main'

# กำหนดรูปแบบสำหรับลิงก์ไปยังโค้ดต้นฉบับ
html_context = {
    "display_github": True,  # รวม GitHub
    "github_user": "tassana.khr",  # ชื่อผู้ใช้
    "github_repo": "robotframework-xlibrary",  # ชื่อ repository
    "github_version": git_tag,  # เวอร์ชัน
    "conf_py_path": "/docs/",  # เส้นทางใน checkout ไปยังรากของเอกสาร
}

# -- ตัวเลือกสำหรับส่วนขยาย coverage ------------------------------------------

# ค่านี้เป็นรายการของรูปแบบที่จะละเว้นจากการตรวจสอบ coverage ซึ่งมีประโยชน์
# เมื่อคุณต้องการละเว้นบางส่วนของโค้ดจากรายงาน coverage
coverage_skip_undoc_in_source = True

# -- ตัวเลือกสำหรับส่วนขยาย napoleon ------------------------------------------

# ค่านี้ควบคุมว่าจะเปลี่ยน docstrings แบบ Google เป็น reStructuredText
# หรือไม่ หากตั้งค่าเป็น 'True', Sphinx จะจัดการพวกมันเป็น reStructuredText พื้นฐาน
napoleon_google_docstring = True

# ค่านี้ควบคุมว่าจะเปลี่ยน docstrings แบบ NumPy เป็น reStructuredText
# หรือไม่ หากตั้งค่าเป็น 'True', Sphinx จะจัดการพวกมันเป็น reStructuredText พื้นฐาน
napoleon_numpy_docstring = True

# ค่านี้ควบคุมว่าจะรวมสมาชิกพิเศษ (เช่น __init__, __call__, ฯลฯ)
# ใน output หากพวกเขามี docstring
napoleon_include_special_with_doc = True

# ค่านี้ควบคุมว่าจะรวมสมาชิก private (เช่น _foo, __foo, ฯลฯ)
# ใน output หากพวกเขามี docstring
napoleon_include_private_with_doc = False

# ค่านี้ควบคุมว่าจะรวมสมาชิก protected (เช่น _foo, _foo, ฯลฯ)
# ใน output หากพวกเขามี docstring
napoleon_include_protected_with_doc = True

# ค่านี้ควบคุมวิธีการแสดง docstrings ของ attribute ใน autodoc
napoleon_attr_annotations = True

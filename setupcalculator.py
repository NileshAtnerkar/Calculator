import sys

from cx_Freeze import *

includefiles =["cal.ico"]
base=None
if sys.platform == "win32":
    base ="win32GUI"
shortcut_table=[
    ("DesktopShortcut",
     "DesktopFolder",
     "Nilesh calculator",
     "TARGETDIR",
     "[TARGETDIR]\calculator.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options ={"data":msi_data}
setup(
    version ="0.1",
    description="Nilesh calculator",
    author ="Nilesh Atnerkar",
    name="Nilesh calculator",
    options={'build_exe':{'include_files': includefiles},"bdist_msi" :bdist_msi_options,},
    executables=[
        Executable(
            script="calculator.py",
            base=base,
            icon="cal.ico",


          )
    ]
)
#open the file location and enter the cmd = python mycalculator.py bdist_msi

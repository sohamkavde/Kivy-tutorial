# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2,glew

block_cipher = None


a = Analysis(
    ['culculator.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

a.datas +=  [('Code\culculator.kv','C:\\Users\\91798\\PycharmProjects\\kivyapp\\calculator\culculator.kv','DATA')]
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='culculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    Tree('C:\\Users\\91798\\PycharmProjects\\kivyapp\\calculator\\'),
    a.binaries,
    a.zipfiles,
    *[Tree(p) for p in (sdl2.dep_bins + glew_dep_bins)],
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='culculator',
)

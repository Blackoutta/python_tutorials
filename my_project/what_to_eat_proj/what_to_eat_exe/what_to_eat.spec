# -*- mode: python -*-

block_cipher = None


a = Analysis(['what_to_eat.py'],
             pathex=['C:\\Users\\huyangyi\\desktop\\python_learning\\my_project\\what_to_eat_bak'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='what_to_eat',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
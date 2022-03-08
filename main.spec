# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

add_data = [
    ("asset/*", "asset"),
    ("asset/cards/*", "asset/cards"),
    ("asset/arrow/*", "asset/arrow")
]

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=add_data,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='My Ono',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='app.ico' )

app = BUNDLE(exe,
         name='MyOno.app',
         icon=None,
         bundle_identifier=None,
         version='0.0.1',
         info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'CFBundleDocumentTypes': [
                {
                    'CFBundleTypeName': 'My File Format',
                    'CFBundleTypeIconFile': 'MyFileIcon.icns',
                    'LSItemContentTypes': ['com.jaaj.example'],
                    'LSHandlerRank': 'Owner'
                    }
                ]
            },
         )
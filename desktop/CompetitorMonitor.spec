# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('styles.py', '.'), ('api_client.py', '.'), ('C:\\Users\\Денис\\Desktop\\Зерокодер\\Промтинж\\Задания\\Урок 4.8\\pem08-master\\venv\\Lib\\site-packages\\PyQt6\\Qt6\\plugins', 'platforms'), ('C:\\Users\\Денис\\Desktop\\Зерокодер\\Промтинж\\Задания\\Урок 4.8\\pem08-master\\venv\\Lib\\site-packages\\PyQt6\\Qt6\\plugins', 'styles')],
    hiddenimports=['PyQt6', 'PyQt6.QtCore', 'PyQt6.QtWidgets', 'PyQt6.QtGui', 'PyQt6.QtCore.qasync', 'PyQt6.sip', 'PyQt6.QtCore.pyqtSignal', 'PyQt6.QtCore.pyqtSlot', 'PyQt6.QtCore.Qt', 'PyQt6.QtCore.QSize', 'PyQt6.QtGui.QFont', 'PyQt6.QtGui.QIcon', 'PyQt6.QtGui.QPixmap', 'PyQt6.QtWidgets.QApplication', 'PyQt6.QtWidgets.QMainWindow', 'PyQt6.QtWidgets.QWidget', 'PyQt6.QtWidgets.QVBoxLayout', 'PyQt6.QtWidgets.QHBoxLayout', 'PyQt6.QtWidgets.QLabel', 'PyQt6.QtWidgets.QPushButton', 'PyQt6.QtWidgets.QTextEdit', 'PyQt6.QtWidgets.QLineEdit', 'PyQt6.QtWidgets.QFrame', 'PyQt6.QtWidgets.QScrollArea', 'PyQt6.QtWidgets.QFileDialog', 'PyQt6.QtWidgets.QStackedWidget', 'PyQt6.QtWidgets.QMessageBox', 'PyQt6.QtWidgets.QProgressBar', 'PyQt6.QtCore.QThread', 'PyQt6.QtCore.pyqtSignal', 'PyQt6.QtGui.QDragEnterEvent', 'PyQt6.QtGui.QDropEvent', 'requests', 'requests.packages.urllib3', 'PIL', 'PIL.Image', 'pathlib', 'pathlib.Path'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='CompetitorMonitor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

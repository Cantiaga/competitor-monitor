"""
Скрипт сборки .exe файла для Windows
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path


def get_qt_plugins_path() -> str:
    """Получить путь к Qt плагинам"""
    try:
        from PyQt6.QtCore import QLibraryInfo
        plugins_path = QLibraryInfo.location(QLibraryInfo.LibraryPath.PluginsPath)
        return plugins_path
    except:
        # Fallback: пытаемся найти в стандартных местах
        import site
        for site_dir in site.getsitepackages():
            qt_plugins = Path(site_dir) / "PyQt6" / "Qt6" / "plugins"
            if qt_plugins.exists():
                return str(qt_plugins)
        return ""


def build_exe():
    """Собрать .exe файл"""
    print("=" * 60)
    print("🔨 СБОРКА DESKTOP ПРИЛОЖЕНИЯ")
    print("=" * 60)
    
    # Текущая директория
    current_dir = Path(__file__).parent
    
    # Проверяем наличие PyInstaller
    print("\n📦 Проверка PyInstaller...")
    try:
        import PyInstaller
        print(f"   ✓ PyInstaller {PyInstaller.__version__}")
    except ImportError:
        print("   ✗ PyInstaller не установлен")
        print("   Установка: pip install pyinstaller")
        sys.exit(1)
    
    # Имя приложения
    app_name = "CompetitorMonitor"
    
    # Параметры PyInstaller
    pyinstaller_args = [
        "pyinstaller",
        "--name", app_name,
        "--onefile",           # Один .exe файл
        "--windowed",          # Без консоли
        "--noconfirm",         # Перезаписывать без подтверждения
        "--clean",             # Очистить кеш
        
        # Иконка (если есть)
        # "--icon", "icon.ico",
        
        # Добавляем файлы
        "--add-data", f"styles.py{os.pathsep}.",
        "--add-data", f"api_client.py{os.pathsep}.",
        
        # Qt плагины (обязательно для работы PyQt6)
        "--add-data", f"{get_qt_plugins_path()}{os.pathsep}platforms",
        "--add-data", f"{get_qt_plugins_path()}{os.pathsep}styles",
        
        # Скрытые импорты для PyQt6
        "--hidden-import", "PyQt6",
        "--hidden-import", "PyQt6.QtCore",
        "--hidden-import", "PyQt6.QtWidgets",
        "--hidden-import", "PyQt6.QtGui",
        "--hidden-import", "PyQt6.QtCore.qasync",
        "--hidden-import", "PyQt6.sip",
        "--hidden-import", "PyQt6.QtCore.pyqtSignal",
        "--hidden-import", "PyQt6.QtCore.pyqtSlot",
        "--hidden-import", "PyQt6.QtCore.Qt",
        "--hidden-import", "PyQt6.QtCore.QSize",
        "--hidden-import", "PyQt6.QtGui.QFont",
        "--hidden-import", "PyQt6.QtGui.QIcon",
        "--hidden-import", "PyQt6.QtGui.QPixmap",
        "--hidden-import", "PyQt6.QtWidgets.QApplication",
        "--hidden-import", "PyQt6.QtWidgets.QMainWindow",
        "--hidden-import", "PyQt6.QtWidgets.QWidget",
        "--hidden-import", "PyQt6.QtWidgets.QVBoxLayout",
        "--hidden-import", "PyQt6.QtWidgets.QHBoxLayout",
        "--hidden-import", "PyQt6.QtWidgets.QLabel",
        "--hidden-import", "PyQt6.QtWidgets.QPushButton",
        "--hidden-import", "PyQt6.QtWidgets.QTextEdit",
        "--hidden-import", "PyQt6.QtWidgets.QLineEdit",
        "--hidden-import", "PyQt6.QtWidgets.QFrame",
        "--hidden-import", "PyQt6.QtWidgets.QScrollArea",
        "--hidden-import", "PyQt6.QtWidgets.QFileDialog",
        "--hidden-import", "PyQt6.QtWidgets.QStackedWidget",
        "--hidden-import", "PyQt6.QtWidgets.QMessageBox",
        "--hidden-import", "PyQt6.QtWidgets.QProgressBar",
        "--hidden-import", "PyQt6.QtCore.QThread",
        "--hidden-import", "PyQt6.QtCore.pyqtSignal",
        "--hidden-import", "PyQt6.QtGui.QDragEnterEvent",
        "--hidden-import", "PyQt6.QtGui.QDropEvent",
        
        # Скрытые импорты для других зависимостей
        "--hidden-import", "requests",
        "--hidden-import", "requests.packages.urllib3",
        "--hidden-import", "PIL",
        "--hidden-import", "PIL.Image",
        "--hidden-import", "pathlib",
        "--hidden-import", "pathlib.Path",
        
        # Главный файл
        "main.py"
    ]
    
    print(f"\n🚀 Запуск сборки: {app_name}.exe")
    print("-" * 60)
    
    # Запускаем PyInstaller
    result = subprocess.run(pyinstaller_args, cwd=current_dir)
    
    if result.returncode == 0:
        exe_path = current_dir / "dist" / f"{app_name}.exe"
        
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print("\n" + "=" * 60)
            print("✅ СБОРКА ЗАВЕРШЕНА УСПЕШНО!")
            print("=" * 60)
            print(f"\n📁 Файл: {exe_path}")
            print(f"📊 Размер: {size_mb:.1f} MB")
            print("\n💡 Для запуска:")
            print(f"   1. Запустите backend: python run.py")
            print(f"   2. Запустите {app_name}.exe")
        else:
            print("\n❌ Ошибка: .exe файл не найден")
    else:
        print("\n❌ Ошибка сборки")
        sys.exit(1)


def clean():
    """Очистить артефакты сборки"""
    current_dir = Path(__file__).parent
    
    dirs_to_remove = ["build", "dist", "__pycache__"]
    files_to_remove = ["*.spec"]
    
    print("🧹 Очистка артефактов сборки...")
    
    for dir_name in dirs_to_remove:
        dir_path = current_dir / dir_name
        if dir_path.exists():
            shutil.rmtree(dir_path)
            print(f"   Удалено: {dir_name}/")
    
    for pattern in files_to_remove:
        for file in current_dir.glob(pattern):
            file.unlink()
            print(f"   Удалено: {file.name}")
    
    print("✓ Очистка завершена")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        clean()
    else:
        build_exe()


import sys
if getattr(sys, 'frozen', False) and sys.platform == 'darwin':
    os.environ['QTWEBENGINEPROCESS_PATH'] = os.path.normpath(os.path.join(
        sys._MEIPASS, 'PyQt5', 'Qt', 'lib',
        'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app',
        'Contents', 'MacOS', 'QtWebEngineProcess'
    ))
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtCore import QUrl, QTimer, QLibraryInfo
from PyQt5 import QtCore
import os

app = ApplicationContext()

# print("QTWEBENGINEPROCESS_PATH : " + os.environ['QTWEBENGINEPROCESS_PATH'])
print("PrefixPath : " + QLibraryInfo.location(QLibraryInfo.PrefixPath))
print("DocumentationPath : " + QLibraryInfo.location(QLibraryInfo.DocumentationPath))
print("HeadersPath : " + QLibraryInfo.location(QLibraryInfo.HeadersPath))
print("LibrariesPath : " + QLibraryInfo.location(QLibraryInfo.LibrariesPath))
print("LibraryExecutablesPath : " + QLibraryInfo.location(QLibraryInfo.LibraryExecutablesPath))
print("BinariesPath : " + QLibraryInfo.location(QLibraryInfo.BinariesPath))
print("PluginsPath : " + QLibraryInfo.location(QLibraryInfo.PluginsPath))
print("ImportsPath : " + QLibraryInfo.location(QLibraryInfo.ImportsPath))
print("Qml2ImportsPath : " + QLibraryInfo.location(QLibraryInfo.Qml2ImportsPath))
print("ArchDataPath : " + QLibraryInfo.location(QLibraryInfo.ArchDataPath))
print("DataPath : " + QLibraryInfo.location(QLibraryInfo.DataPath))
print("TranslationsPath : " + QLibraryInfo.location(QLibraryInfo.TranslationsPath))
print("ExamplesPath : " + QLibraryInfo.location(QLibraryInfo.ExamplesPath))
print("TestsPath : " + QLibraryInfo.location(QLibraryInfo.TestsPath))
print("SettingsPath : " + QLibraryInfo.location(QLibraryInfo.SettingsPath))


class Browser(QWebEngineView):

    def __init__(self):
        QWebEngineView.__init__(self)
        # self.loadFinished.connect(self._result_available)

    # def _result_available(self, ok):
    #     frame = self.page().mainFrame()
    #     print(unicode(frame.toHtml()).encode('utf-8'))

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    web = QWebEngineView()
    page = QWebEnginePage()
    page.setView(web)
    web.setPage(page)
    web.setUrl(QtCore.QUrl('http://www.google.com/'))
    web.show()
    app.app.exec_()

# class MyBrowser(QWebEngineView):

#     def __init__(self):
#         super().__init__()

#     def closeEvent(self, event):
#         self.closing.emit()




# view = MyBrowser()
# view.setUrl(QtCore.QUrl('https://www.google.ca/#q=pyqt'))
# view.show()
# view.page().loadFinished.connect(
#     # Display the web page for one second after it loads.
#     lambda ok: QTimer.singleShot(5000, app.app.quit))
# app.app.exec_()

# view = QWebEngineView()
# # Use a raw string to avoid accidental special characters in Windows filenames:
# # ``c:\temp`` is `c<tab>emp`!
# view.setUrl(QUrl("http://www.pyinstaller.org"))
# view.resize(640, 480)
# view.show()
# view.loadProgress.connect(print)

# view.page().loadFinished.connect(
#     # Display the web page for one second after it loads.
#     lambda ok: QTimer.singleShot(5000, app.app.quit))
# app.app.exec_()

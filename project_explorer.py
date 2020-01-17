from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget, QListWidget, QTextEdit, QAction, QTreeView, \
	QFileSystemModel, QLabel, QFrame, QPushButton, QStatusBar, QTabWidget, QWidget, QFormLayout, QLineEdit, QHBoxLayout, \
	QRadioButton, QCheckBox
import sys
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDir

# https://github.com/BasioMeusPuga/Lector/blob/master/lector/dockwidgets.py
from PyQt5  import QtWidgets


class MainWindow(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.create_right_docker()
		self.create_left_docker()
		self.create_bottom_docker()
		self.create_central_widget()
		self.set_window_properties()
		self.create_status_bar()
		self.create_actions()

	def set_window_properties(self):
		self.setWindowTitle("EnSeGi Explorer")
		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.showMaximized()

	def create_actions(self):
		menu_bar = self.menuBar()
		file_menu = menu_bar.addMenu("File")
		file_menu.addAction("New Project")
		file_menu.addAction("Open")
		file_menu.addAction("Save")
		file_menu.addAction("Open Recent")
		file_menu.addAction("Close Project")
		file_menu.addAction("Rename Project")
		file_menu.addAction("Settings")
		file_menu.addAction("Exit")
		menu_bar = self.menuBar()
		view_menu = menu_bar.addMenu("View")
		view_left_sidebar = QAction('Left menu', self)
		view_menu.addAction(view_left_sidebar)
		view_left_sidebar.triggered.connect(self.show_left_docker)

		view_right_sidebar = QAction('Right menu', self)
		view_menu.addAction(view_right_sidebar)
		view_right_sidebar.triggered.connect(self.show_right_docker)

		view_bottom_sidebar = QAction('Bottom menu', self)
		view_menu.addAction(view_bottom_sidebar)
		view_bottom_sidebar.triggered.connect(self.show_bottom_docker)

	def show_left_docker(self):
		self.left_docker.show()

	def show_right_docker(self):
		self.right_docker.show()

	def show_bottom_docker(self):
		self.bottom_docker.show()

	def create_status_bar(self):
		status_bar = QStatusBar()
		status_bar.setSizeGripEnabled(False)
		self.size_label = QLabel()
		self.size_label.setFrameStyle(QFrame.StyledPanel | QFrame.Sunken)
		status_bar.addPermanentWidget(self.size_label)
		status_bar.showMessage("Status")
		self.setStatusBar(status_bar)

	def create_right_docker(self):
		self.right_docker = QDockWidget("Project Explorer", self)
		self.right_docker.setAllowedAreas(Qt.RightDockWidgetArea)
		self.right_docker.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)

		ex = RightDocker()
		self.right_docker.setWidget(ex)
		self.addDockWidget(Qt.RightDockWidgetArea, self.right_docker)

	def create_left_docker(self):
		self.left_docker = QDockWidget("Project Explorer", self)
		self.left_docker.setAllowedAreas(Qt.LeftDockWidgetArea)
		self.left_docker.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)

		ex = RightDocker()
		self.left_docker.setWidget(ex)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.left_docker)

	def create_bottom_docker(self):
		self.bottom_docker = QDockWidget("Project Explorer", self)
		self.bottom_docker.setAllowedAreas(Qt.BottomDockWidgetArea)
		self.bottom_docker.setFeatures(QtWidgets.QDockWidget.DockWidgetClosable)

		ex = RightDocker()
		self.bottom_docker.setWidget(ex)
		self.addDockWidget(Qt.BottomDockWidgetArea, self.bottom_docker)

	def create_central_widget(self):
		self.setCentralWidget(QTextEdit())

	def createDockWidget(self):
		self.dock1 = QDockWidget("Project Explorer", self)
		model = QFileSystemModel()
		model.setRootPath(QDir.currentPath())

		tree = QTreeView()
		tree.setModel(model)
		self.dock1.setWidget(tree)
		self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)

		self.dock = QDockWidget("Signal Explorer", self)
		self.listWiget = QListWidget()
		list = ["Python", "C++", "Java", "C#"]
		self.listWiget.addItems(list)
		self.dock.setWidget(self.listWiget)
		self.addDockWidget(Qt.RightDockWidgetArea, self.dock)

		# self.dock.setFloating(False)

class RightDocker(QTabWidget):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.tab1 = QWidget()
		self.tab2 = QWidget()
		self.tab3 = QWidget()

		self.addTab(self.tab1, "Tab 1")
		self.addTab(self.tab2, "Tab 2")
		self.addTab(self.tab3, "Tab 3")
		self.tab1UI()
		self.tab2UI()
		self.tab3UI()
		self.setWindowTitle("tab demo")

		self.setTabPosition(QtWidgets.QTabWidget.West)

	def tab1UI(self):
		layout = QFormLayout()
		layout.addRow("Name", QLineEdit())
		layout.addRow("Address", QLineEdit())
		self.setTabText(0, "Contact Details")
		self.tab1.setLayout(layout)

	def tab2UI(self):
		layout = QFormLayout()
		sex = QHBoxLayout()
		sex.addWidget(QRadioButton("Male"))
		sex.addWidget(QRadioButton("Female"))
		layout.addRow(QLabel("Sex"), sex)
		layout.addRow("Date of Birth", QLineEdit())
		self.setTabText(1, "Personal Details")
		self.tab2.setLayout(layout)

	def tab3UI(self):
		layout = QHBoxLayout()
		layout.addWidget(QLabel("subjects"))
		layout.addWidget(QCheckBox("Physics"))
		layout.addWidget(QCheckBox("Maths"))
		self.setTabText(2, "Education Details")
		self.tab3.setLayout(layout)


def main():
	app = QApplication(sys.argv)
	app.setOrganizationName("Knorr-Bremse Technology Center India, Pune")
	app.setOrganizationDomain("https://www.knorr-bremse.co.in/en/group/kbinindia/tci/tci_1.jsp")
	app.setApplicationName("EnSeGi Library GUI")
	# app.setWindowIcon(QIcon(":/icon.png"))
	form = MainWindow()
	form.show()
	sys.exit(app.exec())

main()

import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from interface.window import Ui_MainWindow
from PySide6.QtCore import Slot
from PySide6.QtCharts import QScatterSeries, QChart, QChartView
import parsing


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_file.clicked.connect(self.open_file)



    @Slot()
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "WAV Files (*.wav)")
        if file_path:
            data = parsing.parse_wavfile(file_path)
            print(data)
            scatter_series = QScatterSeries()
            for i in range(10):
                scatter_series.append(i, i+1)
            
            chart = QChart()
            chart.addSeries(scatter_series)
            self.horizontalLayout.addWidget(QChartView(chart))
            



        



    












app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

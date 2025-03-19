import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
import signal_analysis
from interface.window import Ui_MainWindow
from PySide6.QtCore import Slot
from PySide6.QtCharts import QScatterSeries, QChart, QChartView, QSplineSeries
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
            scatter_series = QScatterSeries()
            for i in range(10):
                scatter_series.append(i, i+1)
            
            chart = QChart()
            chart.addSeries(scatter_series)
            chart.legend().setVisible(0)
            self.horizontalLayout.addWidget(QChartView(chart))


            input_signal = parsing.parse_wavfile(file_path)

            ampl_array = signal_analysis.compute_amplitude_spectrum(input_signal)
            freq_array = signal_analysis.compute_frequency_spectrum(input_signal)
            line_series_2 = QSplineSeries()
            for i in range(30):
                line_series_2.append(ampl_array[i], freq_array[i])
            
            chart_2 = QChart()
            chart_2.addSeries(line_series_2)
            chart_2.createDefaultAxes()
            chart_2.legend().setVisible(0)
            self.horizontalLayout_2.addWidget(QChartView(chart_2))

            



        



    












app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

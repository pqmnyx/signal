from datetime import timedelta
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QWidget
import signal_analysis
from interface.window import Ui_MainWindow
from PySide6.QtCore import Slot
from PySide6.QtCharts import QScatterSeries, QChart, QChartView, QSplineSeries
from parsing import Signal, parse_wavfile
from filter import filter


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    signal: Signal = None
    time_window: timedelta = timedelta(seconds=1)
    points_resolution: int = 50


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chart_list = [QChart(), QChart(), QChart(), QChart()]  
        self.horizontalLayout.addWidget(QChartView(self.chart_list[0]))
        self.horizontalLayout_2.addWidget(QChartView(self.chart_list[1]))
        self.horizontalLayout_3.addWidget(QChartView(self.chart_list[2]))
        self.horizontalLayout_4.addWidget(QChartView(self.chart_list[3]))

        self.pushButton_file.clicked.connect(self.open_file)
        self.pushButton_filter.clicked.connect(self.generate_charts)


    @Slot()
    def open_file(self): 
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "WAV Files (*.wav)")
        if file_path:
            self.signal = parse_wavfile(file_path)
            

    @Slot()    
    def generate_charts(self):
        if self.signal == None:
            return -1

        a = []
        a = self.lineEdit_a.text().strip().split(",")
        b = []
        b = self.lineEdit_b.text().strip().split(",")
        a = list(map(float, a))
        b = list(map(float, b))
        
        input_signal = self.signal.trim(self.time_window).sparse_signal(self.points_resolution)
        points = []
        for index, element in enumerate(input_signal.data):
            points.append([index/input_signal.bitrate, element])
        self.drawChart(self.chart_list[0], points)

        output_signal = filter(a, b, self.signal).trim(self.time_window).sparse_signal(self.points_resolution)
        points = []
        for index, element in enumerate(output_signal.data):
            points.append([index/output_signal.bitrate, element])
        self.drawChart(self.chart_list[2], points)

        ampl_array = signal_analysis.compute_amplitude_spectrum(self.signal)
        freq_array = signal_analysis.compute_frequency_spectrum(self.signal)
        points = list(zip(freq_array, ampl_array))
        self.drawChart(self.chart_list[1], points)

        filtered_signal = filter(a, b, self.signal)
        ampl_array = signal_analysis.compute_amplitude_spectrum(filtered_signal)
        freq_array = signal_analysis.compute_frequency_spectrum(filtered_signal)
        points = list(zip(freq_array, ampl_array))
        self.drawChart(self.chart_list[3], points)



    def drawChart(self, chart: QChart, points: list[tuple[float,float]]) -> QChart:
        chart.removeAllSeries()
        line_series = QSplineSeries()
        for x, y in points:
            line_series.append(x,y)
        chart.addSeries(line_series)
        chart.createDefaultAxes()
        chart.legend().setVisible(0)

        return chart

    


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

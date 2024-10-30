from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
from tkinter import filedialog
from convert_logics.logics import taking_out, convert_m4a_to_wav
from GUI.style_wind import CONST_WINDOW


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(350, 250)
        self.setStyleSheet(CONST_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="select file for sentiment analysis")
        support = QLabel(text="support format: PCM WAV, AIFF/AIFF-C and Native FLAC")
        start_analysis = QPushButton(text="select file")
        start_analysis.clicked.connect(self.write_sound)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(support, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(start_analysis)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def write_sound(self):
        self.file_path = filedialog.askopenfilename(
                title="select file",
                filetypes=[("Audio Files", "*.mp4"), ("All Files", "*.*")]
            )
        
        sound = taking_out(self.file_path)
        print(sound)
        
        
        
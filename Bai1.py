import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QColorDialog, QFontDialog
from PyQt5.QtCore import Qt

class TextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties (title and initial size)
        self.setWindowTitle("Text Display Application")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create widgets (QLineEdit, QPushButton, and QLabel)
  
        self.start_button = QPushButton("Bắt đầu Game")

        self.button = QPushButton("Thoát Game")
        

        # Create a vertical layout
        layout = QVBoxLayout()

        # Add widgets to the layout
      
        layout.addWidget(self.start_button)
        layout.addWidget(self.button)
        

        # Set the layout for the central widget
        central_widget.setLayout(layout)

        # Connect the button click event to the display_text function

        self.start_button.clicked.connect(self.show_dialog_Start)
        self.button.clicked.connect(self.show_dialog_Quit)

    def show_dialog_Start(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("!!!")

        # Create a label with a message
        label = QLabel("Chương trình đã bắt đầu")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec_()
        
    def show_dialog_Quit(self):
        # Create a QDialog instance
        dialog = QDialog(self)
        dialog.setWindowTitle("!!!")

        # Create a label with a message
        label = QLabel("Bạn đã thoát game")

        # Create a layout for the dialog
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        # Set the layout for the dialog
        dialog.setLayout(dialog_layout)

        # Show the dialog as a modal dialog (blocks the main window)
        dialog.exec_()
        
def main():
    # Create a PyQt application
    app = QApplication(sys.argv)

    # Create an instance of the TextDisplayApp class
    window = TextDisplayApp()

    # Show the window
    window.show()

    # Run the application's event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
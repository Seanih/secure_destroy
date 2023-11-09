import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
)

# Qt is a positioning module
from PyQt6.QtCore import Qt
from pathlib import Path


def select_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    if filenames:
        destroy_btn.setDisabled(0)
        clear_btn.setVisible(True)
        message.setText(f"{len(filenames)} file(s) selected:\n" + "\n".join(filenames))
    else:
        message.setText("No files selected")


def destroy_files():
    try:
        num_files = len(filenames)
        for filename in filenames:
            path = Path(filename)
            # write to file multiple times
            with open(path, "wb") as file:
                file.write(b"")
            with open(path, "wb") as file:
                file.write(b"bahahahaha!")
            with open(path, "wb") as file:
                file.write(b"")
            path.unlink()

            clear_btn.setVisible(False)
            destroy_btn.setDisabled(1)
            message.setText(f"Successfully destroyed {num_files} file(s)")
    except:
        message.setText("No files were selected or an an error occured.")


def clear_selections():
    try:
        if filenames:
            filenames.clear()
            clear_btn.setVisible(False)
            destroy_btn.setDisabled(1)
            message.setText("Removed selection")
        else:
            message.setText("No files were selected")
    except:
        pass


# instantiate GUI
app = QApplication([])
window = QWidget()
window.setWindowTitle("Secure File Destroyer")
layout = QVBoxLayout()

# create and add app description
description = QLabel(
    'Select the files you want destroyed. The files will be <font color="red">permanently</font> deleted.'
)
layout.addWidget(description)

# create buttons and add to layout with positioning
select_btn = QPushButton("Select Files")
select_btn.setToolTip("Choose the file(s) you want to delete")
select_btn.setFixedWidth(100)
layout.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)
select_btn.clicked.connect(select_files)

destroy_btn = QPushButton("Destroy Files")
destroy_btn.setToolTip("delete the selected file(s)")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)
destroy_btn.setDisabled(1)

message = QLabel("")
layout.addWidget(message, alignment=Qt.AlignmentFlag.AlignCenter)

clear_btn = QPushButton("Clear Selection")
clear_btn.setToolTip("Remove the selected files")
clear_btn.setFixedWidth(100)
layout.addWidget(clear_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
clear_btn.clicked.connect(clear_selections)
clear_btn.setVisible(False)

# ready app for execution
window.setLayout(layout)
window.show()
sys.exit(app.exec())

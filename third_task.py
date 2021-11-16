import os
from PySide6.QtCore import QSize, QUrl
from PySide6.QtWidgets import QWidget, \
    QApplication, \
    QHBoxLayout, \
    QPushButton, \
    QMainWindow, \
    QVBoxLayout, \
    QFileDialog, \
    QLabel
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class VideoWidget(QVideoWidget):
    def __init__(self, media_player):
        super(VideoWidget, self).__init__()
        self._media_player = media_player

    def mousePressEvent(self, mouse_event):
        if self._media_player.playbackState() == QMediaPlayer.PlayingState:
            self._media_player.pause()
        else:
            self._media_player.play()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Media player')

        self.setMinimumSize(QSize(640, 480))

        file_name_prefix = QLabel('File name: ')
        file_name_prefix.setFixedWidth(60)

        self.file_name_label = QLabel()
        self.file_name_label.setContentsMargins(0, 0, 0, 0)

        self.push_button = QPushButton('Open file')
        self.push_button.clicked.connect(self.open_file_dialog)
        self.push_button.setFixedWidth(80)

        top_layout = QHBoxLayout()
        top_layout.addWidget(file_name_prefix)
        top_layout.addWidget(self.file_name_label)
        top_layout.addWidget(self.push_button)

        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.audio_output.setVolume(10)

        video_widget = VideoWidget(self.media_player)

        self.media_player.setVideoOutput(video_widget)
        self.media_player.setAudioOutput(self.audio_output)

        self.error_label = QLabel()
        self.error_label.setFixedHeight(20)

        full_layout = QVBoxLayout()

        full_layout.addLayout(top_layout)
        full_layout.addWidget(video_widget)
        full_layout.addWidget(self.error_label)

        container = QWidget()
        container.setContentsMargins(0, 0, 0, 0)
        container.setLayout(full_layout)

        self.setCentralWidget(container)

    def media_player_error(self, signal):
        self.error_label.setText(f'Error: {signal} {self.media_player.errorString()}')

    def open_file_dialog(self, signal):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open video')

        if file_name != '':
            self.media_player.setSource(QUrl.fromLocalFile(file_name))
            self.media_player.play()

            self.file_name_label.setText(os.path.basename(file_name))


if __name__ == '__main__':
    app = QApplication()

    main_win = MainWindow()
    main_win.show()

    app.exec()
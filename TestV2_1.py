#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: RTL-SDR reciever
# Author: Tyler Kovach
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
import osmosdr
import time

from gnuradio import qtgui

class TestV2_1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "RTL-SDR reciever")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("RTL-SDR reciever")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "TestV2_1")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.volume = volume = 50e-3
        self.tuning = tuning = 0.88e6
        self.samp_rate = samp_rate = 768000

        ##################################################
        # Blocks
        ##################################################
        self._volume_range = Range(0, 10, 50e-3, 50e-3, 200)
        self._volume_win = RangeWidget(self._volume_range, self.set_volume, 'volume', "counter_slider", float)
        self.top_grid_layout.addWidget(self._volume_win)
        self._tuning_range = Range(0.5e6, 30e6, 10e3, 0.88e6, 200)
        self._tuning_win = RangeWidget(self._tuning_range, self.set_tuning, 'tuning', "counter_slider", float)
        self.top_grid_layout.addWidget(self._tuning_win)
        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + "rtl=0,direct_samp=2"
        )
        self.rtlsdr_source_0.set_time_now(osmosdr.time_spec_t(time.time()), osmosdr.ALL_MBOARDS)
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(tuning, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(50, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(200000, 0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            2048, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            tuning, #fc
            200e3, #bw
            "", #name
            1
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_ccf(
            16,
            firdes.low_pass(
                1,
                samp_rate,
                samp_rate/64,
                12000,
                firdes.WIN_HAMMING,
                6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff(volume)
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_am_demod_cf_0 = analog.am_demod_cf(
        	channel_rate=48000,
        	audio_decim=1,
        	audio_pass=1000,
        	audio_stop=8000,
        )
        self.analog_agc_xx_0 = analog.agc_cc(6.25e-4, 1.0, 1.0)
        self.analog_agc_xx_0.set_max_gain(65536)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_agc_xx_0, 0), (self.analog_am_demod_cf_0, 0))
        self.connect((self.analog_am_demod_cf_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.analog_agc_xx_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "TestV2_1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume
        self.blocks_multiply_const_vxx_0.set_k(self.volume)

    def get_tuning(self):
        return self.tuning

    def set_tuning(self, tuning):
        self.tuning = tuning
        self.qtgui_freq_sink_x_0.set_frequency_range(self.tuning, 200e3)
        self.rtlsdr_source_0.set_center_freq(self.tuning, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/64, 12000, firdes.WIN_HAMMING, 6.76))
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)





def main(top_block_cls=TestV2_1, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 21:25:38 2020

@author: josephbattesti
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
import numpy as np
from scipy.fftpack import fft


def db_amp(y: np.ndarray) -> np.ndarray:
    x = np.ndarray.copy(y)
    x = 10 * np.log10(x / np.max(x))
    return x


def select_chunk(signal: np.ndarray) -> tuple:
    fig = plt.figure(figsize=(11, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(signal)
    plt.ylabel('Value')
    plt.xlabel('Sample')
    zoom_ok = False
    print('\nZoom or pan to view, \npress spacebar when ready to click:\n')
    while not zoom_ok:
        zoom_ok = plt.waitforbuttonpress()
    print('Select starting point: ')
    val = plt.ginput(1)
    zoom_ok = False
    print('\nZoom or pan to view, \npress spacebar when ready to click:\n')
    while not zoom_ok:
        zoom_ok = plt.waitforbuttonpress()
    print('Select ending point: ')
    val2 = plt.ginput(1)
    plt.close()
    return signal[np.int(val[0][0]):np.int(val2[0][0])], np.int(val[0][0])


def signal_to_noise_ratio(signal: np.ndarray) -> float:
    print('Select noise chunk')
    noise = select_chunk(signal)
    print('Done selecting noise chunk')
    print('Select signal chunk')
    signal = select_chunk(signal)
    print('Done selecting signal chunk')
    snr = 10 * np.log10(np.mean(signal**2) / np.mean(noise**2))
    print('SNR=' + str(int(snr)) + 'db')
    return snr


def spectrum(signal: np.ndarray, fs: int) -> [np.ndarray, np.ndarray, np.ndarray]:
    complex_spectrum = fft(signal)
    amplitude = abs(complex_spectrum)
    phase = np.unwrap(np.angle(complex_spectrum))
    frequency_axis = np.linspace(0, fs / 2, np.shape(signal)[0] // 2)
    amplitude_db = db_amp(amplitude[np.shape(amplitude)[
                          0] - (np.shape(amplitude)[0] // 2) - 1:-1])
    return frequency_axis, amplitude_db, phase



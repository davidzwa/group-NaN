clear all; clc; close all;

% Frequency data
fc = 102.7E6;
fs = 2.4E6;
gain = 20;
time = 2;  %sec

%output specification
file = 'cap.bin';

cmd = ['Lab6_matlab\rtl_sdr ' ... 
    '-s ' num2str(fs) ...
    ' -f ' num2str(fc) ...
    ' -g ' num2str(gain) ...
    ' -d 0' ...
    ' -n ' num2str(time*fs) ...
    ' ' num2str(file) ...
    ];
status = system(cmd)

%sdrinfo
%rx = comm.SDRRTLReceiver;
%rx.CenterFrequency = fc;
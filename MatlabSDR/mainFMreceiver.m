clear all; clc; close all;

% Frequency data
fc = 102.7E6;
fs = 2.4E6;
gain = 20;
time = 10;  %sec
samples = time*fs;

%file specification
subFolder = 'Lab6_matlab';
file = 'cap.bin';

addpath(subFolder);
cmd = [subFolder '\rtl_sdr ' ... 
    '-s ' num2str(fs) ...
    ' -f ' num2str(fc) ...
    ' -g ' num2str(gain) ...
    ' -d 0' ...
    ' -n ' num2str(samples) ...
    ' ' num2str(file) ...
    ];
system(cmd)
x = loadFile(file);
simpleSA(x,2^14,2400);  % example values, not-working

%sdrinfo
%rx = comm.SDRRTLReceiver;
%rx.CenterFrequency = fc;
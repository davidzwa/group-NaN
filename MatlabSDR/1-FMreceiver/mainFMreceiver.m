clear all; clc; close all;

% Frequency data
fc = 102.7E6;
fs = 2.4E6;
gain = 20;
time = 5;  %sec
samples = time*fs;

%file specification
subFolder = 'Lab6_matlab\';
file = 'cap.bin';
refresh_capture = false;
addpath(subFolder);

if refresh_capture
    cmd = [subFolder '\rtl_sdr ' ... 
        '-s ' num2str(fs) ...
        ' -f ' num2str(fc) ...
        ' -g ' num2str(gain) ...
        ' -d 0' ...
        ' -n ' num2str(samples) ...
        ' ' num2str(file) ...
        ];
    system(cmd)
end
x = loadFile(file);

x = FM_demod(x, 100000, 10, 20000, 5, fs);

sound(x, 48e3)

simpleSA(x,2^14, 48e3);  % example values, not-working

%sdrinfo
%rx = comm.SDRRTLReceiver;
%rx.CenterFrequency = fc;
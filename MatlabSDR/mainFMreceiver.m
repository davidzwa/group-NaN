clear all; clc; close all;

% Frequency data
fc = 102.7E6;
fs = 2.4E6;
gain = 20;
time = 5;  %sec
samples = time*fs;

%file specification
subFolder = 'Lab6_matlab';
file = 'capture.bin';
refresh_capture = false;    %only refresh when the dongle is present
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
%simpleSA(x,2^14,2400);  % example values, not-working

fc = 80E3;
[b,a] = butter(6,fc/fs);
y_B1 = filter(b, a, x);
y_N2 = decimate(y_B1, 10);
z_dis = discrim(y_N2);
fc2 = 20E3;
fs2 = 48E3;
[b2,a2] = butter(6,fc2/fs2);
z_B2 = filter(b2, a2, z_dis);
z_N2 = decimate(z_B2,5);

tau = 75E-6;
f3 = 1/(2*pi*tau);
a1 = exp(-2*pi*f3/fs2);
b3 = [1-a1];
a3 = [1, -a1];
y = filter(b3,a3,z_N2);
sound(y,fs2);
simpleSA(z_dis,2^14,2400);
function [z_out,z_B2,z_N2,z_dis,y_N1,y_B1] = FM_demod(x,B1,N1,B2,N2,fs) 


[b1, a1] = butter(6, B1 / fs, 'low');
y_B1 = filter(b1, a1, x);
y_N1 = downsample(y_B1, N1);
z_dis = discrim(y_N1);
[b2, a2] = butter(6, B2 / (fs / N1), 'low');
z_B2 = filter(b2, a2, z_dis);
z_N2 = downsample(z_B2, N2);

tau = 75e-6;
f3 = 1/(2*pi*tau);
a1 = exp(-2 * pi * f3 / (fs/N1/N2));
b3 = [1-a1];
a3 = [1, -a1];
z_out = filter(b3, a3, z_N2);

%z_out = z_N2;
end


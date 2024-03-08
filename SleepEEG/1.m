
[head, label] = edfread('sc4002e0.hyp');      % 读标签，舍弃最后一个标签
[header, recorddata] = edfread('sc4012e0_1.0.0.rec');   % 各通道的数据?

%% 画频谱
Fs = 100;                     % Sampling frequency 
T = 1/Fs;                     % Sample time 
N = size(recorddata,2);       % Length of signal 
t = (0:N-1)/Fs;               % Time vector  
 
xx1=abs(fft(eeg)); 
xx2=fftshift(abs(fft(eeg)));
 
% figure 
% subplot(4,1,1) 
% plot(eeg); 
% title('eeg'); 
% subplot(4,1,2) 
% plot(xx1); 
% title('abs(fft(eeg))'); 
% subplot(4,1,3) 
% plot(xx2); 
% title('fftshift(abs(fft(eeg)))'); 
% subplot(4,1,4) 
plot((1:N/2-1)*Fs/N,xx1(1:N/2-1)*2/N);
title('plot((1:N/2-1)*Fs/N,xx1(1:N/2-1)*2/N)结果图');


%% 滤波,分频
       
f = (0:N-1)*Fs/N;              %频率序列
Wn_Delta = [0.1*2 4*2]/Fs;     %设置通带为0.1-4Hz Delta波
Wn_Theta = [4*2 8*2]/Fs;       %设置通带为4-8Hz Theta波
Wn_Alpha = [8*2 12*2]/Fs;      %设置通带为8-12Hz Alpha波
Wn_Beta_1 = [16*2 18*2]/Fs;    %设置通带为16-18Hz Beta_1波
Wn_Beta_2 = [18*2 49.9*2]/Fs;    %设置通带为18-50Hz Beta_2波
 
[k,l] = butter(2,Wn_Beta_2);    %4阶IIR滤波器,可改频带
result = filtfilt(k,l,eeg);
tmp = fft(result);
eeg_IFFT = ifft(tmp);          %滤完波后的信号
 
figure,
subplot(211),plot(f(1:N/2),abs(tmp(1:N/2)*2/N));title('滤波后频谱结果，频率:0.1-4Hz');axis([0,100,-inf,inf])
subplot(212),plot(eeg_IFFT);title('脑波滤波后结果图像');
 
for i=1:length(eeg_IFFT)/3000    %wpcoef(wpt1,[n,i-1])是求第n层第i个节点的系数
    E_Beta_2(i)=norm(eeg_IFFT(3000*(i-1)+1:3000*(i-1)+3000),2);   % norm(A,2) = sum(abs(A).^p)^(1/p)
end
save('E_Beta_2.mat');


%% 特征提取
 
for i=1:length(E_Delta)
    Cw(1,i) = E_Alpha(1,i) * E_Beta_1(1,i) / E_Delta(1,i);
    CREM(1,i) = E_Theta(1,i) * E_Beta_2(1,i) / E_Delta(1,i);
end


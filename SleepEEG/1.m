
[head, label] = edfread('sc4002e0.hyp');      % ����ǩ���������һ����ǩ
[header, recorddata] = edfread('sc4012e0_1.0.0.rec');   % ��ͨ��������?

%% ��Ƶ��
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
title('plot((1:N/2-1)*Fs/N,xx1(1:N/2-1)*2/N)���ͼ');


%% �˲�,��Ƶ
       
f = (0:N-1)*Fs/N;              %Ƶ������
Wn_Delta = [0.1*2 4*2]/Fs;     %����ͨ��Ϊ0.1-4Hz Delta��
Wn_Theta = [4*2 8*2]/Fs;       %����ͨ��Ϊ4-8Hz Theta��
Wn_Alpha = [8*2 12*2]/Fs;      %����ͨ��Ϊ8-12Hz Alpha��
Wn_Beta_1 = [16*2 18*2]/Fs;    %����ͨ��Ϊ16-18Hz Beta_1��
Wn_Beta_2 = [18*2 49.9*2]/Fs;    %����ͨ��Ϊ18-50Hz Beta_2��
 
[k,l] = butter(2,Wn_Beta_2);    %4��IIR�˲���,�ɸ�Ƶ��
result = filtfilt(k,l,eeg);
tmp = fft(result);
eeg_IFFT = ifft(tmp);          %���겨����ź�
 
figure,
subplot(211),plot(f(1:N/2),abs(tmp(1:N/2)*2/N));title('�˲���Ƶ�׽����Ƶ��:0.1-4Hz');axis([0,100,-inf,inf])
subplot(212),plot(eeg_IFFT);title('�Բ��˲�����ͼ��');
 
for i=1:length(eeg_IFFT)/3000    %wpcoef(wpt1,[n,i-1])�����n���i���ڵ��ϵ��
    E_Beta_2(i)=norm(eeg_IFFT(3000*(i-1)+1:3000*(i-1)+3000),2);   % norm(A,2) = sum(abs(A).^p)^(1/p)
end
save('E_Beta_2.mat');


%% ������ȡ
 
for i=1:length(E_Delta)
    Cw(1,i) = E_Alpha(1,i) * E_Beta_1(1,i) / E_Delta(1,i);
    CREM(1,i) = E_Theta(1,i) * E_Beta_2(1,i) / E_Delta(1,i);
end


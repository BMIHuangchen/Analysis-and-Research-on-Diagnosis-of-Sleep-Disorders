[header, recorddata] = edfread('SC4001E0-PSG.edf')
%% 
%x=recod';
x = recorddata(1,1:524288)';
y=recorddata(2,1:524288)';
z=recorddata(3,1:524288)';
save('x.mat', 'x','y','z');
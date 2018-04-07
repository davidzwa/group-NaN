% 07-03-18 - David Zwart, 
%            Created SDR-less project folder for learning purposes

% Don't use dongle, but waveform
useSDR = false;
saveToFile = false; % We use matlab workspace... i think for now

SSID = 'DAVID_FAKE_WIFI'; % Network SSID
beaconInterval = 100; % In Time units (TU)
band = 5;             % Band, 5 or 2.4 GHz
chNum = 52;           % Channel number, corresponds to 5260MHz

% Generate Beacon frame
[mpduBits,fc] = helperGenerateBeaconFrame(chNum, band, beaconInterval, SSID);

%
%bits
%cfgFormat
%waveform = wlanWaveformGenerator(bits,cfgFormat);
cfgNonHT = wlanNonHTConfig;              % Create a wlanNonHTConfig object
cfgNonHT.PSDULength = numel(mpduBits)/8; % Set the PSDU length in bits

% The idle time is the length in seconds of an idle period after each
% generated packet. The idle time is set to the beacon interval.
txWaveform = wlanWaveformGenerator(mpduBits, cfgNonHT, 'IdleTime', beaconInterval*1024e-6);
Rs = wlanSampleRate(cfgNonHT);           % Get the input sampling rate

if saveToFile
    % The waveform is stored in a baseband file
    BBW = comm.BasebandFileWriter('nonHTBeaconPacket.bb', Rs, fc); %#ok<UNRCH>
    BBW(txWaveform);
    release(BBW);
end
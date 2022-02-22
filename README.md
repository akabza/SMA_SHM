# SMA_SHM
SMA Sunny Home Manager

This python code allows to read parameter from a SMA Sunny Home Manager 2.0.

The output may look like this examples:

SerialNo 300XXX346


Leistung  --- positiv ---  --- negativ ---<br>
Wirk       324.3  (1.4.0)     0.0  (2.4.0) W<br>
Blind        0.0  (3.4.0)   264.2  (4.4.0) W<br>
Schein     418.3  (9.4.0)     0.0 (10.4.0) W<br>
L-Faktor    77.5 (13.4.0) %<br>


Arbeit    ---- positiv ----  ---- negativ -----<br>
Wirk       4650.385 (1.8.0)  10776.101  (2.8.0) kWh<br>
Blind      1534.124 (3.8.0)   3550.931  (4.8.0) kWh<br>
Schein     6185.875 (9.8.0)  11049.777 (10.8.0) kWh<br>


Phasen           ------- L1 ------ ------- L2 ------ ------- L3 ------<br>
positiv            74.4 (21.4.0)     39.8 (41.4.0)    210.1 (61.4.0) W<br>
negativ             0.0 (22.4.0)      0.0 (42.4.0)      0.0 (62.4.0) W<br>
Strom               7.20 (31.4.0)     4.76 (51.4.0)    11.84 (71.4.0) A<br>
Spannung          229.920 (32.4.0)  230.484 (52.4.0)  231.268 (72.4.0) V<br>
Leistungsfaktor    55.1 (33.4.0)     55.1 (53.4.0)     55.1 (73.4.0) %<br>

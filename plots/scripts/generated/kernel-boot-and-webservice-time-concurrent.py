import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

firecracker_x10_kernel_boot = [
	827.23400,
	867.32700,
	796.71300,
	722.12400,
	873.04600,
	814.83500,
	808.52500,
	844.53200,
	860.44900,
	836.74100,
	862.53100,
	544.05400,
	897.59100,
	842.71700,
	1400.19400,
	865.74200,
	901.30400,
	859.36200,
	865.08900,
	922.34000,
	919.82700,
	822.72400,
	1309.68200,
	665.55000,
	870.66500,
	836.81700,
	852.01200,
	901.95100,
	884.81700,
	843.94900,
	889.80500,
	704.54400,
	831.81700,
	840.66300,
	812.49400,
	903.74200,
	659.04900,
	854.26500,
	835.07000,
	833.29000
]

firecracker_x10_webservice = [
	1506.50528,
	1073.67848,
	1435.60394,
	1311.89122,
	1478.34139,
	1274.45722,
	1421.57364,
	1433.41290,
	1032.50822,
	1196.20268,
	1264.26841,
	1200.80116,
	2212.04304,
	1260.07719,
	1902.87815,
	1039.27796,
	1161.05064,
	1086.15483,
	1459.48865,
	1352.40859,
	1226.24440,
	1025.57109,
	1878.83402,
	1277.00272,
	1020.85747,
	1098.40982,
	1077.30883,
	1051.77403,
	1487.52624,
	1363.94244,
	1362.38808,
	1201.21848,
	1295.10240,
	1315.16963,
	1286.23172,
	1109.81820,
	1215.80142,
	1231.10123,
	1450.49284,
	1283.73120
]

firecracker_x20_webservice = [
	3405.80919,
	1559.98051,
	2712.13552,
	2633.59266,
	3013.82574,
	1427.36557,
	2329.67524,
	2201.84338,
	3167.36727,
	1448.08882,
	1280.40175,
	2596.03458,
	1742.37438,
	1301.35652,
	2327.94513,
	2138.97079,
	2937.65632,
	1463.04191,
	2874.72565,
	2635.97481,
	3190.60533,
	2216.21526,
	1528.93060,
	2961.00153,
	2653.05957,
	1490.81684,
	2016.10431,
	2084.18570,
	2796.41614,
	1367.58195,
	2725.03962,
	2103.58075,
	2994.78055,
	1489.09197,
	1904.28617,
	1710.62562,
	2775.57512,
	1371.95959,
	2908.16411,
	1985.24329,
	3274.88962,
	1078.88135,
	2635.89147,
	2795.58008,
	2687.80382,
	1505.66399,
	1672.27746,
	3052.86680,
	2228.88197,
	1456.31110,
	2654.78988,
	2795.76591,
	1645.66797,
	2281.32286,
	1196.23926,
	2603.84760,
	1703.79516,
	1993.54718,
	2738.81287,
	2056.31275,
	1803.12607,
	1755.27661,
	2646.68840,
	3345.33619,
	2632.27497,
	1498.24509,
	3002.20424,
	3387.82650,
	3428.23955,
	1443.76143,
	2751.43478,
	1628.08451,
	2591.89728,
	1525.96461,
	1580.07974,
	2806.29027,
	1593.98959,
	1485.86179,
	2294.99433,
	1320.77997
]

qemu_x10_webservice = [
	2061.68022,
	2123.34468,
	2068.31641,
	2059.04444,
	1898.52753,
	2044.97267,
	2034.39062,
	1410.41973,
	2045.34912,
	2056.50077,
	1791.11967,
	2050.81856,
	2054.14683,
	2046.76147,
	2091.33657,
	1298.60299,
	2060.50147,
	1553.72132,
	2066.34829,
	1425.05469
]

qemu_x10_kernel_boot = [
	1808.02000,
	1785.44400,
	1814.50600,
	959.30600,
	1823.86800,
	1843.04300,
	1786.47600,
	841.46600,
	957.47000,
	943.35600
]

qemu_x20_webservice = [
	2461.65463,
	1194.63251,
	6318.35921,
	7990.48570,
	4899.72008,
	7955.71421,
	7911.51939,
	7663.64474,
	2066.74216,
	7727.31982,
	2049.67372,
	5802.00090,
	4514.83784,
	2048.02449,
	5323.16251,
	8467.13624,
	2052.68366,
	7833.76863,
	6883.89973,
	4394.01634
]

firecracker_x20_kernel_boot = [
	1204.44700,
	824.36700,
	1787.69900,
	1199.23300,
	844.43200,
	1576.95100,
	938.50900,
	824.74000,
	905.54900,
	866.83300,
	516.06300,
	815.73100,
	620.01900,
	1987.05500,
	839.47400,
	2013.45600,
	883.38600,
	1250.76400,
	1616.05000,
	965.29800,
	1256.70200,
	772.98100,
	827.40200,
	1395.90000,
	954.03600,
	871.77600,
	864.34800,
	1691.44000,
	910.21600,
	1296.94100,
	879.29400,
	1119.59600,
	608.66900,
	926.33000,
	838.47700,
	2257.68700,
	641.90100,
	2187.78900,
	861.54300,
	1878.58600,
	1619.62000,
	1222.85200,
	818.45300,
	1227.04300,
	1883.21900,
	1088.39700,
	833.05900,
	1967.74700,
	915.59300,
	856.05100,
	844.39000,
	868.45700,
	1533.19900,
	761.30700,
	1539.75100,
	1756.33600,
	904.74100,
	600.85500,
	1262.55500,
	1430.29800,
	2427.80300,
	1012.97500,
	785.19900,
	1771.76600,
	2764.79800,
	1159.09700,
	838.79000,
	1711.41900,
	879.12100,
	1163.59200,
	1050.61500,
	1010.61800,
	1410.67500,
	912.64300,
	833.47100,
	1408.59000,
	895.04800
]

qemu_x10_emulated_kernel_boot = [
	1635.29500,
	1340.00000,
	1421.46400,
	895.74900,
	1691.70600,
	1237.65600,
	1379.18500,
	1551.78300,
	1609.93400,
	1390.90000
]

qemu_x20_emulated_kernel_boot = [
	2227.71900,
	2153.67300,
	2077.32500,
	2189.70900,
	2513.94900,
	1968.49400,
	1425.81800,
	1969.73200,
	2824.23300,
	1491.00600,
	1524.03400,
	3898.57800,
	2205.78200,
	987.00000,
	2075.55500,
	3543.20400
]

qemu_x20_emulated_webservice = [
	9399.35159,
	9066.32819,
	8900.20204,
	7176.16540,
	9985.58551,
	9795.74414,
	6347.28192,
	9491.93390,
	5841.14698,
	9346.51703,
	7135.69970,
	8304.51995,
	5030.32842,
	2058.30614,
	5732.72607,
	5774.94422,
	9536.73092,
	3124.84295,
	9962.47447,
	9116.09705
]

qemu_x20_kernel_boot = [
	1769.69200,
	845.00600,
	1625.41800,
	4957.51400,
	2736.37800,
	2949.16500,
	3076.66200,
	3058.14400,
	1718.07500,
	2936.87400,
	1807.19800,
	2653.38900,
	2798.30300,
	1835.52200,
	2750.62900,
	3426.62700,
	1811.71300,
	2707.24100,
	2060.75600,
	1809.65300
]



labels = ['qemu x10','qemu x10 emulated','qemu x20','qemu x20 emulated','firecracker x10','firecracker x20']
y_pos = np.arange(len(labels))

import statistics as stats

web = [
	stats.mean(qemu_x10_webservice),
	stats.mean(qemu_x10_webservice),
	stats.mean(qemu_x20_webservice),
	stats.mean(qemu_x20_emulated_webservice),
	stats.mean(firecracker_x10_webservice),
	stats.mean(firecracker_x20_webservice)
]

kernel = [
	stats.mean(qemu_x10_kernel_boot),
	stats.mean(qemu_x10_emulated_kernel_boot),
	stats.mean(qemu_x20_kernel_boot),
	stats.mean(qemu_x20_emulated_kernel_boot),
	stats.mean(firecracker_x10_kernel_boot),
	stats.mean(firecracker_x20_kernel_boot)
]

bar2 = plt.bar(y_pos, web, align='center', alpha=0.5,  color=['orange'])
bar1 = plt.bar(y_pos, kernel, align='center', alpha=0.5,  color=['black'])

plt.xticks(y_pos, labels)

#plt.yticks(np.arange(0, 1800, 200))
plt.ylabel('Time (ms)')
plt.title('Stacked Mean Kernel Boot and Web Service Startup Times (Concurrent)')

#plt.legend((bar1[0], bar2[0]), ('Kernel boot time', 'Web service startup time'))
plt.legend((bar2[0], bar1[0]), ('Web service startup time', 'Kernel boot time'))

plt.gcf().subplots_adjust(bottom=0.30)
plt.xticks(rotation=45)
plt.savefig('plots/scripts/images/kernel-boot-and-webservice-time-concurrent.png')
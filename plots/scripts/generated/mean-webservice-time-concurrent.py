firecracker_x10 = [
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

firecracker_x20 = [
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

qemu_x10_emulated = [
	2061.68022,
	2068.31641,
	1898.52753,
	2034.39062,
	2045.34912,
	1791.11967,
	2054.14683,
	2091.33657,
	2060.50147,
	2066.34829
]

qemu_x20_emulated = [
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

qemu_x10 = [
	2123.34468,
	2059.04444,
	2044.97267,
	1410.41973,
	2056.50077,
	2050.81856,
	2046.76147,
	1298.60299,
	1553.72132,
	1425.05469
]

qemu_x20 = [
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



import statistics as stats
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('qemu x10','qemu x20','qemu x10 emulated','qemu x20 emulated','firecracker x10','firecracker x20')
y_pos = np.arange(len(objects))
performance = [
	stats.mean(qemu_x10),
	stats.mean(qemu_x20),
	stats.mean(qemu_x10_emulated),
	stats.mean(qemu_x20_emulated),
	stats.mean(firecracker_x10),
	stats.mean(firecracker_x20)
]

plt.bar(y_pos, performance, align='center', alpha=0.5, color=['orange', 'green', 'orange', 'green'])
plt.xticks(y_pos, objects)
plt.yticks(np.arange(0, 8000, 500))
plt.ylabel('Time (ms)')
plt.title('Mean Web Service Startup Time in ms')

plt.gcf().subplots_adjust(bottom=0.30)
plt.xticks(rotation=45)

#plt.show()
plt.savefig('plots/scripts/images/mean-webservice-time-concurrent.png')
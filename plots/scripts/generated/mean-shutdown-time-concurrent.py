qemu_x20 = [
	34328.26015,
	31689.63565,
	30872.08654,
	28483.81467,
	32425.93938,
	28078.47242,
	29168.91442,
	30856.47679,
	34672.52070,
	29533.35762,
	34635.56851,
	31902.19048,
	33533.99097,
	35559.15194,
	33067.23676,
	29170.10260,
	35492.02324,
	29539.72439,
	30216.14009,
	34024.39076
]

firecracker_x10 = [
	2382.45520,
	2437.74087,
	2455.41248,
	2358.02815,
	2369.20552,
	2356.90435,
	2480.68290,
	2318.00770,
	2346.40220,
	2341.39286,
	2385.12112,
	2354.94443,
	2492.85666,
	2379.13121,
	2537.68148,
	2474.21340,
	2436.13903,
	2342.49071,
	2327.06907,
	2337.45103,
	2309.07076,
	2450.10042,
	2536.04493,
	2379.23426,
	2353.20372,
	2332.38845,
	2502.34840,
	2429.26162,
	2382.95797,
	2377.40066,
	2441.43951,
	2353.35696,
	2340.54583,
	2328.51685,
	2345.01610,
	2286.97554,
	2303.52773,
	2376.68051,
	2468.75771,
	2352.14000
]

firecracker_x20 = [
	2951.25948,
	2612.69123,
	2958.49864,
	3000.61640,
	3037.56689,
	2599.32038,
	2350.28411,
	2331.51568,
	3026.04690,
	2619.30789,
	2486.63286,
	2873.48017,
	2884.08434,
	2352.80759,
	2927.01773,
	2282.29165,
	2786.01503,
	2462.46355,
	2445.80480,
	3110.00412,
	2466.30501,
	2508.23763,
	2880.36289,
	2465.47851,
	3189.60310,
	2581.61289,
	2784.40042,
	2821.56002,
	2780.24444,
	2393.75680,
	2600.85570,
	2556.84687,
	3261.35596,
	2365.04135,
	2712.02301,
	2795.37076,
	2793.96878,
	2423.26276,
	2451.27271,
	2762.86460,
	2486.65868,
	2438.71712,
	2803.13322,
	2473.32909,
	3018.36700,
	2430.64574,
	2320.11483,
	2420.78107,
	2310.74854,
	2440.80604,
	2506.18588,
	3081.78058,
	2876.06869,
	2386.37042,
	2490.95996,
	2708.55752,
	2934.41177,
	2650.40940,
	3018.82587,
	2399.95140,
	2307.07804,
	2660.10808,
	2676.37806,
	2452.39775,
	3313.43055,
	2460.12443,
	2628.89377,
	2319.76672,
	2442.49807,
	2439.36433,
	3063.74796,
	2754.61138,
	2375.05973,
	2539.27379,
	2904.88961,
	3062.45893,
	2889.10616,
	2451.93013,
	2988.57158,
	2496.72413
]

qemu_x10_emulated = [
	15908.73185,
	16222.13714,
	15842.44108,
	17012.62906,
	15549.20044,
	15542.08916,
	15554.98961,
	15271.07761,
	15718.05867,
	15162.19318
]

qemu_x20_emulated = [
	29357.82510,
	30662.23420,
	32520.74105,
	34155.62760,
	30784.49994,
	31526.67570,
	35022.92501,
	30330.37529,
	34428.86938,
	31830.47535,
	32386.99117,
	30102.91159,
	35671.56815,
	36672.09416,
	34864.31079,
	35235.24911,
	29633.86236,
	35998.21778,
	30680.14409,
	31333.52363
]

qemu_x10 = [
	15242.35278,
	16195.20112,
	16028.14253,
	16072.69002,
	15172.23902,
	15479.58662,
	16715.64501,
	15764.85923,
	17036.69884,
	16104.44938
]



import statistics as stats
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('qemu x10','qemu x10 emulated','qemu x20','qemu x20 emulated','firecracker x10','firecracker x20')
y_pos = np.arange(len(objects))
performance = [
	stats.mean(qemu_x10),
	stats.mean(qemu_x10_emulated),
	stats.mean(qemu_x20),
	stats.mean(qemu_x20_emulated),
	stats.mean(firecracker_x10),
	stats.mean(firecracker_x20)
]

plt.bar(y_pos, performance, align='center', alpha=0.5, color=['orange', 'green', 'orange', 'green'])
plt.xticks(y_pos, objects)
plt.yticks(np.arange(0, 36000, 3000))
plt.ylabel('Time (ms)')
plt.title('Mean VM Shutdown Time (Concurrent)')

plt.gcf().subplots_adjust(bottom=0.30)
plt.xticks(rotation=45)

#plt.show()
plt.savefig('plots/scripts/images/mean-shutdown-time-concurrent.png')
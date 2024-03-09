# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# fold4——Fpz-CZ
train_acc1 =[0.79226896,0.82520172,0.83498712,0.84233476,0.84729041,0.85127897,0.85471817,0.85741917,0.86080687,0.86408584,0.86576252,0.86834907,0.87054077,0.87275536,0.8753133,0.87778541,0.88023462,0.88123605,0.88370243,0.88747926,0.88897282,0.89068956,0.89298426,0.8954392,0.89777396,0.89974249,0.90251216,0.90428612,0.90655794,0.90851502,0.91006581,0.91228612,0.91409442,0.91555937,0.9181917,0.91880973,0.92170529,0.92118455,0.92382833,0.92494993,0.92830901,0.92832046,0.9299628,0.93240057,0.93315594,0.93457511,0.93621745,0.93687554,0.93641774,0.93958798,0.94046924,0.93986838,0.94302146,0.94294707,0.94337625,0.94499571,0.94597425,0.94774249,0.94896137,0.94877825,0.94993419,0.94936195,0.95106152,0.9514907,0.95289843,0.95463233,0.9549814,0.9541917,0.95592561,0.95689843,0.95705293,0.9571731,0.95812303,0.95761946,0.95925036,0.96025179,0.96090987,0.96149928,0.96172818,0.96154506,0.96289557,0.96445207,0.9633877,0.96421745,0.96425179,0.96551645,0.96497854,0.96584835,0.96663233,0.96775393,0.96751931,0.96816023,0.96798856,0.96802289,0.96857797,0.96882976,0.96939628,0.96993419,0.96989413,0.97027182]
val_acc1 =[0.758,0.774,0.7785,0.794,0.8025,0.806,0.8105,0.817,0.806,0.8045,0.818,0.818,0.8005,0.809,0.8185,0.8105,0.816,0.814,0.817,0.799,0.805,0.805,0.8215,0.8305,0.8095,0.8145,0.8205,0.8005,0.832,0.8045,0.825,0.81,0.8115,0.8225,0.8415,0.8295,0.823,0.8295,0.8175,0.83,0.8305,0.8305,0.831,0.827,0.827,0.8235,0.836,0.8335,0.827,0.8215,0.83,0.828,0.8315,0.827,0.8295,0.834,0.823,0.8075,0.8215,0.8245,0.816,0.8305,0.8345,0.8175,0.831,0.797,0.8235,0.8215,0.822,0.802,0.8325,0.8235,0.8315,0.824,0.8285,0.8085,0.812,0.81,0.8045,0.8105,0.81,0.8035,0.805,0.817,0.824,0.8135,0.8185,0.8035,0.821,0.827,0.8175,0.8145,0.819,0.824,0.8215,0.7955,0.8135,0.819,0.8235,0.8155]
#fold5——Pz-Oz
train_acc2 =[0.76505563,0.79704993,0.80778317,0.81375178,0.8193495,0.82211127,0.82657347,0.82986591,0.8333923,0.83613695,0.8394408,0.84233951,0.84521541,0.84852496,0.8496776,0.85321541,0.85735806,0.85984593,0.86267618,0.86551213,0.86751498,0.87065335,0.87316976,0.8760913,0.87855635,0.88199715,0.88356633,0.88598003,0.88794864,0.89121255,0.89303852,0.89499572,0.89686163,0.90050214,0.90215121,0.90320685,0.90619116,0.90616833,0.90898146,0.91048217,0.91359201,0.91471041,0.916097,0.91769472,0.91836805,0.92044508,0.92058773,0.9227903,0.92517546,0.92532953,0.92734379,0.92895292,0.93089301,0.93037946,0.93235949,0.93353495,0.93526961,0.93439658,0.93782026,0.93686733,0.93724964,0.94015977,0.93912126,0.94067332,0.94017118,0.94211127,0.94290442,0.94267047,0.94487874,0.94535235,0.94597432,0.94646505,0.94820542,0.94675606,0.94805706,0.94918117,0.94788017,0.95169757,0.95172611,0.95185735,0.95194294,0.95393438,0.95326676,0.95425963,0.95515549,0.95502996,0.95569757,0.95568616,0.957398,0.9575806,0.95761484,0.95938944,0.95908131,0.95966334,0.96056491,0.96081027,0.96031954,0.96116976,0.9614893,0.96116405]
val_acc2 =[0.782,0.826,0.854,0.87533333,0.88533333,0.892,0.89533333,0.89733333,0.89466667,0.902,0.89533333,0.89333333,0.89133333,0.88466667,0.884,0.88666667,0.888,0.888,0.884,0.878,0.876,0.88466667,0.888,0.88066667,0.87666667,0.876,0.884,0.87466667,0.87533333,0.864,0.866,0.87733333,0.868,0.85533333,0.86,0.866,0.854,0.86533333,0.85266667,0.85133333,0.86133333,0.85066667,0.85933333,0.848,0.84133333,0.82133333,0.812,0.82266667,0.80266667,0.842,0.824,0.844,0.84333333,0.83133333,0.85466667,0.82733333,0.84466667,0.838,0.83133333,0.794,0.83933333,0.82333333,0.838,0.864,0.83666667,0.85066667,0.85866667,0.826,0.84,0.844,0.80866667,0.83466667,0.836,0.86333333,0.854,0.852,0.82533333,0.82066667,0.84733333,0.84333333,0.846,0.83666667,0.846,0.84066667,0.82,0.81933333,0.838,0.83333333,0.78,0.80866667,0.82466667,0.824,0.83733333,0.83733333,0.81666667,0.83933333,0.83933333,0.836,0.846,0.79333333]
#fold3 ——EOG和Fpz-cz
train_acc3=[0.77651355,0.80964907,0.82123823,0.82952924,0.83428245,0.83853923,0.84226534,0.84689301,0.84944936,0.85173181,0.8528388,0.85665621,0.85943509,0.86051355,0.86324679,0.8660485,0.86745221,0.86964907,0.87306705,0.87576605,0.87718688,0.880097,0.88277889,0.8860485,0.88776605,0.88933524,0.89295863,0.89490442,0.89731241,0.89910414,0.90011983,0.9026077,0.90471327,0.90839372,0.90866191,0.91003709,0.91220542,0.91430528,0.91710699,0.9181398,0.91910414,0.92065621,0.921398,0.92342939,0.92413695,0.92462767,0.9272525,0.93025963,0.93055635,0.933398,0.93129244,0.93409986,0.93465906,0.93632525,0.93722682,0.93782596,0.93876177,0.93989729,0.94030813,0.9403709,0.94250499,0.94340086,0.94538088,0.94494722,0.94633381,0.94737803,0.94771469,0.949301,0.95044223,0.95011698,0.95122397,0.95150927,0.95184593,0.95366619,0.95370043,0.9541398,0.95567475,0.95548074,0.95569187,0.95698146,0.95778031,0.95717546,0.95964051,0.95984023,0.95918973,0.96005706,0.96149501,0.96082168,0.96258488,0.96282454,0.96319544,0.96335521,0.96415407,0.96357204,0.96492439,0.96504993,0.96531812,0.9651127,0.96593438,0.96611698]
val_acc3=[0.858,0.86733333,0.852,0.87866667,0.87933333,0.878,0.888,0.88933333,0.894,0.892,0.88866667,0.89066667,0.88266667,0.878,0.882,0.88066667,0.89,0.888,0.88933333,0.89133333,0.892,0.886,0.87666667,0.886,0.876,0.87866667,0.89,0.884,0.88466667,0.888,0.89266667,0.896,0.89466667,0.894,0.90733333,0.89733333,0.888,0.898,0.90466667,0.89333333,0.89466667,0.88866667,0.89666667,0.896,0.89066667,0.896,0.89133333,0.89733333,0.89666667,0.89266667,0.9,0.89733333,0.89266667,0.89533333,0.892,0.89333333,0.904,0.89,0.89333333,0.888,0.88866667,0.882,0.88866667,0.89333333,0.87933333,0.88866667,0.88533333,0.88533333,0.888,0.89333333,0.89066667,0.888,0.87666667,0.892,0.894,0.88666667,0.882,0.89533333,0.894,0.88666667,0.88933333,0.88666667,0.88933333,0.89733333,0.89133333,0.89466667,0.89466667,0.89333333,0.886,0.89333333,0.89666667,0.888,0.884,0.89066667,0.894,0.892,0.89866667,0.894,0.88666667,0.88933333]


font1 = {'size': 23, 'weight': 'normal', }
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.plot(train_acc1,color='#0000CD', label='训练', alpha=0.7,ms=10)
plt.plot(val_acc1,color='#FF0000', label='验证',alpha=0.7,ms=10)
plt.title(u'2类睡眠阶段',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
# plt.grid()


plt.subplot(1, 3, 2)
plt.plot(train_acc2, color='#0000CD',label='训练')
plt.plot(val_acc2, color='#FF0000', label='验证')
plt.title(u'3类睡眠阶段',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
# plt.grid()


plt.subplot(1, 3, 3)
plt.plot(train_acc3, color='#0000CD',label='训练')
plt.plot(val_acc3,color='#FF0000',  label='验证')
plt.title(u'5类睡眠阶段',font1)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend()
plt.show()
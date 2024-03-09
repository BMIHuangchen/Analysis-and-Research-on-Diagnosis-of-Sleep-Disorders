# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def roc(y_test, y_pre):
    from sklearn.metrics import roc_curve
    from sklearn.metrics import roc_auc_score as AUC
    import matplotlib.pyplot as plt

    # 利用roc_curve函数获得假阳性率FPR，和真阳性率recall，都是一系列值
    FPR, recall, thresholds = roc_curve(y_test, y_pre)
    # 计算AUC面积
    area = AUC(y_test, y_pre)

    # 画图
    plt.figure()
    plt.plot(FPR, recall, label='ROC curve (area = %0.2f)' % area)
    plt.legend(loc="lower right")
    plt.show()

#专家
data1 = [0.0      ,0.0      ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0        ,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,
]
#预测
data = [0.17012906,0.12996328,0.084913194,0.13310885,0.073673934,0.13157666,0.08739266,0.43000567,0.1675998,0.10728555,0.11995041,0.07897943,0.31984383,0.12382984,0.8885511,0.13111705,0.1143648,0.12688589,0.11102182,0.1762594,0.119481266,0.3377232,0.8970662,0.8840467,0.07846844,0.919386,0.13466722,0.3409009,0.10966027,0.09289998,0.10857326,0.10018441,0.08411789,0.16031173,0.11110428,0.12930778,0.15089431,0.10310206,0.08406225,0.09311658,0.09252891,0.4206911,0.081199825,0.10639995,0.08292416,0.27179068,0.19808078,0.15298653,0.1339427,0.8580119,0.80239844,0.24119994,0.08832574,0.88180643,0.30876765,0.13906923,0.68910164,0.816893,0.3823312,0.43168905,0.5374231,0.42776626,0.15913415,0.9097289,0.5832845,0.13463888,0.5612957,0.17857477,0.49314716,0.8475822,0.9099034,0.12100732,0.40642703,0.5035685,0.4905938,0.73474514,0.66051686,0.77983963,0.5242028,0.6426592,0.12495655,0.10099268,0.16802543,0.14793655,0.13474268,0.22793451,0.12878534,0.84300476,0.828611,0.41148344,0.41979814,0.41610005,0.8463952,0.60036534,0.7261035,0.6375945,0.2715281,0.15601635,0.8645201,0.11802322,0.11222693,0.874928,0.7860464,0.50204325,0.34419888,0.46036258,0.8764825,0.087451994,0.81396306,0.8798471,0.40106463,0.33720106,0.12341535,0.09809956,0.14805812,0.21349218,0.10085219,0.10885081,0.2618286,0.19739005,0.124311954,0.57868534,0.09363952,0.09949833,0.11683279,0.32786787,0.37885934,0.35751188,0.23420268,0.18069413,0.11890939,0.25,0.87546647,0.19873804,0.11755738,0.12177235,0.6716401,0.8241794,0.8125502,0.7326407,0.10395828,0.8900085,0.18098411,0.112615466,0.32402712,0.4676669,0.71863574,0.9018425,0.75556946,0.91203594,0.7648032,0.119610816,0.15599996,0.22836974,0.8065994,0.8102879,0.20045939,0.88870335,0.6691407,0.16569391,0.838197,0.5707921,0.85726726,0.70125085,0.8661729,0.46545604,0.65141666,0.9304144,0.8979219,0.33144087,0.27637067,0.7161643,0.74381095,0.9020193,0.86199135,0.82604825,0.4137712,0.6660261,0.8278599,0.47283527,0.37982368,0.46036035,0.5298751,0.6271394,0.5729733,0.30657533,0.073225886,0.12550476,0.24000993,0.30860734,0.9186049,0.16393849,0.3997305,0.7856149,0.2447303,0.10285124,0.5054629,0.33289102,0.92832196,0.13589913,0.2665704,0.26335177,0.08711845,0.8060546,0.6706396,0.12955934,0.27250725,0.1639331,0.095487386,0.57461023,0.13148138,0.11403644,0.10574287,0.15711546,0.5083037,0.3531196,0.37618157,0.788144,0.82921505,0.33521676,0.29930705,0.12242377,0.892332,0.10757899,0.40105057,0.53049916,0.3836279,0.4406931,0.6323522,0.8233569,0.22524756,0.8716589,0.7798208,0.6728821,0.90810907,0.89339495,0.89998764,0.8914074,0.47785977,0.912743,0.49215803,0.4087221,0.76120543,0.13954231,0.21441263,0.11768448,0.89374113,0.6425303,0.88106257,0.90340394,0.60913783,0.9198514,0.92229253,0.53810835,0.890744,0.695871,0.11906275,0.1101698,0.2431987,0.770095,0.91535234,0.54263407,0.1128999,0.89925754,0.08356881,0.18747395,0.44259864,0.14269099,0.71812403,0.11562669,0.88313484,0.12377757,0.8413626,0.2172176,0.3125763,0.24159712,0.8993262,0.120122135,0.7096971,0.91988087,0.10321385,0.098400176,0.09681076,0.30048174,0.22540829,0.13088009,0.14111772,0.08440879,0.19385684,0.1104103,0.09969112,0.07851401,0.11434138,0.81350404,0.20967734,0.0813725,0.5922996,0.14415774,0.7776275,0.19110647,0.115294814,0.14481294,0.305673,0.17043626,0.11616805,0.083988935,0.118175775,0.20302,0.13949868,0.17104968,0.19598526,0.095698714,0.0944401,0.12440273,0.078505516,0.074924976,0.08837631,0.10063529,0.096019775,0.31257674,0.110685706,0.11483699,0.10006264,0.16846219,0.11813331,0.27923572,0.12162146,0.095091045,0.3065313,0.36212745,0.087543696,0.93339646,0.16458017,0.8119478,0.59189063,0.46923533,0.37112662,0.89672405,0.66586864,0.34362447,0.08370119,0.09282911,0.08302316,0.4391212,0.9203981,0.3514391,0.12831208,0.10403955,0.29907537,0.08457592,0.15430143,0.8941575,0.72598416,0.52474916,0.70235467,0.40865678,0.44928163,0.524289,0.8575709,0.90003014,0.89713424,0.913289,0.6430472,0.88173217,0.8716179,0.48086405,0.66132253,0.911451,0.8619428,0.82538426,0.58417875,0.89999664,0.8684566,0.44769117,0.9069263,0.5051508,0.9078847,0.9307081,0.095571816,0.8965783,0.92640567,0.46476078,0.7387259,0.836061,0.8898011,0.8192502,0.910709,0.73255634,0.9335644,0.91704607,0.12444857,0.35685813,0.1258674,0.26067042,0.23752406,0.08429924,0.15584108,0.20998147,0.11034119,0.26831007,0.17511892,0.30370355,0.08653751,0.155346,0.90317297,0.8705863,0.20575294,0.8327633,0.11279282,0.31751788,0.12675264,0.07724187,0.0774878,0.26267493,0.27319953,0.09906256,0.07380071,0.1793448,0.07080078,0.2660219,0.09054607,0.5649115,0.08408064,0.14157969,0.8465651,0.092900604,0.38570097,0.10190758,0.1242888,0.31387097,0.9313372,0.83376276,0.08367348,0.2833239,0.27945083,0.0925273,0.09594372,0.28419614,0.21263397,0.15370527,0.64825517,0.19964862,0.20442244,0.21572393,0.44549128,0.88310826,0.42410788,0.84828633,0.5528279,0.24951541,0.8936682,0.15597576,0.3137261,0.15903297,0.099837005,0.25704756,0.37922278,0.5922351,0.12028602,0.88674533,0.655142,0.6765379,0.8823892,0.3247615,0.862731,0.8684667,0.25325277,0.930534,0.8554933,0.8887352,0.4254288,0.9026699,0.2407059,0.8344127,0.9303963,0.63281673,0.40885136,0.23135489,0.09212619,0.8949377,0.67352986,0.8955033,0.72624195,0.35535473,0.2911681,0.09148988,0.89324033,0.18061432,0.9030505,0.9283055,0.89711857,0.72640085,0.9154371,0.909773,0.90938497,0.9149679,0.8713894,0.79662585,0.9222692,0.1136145,0.10099137,0.9157262,0.3293512,0.45591575,0.10894544,0.08359768,0.90393907,0.3073739]
data2 = [0.17012906,0.12996328,0.084913194,0.13310885,0.073673934,0.13157666,0.08739266,0.43000567,0.1675998,0.10728555,0.11995041,0.07897943,0.31984383,0.12382984,0.8885511,0.13111705,0.1143648,0.12688589,0.11102182,0.1762594,0.119481266,0.3377232,0.8970662,0.8840467,0.07846844,0.919386,0.13466722,0.3409009,0.10966027,0.09289998,0.10857326,0.10018441,0.08411789,0.16031173,0.11110428,0.12930778,0.15089431,0.10310206,0.08406225,0.09311658,0.09252891,0.4206911,0.081199825,0.10639995,0.08292416,0.27179068,0.19808078,0.15298653,0.1339427,0.8580119,0.80239844,0.24119994,0.08832574,0.88180643,0.30876765,0.13906923,0.68910164,0.816893,0.3823312,0.43168905,0.5374231,0.42776626,0.15913415,0.9097289,0.5832845,0.13463888,0.5612957,0.17857477,0.49314716,0.8475822,0.9099034,0.12100732,0.40642703,0.5035685,0.4905938,0.73474514,0.66051686,0.77983963,0.5242028,0.6426592,0.12495655,0.10099268,0.16802543,0.14793655,0.13474268,0.22793451,0.12878534,0.84300476,0.828611,0.41148344,0.41979814,0.41610005,0.8463952,0.60036534,0.7261035,0.6375945,0.2715281,0.15601635,0.8645201,0.11802322,0.11222693,0.874928,0.7860464,0.50204325,0.34419888,0.46036258,0.8764825,0.087451994,0.81396306,0.8798471,0.40106463,0.33720106,0.12341535,0.09809956,0.14805812,0.21349218,0.10085219,0.10885081,0.2618286,0.19739005,0.124311954,0.57868534,0.09363952,0.09949833,0.11683279,0.32786787,0.37885934,0.35751188,0.23420268,0.18069413,0.11890939,0.25,0.87546647,0.19873804,0.11755738,0.12177235,0.6716401,0.8241794,0.8125502,0.7326407,0.10395828,0.8900085,0.18098411,0.112615466,0.32402712,0.4676669,0.71863574,0.9018425,0.75556946,0.91203594,0.7648032,0.119610816,0.15599996,0.22836974,0.8065994,0.8102879,0.20045939,0.88870335,0.6691407,0.16569391,0.838197,0.5707921,0.85726726,0.70125085,0.8661729,0.46545604,0.65141666,0.9304144,0.8979219,0.33144087,0.27637067,0.7161643,0.74381095,0.9020193,0.86199135,0.82604825,0.4137712,0.6660261,0.8278599,0.47283527,0.37982368,0.46036035,0.5298751,0.6271394,0.5729733,0.30657533,0.073225886,0.12550476,0.24000993,0.30860734,0.9186049,0.16393849,0.3997305,0.7856149,0.2447303,0.10285124,0.5054629,0.33289102,0.92832196,0.13589913,0.2665704,0.26335177,0.08711845,0.8060546,0.6706396,0.12955934,0.27250725,0.1639331,0.095487386,0.57461023,0.13148138,0.11403644,0.10574287,0.15711546,0.5083037,0.3531196,0.37618157,0.788144,0.82921505,0.33521676,0.29930705,0.12242377,0.892332,0.10757899,0.40105057,0.53049916,0.3836279,0.4406931,0.6323522,0.8233569,0.22524756,0.8716589,0.7798208,0.6728821,0.90810907,0.89339495,0.89998764,0.8914074,0.47785977,0.912743,0.49215803,0.4087221,0.76120543,0.13954231,0.21441263,0.11768448,0.89374113,0.6425303,0.88106257,0.90340394,0.60913783,0.9198514,0.92229253,0.53810835,0.890744,0.695871,0.11906275,0.1101698,0.2431987,0.770095,0.91535234,0.54263407,0.1128999,0.89925754,0.08356881,0.18747395,0.44259864,0.14269099,0.71812403,0.11562669,0.88313484,0.12377757,0.8413626,0.2172176,0.3125763,0.24159712,0.8993262,0.120122135,0.7096971,0.91988087,0.10321385,0.098400176,0.09681076,0.30048174,0.22540829,0.13088009,0.14111772,0.08440879,0.19385684,0.1104103,0.09969112,0.07851401,0.11434138,0.81350404,0.20967734,0.0813725,0.5922996,0.14415774,0.7776275,0.19110647,0.115294814,0.14481294,0.305673,0.17043626,0.11616805,0.083988935,0.118175775,0.20302,0.13949868,0.17104968,0.19598526,0.095698714,0.0944401,0.12440273,0.078505516,0.074924976,0.08837631,0.10063529,0.096019775,0.31257674,0.110685706,0.11483699,0.10006264,0.16846219,0.11813331,0.27923572,0.12162146,0.095091045,0.3065313,0.36212745,0.087543696,0.93339646,0.16458017,0.8119478,0.59189063,0.46923533,0.37112662,0.89672405,0.66586864,0.34362447,0.08370119,0.09282911,0.08302316,0.4391212,0.9203981,0.3514391,0.12831208,0.10403955,0.29907537,0.08457592,0.15430143,0.8941575,0.72598416,0.52474916,0.70235467,0.40865678,0.44928163,0.524289,0.8575709,0.90003014,0.89713424,0.913289,0.6430472,0.88173217,0.8716179,0.48086405,0.66132253,0.911451,0.8619428,0.82538426,0.58417875,0.89999664,0.8684566,0.44769117,0.9069263,0.5051508,0.9078847,0.9307081,0.095571816,0.8965783,0.92640567,0.46476078,0.7387259,0.836061,0.8898011,0.8192502,0.910709,0.73255634,0.9335644,0.91704607,0.12444857,0.35685813,0.1258674,0.26067042,0.23752406,0.08429924,0.15584108,0.20998147,0.11034119,0.26831007,0.17511892,0.30370355,0.08653751,0.155346,0.90317297,0.8705863,0.20575294,0.8327633,0.11279282,0.31751788,0.12675264,0.07724187,0.0774878,0.26267493,0.27319953,0.09906256,0.07380071,0.1793448,0.07080078,0.2660219,0.09054607,0.5649115,0.08408064,0.14157969,0.8465651,0.092900604,0.38570097,0.10190758,0.1242888,0.31387097,0.9313372,0.83376276,0.08367348,0.2833239,0.27945083,0.0925273,0.09594372,0.28419614,0.21263397,0.15370527,0.64825517,0.19964862,0.20442244,0.21572393,0.44549128,0.88310826,0.42410788,0.84828633,0.5528279,0.24951541,0.8936682,0.15597576,0.3137261,0.15903297,0.099837005,0.25704756,0.37922278,0.5922351,0.12028602,0.88674533,0.655142,0.6765379,0.8823892,0.3247615,0.862731,0.8684667,0.25325277,0.930534,0.8554933,0.8887352,0.4254288,0.9026699,0.2407059,0.8344127,0.9303963,0.63281673,0.40885136,0.23135489,0.09212619,0.8949377,0.67352986,0.8955033,0.72624195,0.35535473,0.2911681,0.09148988,0.89324033,0.18061432,0.9030505,0.9283055,0.89711857,0.72640085,0.9154371,0.909773,0.90938497,0.9149679,0.8713894,0.79662585,0.9222692,0.1136145,0.10099137,0.9157262,0.3293512,0.45591575,0.10894544,0.08359768,0.90393907,0.3073739]

roc(data1, data)





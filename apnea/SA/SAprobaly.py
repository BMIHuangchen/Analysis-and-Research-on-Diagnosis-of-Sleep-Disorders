# -*- coding:utf-8 -*-
import sys
reload(sys)
import matplotlib
print(matplotlib.matplotlib_fname())
sys.setdefaultencoding('utf-8')
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

Bottom = (0.82987094, 0.87003672, 0.915086806, 0.86689115, 0.926326066, 0.86842334, 0.91260734, 0.56999433, 0.7324002000000001, 0.69271445, 0.88004959, 0.97102057, 0.6801561700000001, 0.87617016, 0.7114488999999999, 0.8688829499999999, 0.8856352, 0.8731141099999999, 0.8889781800000001, 0.8237406, 0.880518734, 0.6622768, 0.7029338, 0.7159533, 0.92153156, 0.780614, 0.86533278, 0.6590990999999999, 0.89033973, 0.90710002, 0.89142674, 0.89981559, 0.91588211, 0.83968827, 0.8888957200000001, 0.87069222, 0.84910569, 0.89689794, 0.91593775, 0.90688342, 0.90747109, 0.5793089, 0.918800175, 0.89360005, 0.91707584, 0.7282093199999999, 0.80191922, 0.84701347, 0.8660573, 0.14198809999999995, 0.19760155999999995, 0.75880006, 0.91167426, 0.11819356999999997, 0.6912323499999999, 0.86093077, 0.31089836000000004, 0.18310700000000002, 0.6176688, 0.56831095, 0.46257689999999996, 0.5722337399999999, 0.84086585, 0.09027110000000005, 0.4167155, 0.86536112, 0.43870430000000005, 0.82142523, 0.5068528400000001, 0.15241780000000005, 0.09009659999999997, 0.87899268, 0.59357297, 0.4964315, 0.5094061999999999, 0.26525486, 0.33948314, 0.22016037, 0.47579720000000003, 0.3573408, 0.87504345, 0.8990073199999999, 0.83197457, 0.85206345, 0.86525732, 0.77206549, 0.87121466, 0.15699523999999998, 0.171389, 0.58851656, 0.5802018600000001, 0.58389995, 0.15360479999999999, 0.39963466000000003, 0.2738965, 0.36240550000000005, 0.7284719, 0.84398365, 0.1354799, 0.88197678, 0.8877730699999999, 0.12507199999999996, 0.21395359999999997, 0.49795674999999995, 0.65580112, 0.53963742, 0.12351749999999995, 0.912548006, 0.18603694000000004, 0.1201529, 0.59893537, 0.6627989400000001, 0.87658465, 0.90190044, 0.85194188, 0.78650782, 0.89914781, 0.89114919, 0.7381713999999999, 0.80260995, 0.875688046, 0.42131465999999995, 0.90636048, 0.90050167, 0.88316721, 0.67213213, 0.62114066, 0.64248812, 0.76579732, 0.81930587, 0.88109061, 0.75, 0.12453353, 0.8012619599999999, 0.88244262, 0.87822765, 0.32835990000000004, 0.1758206, 0.1874498, 0.26735929999999997, 0.89604172, 0.10999150000000002, 0.81901589, 0.887384534, 0.67597288, 0.5323331, 0.28136426000000003, 0.09815750000000001, 0.24443053999999997, 0.08796406000000001, 0.23519679999999998, 0.880389184, 0.8440000400000001, 0.77163026, 0.19340060000000003, 0.18971210000000005, 0.79954061, 0.11129665, 0.33085929999999997, 0.83430609, 0.16180300000000003, 0.4292079, 0.14273274000000002, 0.29874915, 0.13382709999999998, 0.5345439599999999, 0.34858334, 0.06958560000000003, 0.10207809999999995, 0.66855913, 0.7236293300000001, 0.2838357, 0.25618905000000003, 0.09798070000000003, 0.13800864999999995, 0.17395174999999996, 0.5862288, 0.33397390000000005, 0.17214010000000002, 0.52716473, 0.62017632, 0.53963965, 0.47012489999999996, 0.3728606, 0.4270267, 0.69342467, 0.926774114, 0.87449524, 0.75999007, 0.69139266, 0.08139510000000005, 0.83606151, 0.6002695, 0.2143851, 0.7552696999999999, 0.89714876, 0.49453709999999995, 0.6671089800000001, 0.07167804, 0.86410087, 0.7334296, 0.73664823, 0.91288155, 0.19394540000000005, 0.3293604, 0.87044066, 0.72749275, 0.8360669000000001, 0.904512614, 0.42538977, 0.86851862, 0.88596356, 0.89425713, 0.84288454, 0.4916963, 0.6468804, 0.62381843, 0.21185600000000004, 0.17078495000000005, 0.66478324, 0.70069295, 0.87757623, 0.10766799999999999, 0.89242101, 0.59894943, 0.46950084000000003, 0.6163721, 0.5593068999999999, 0.36764779999999997, 0.10664309999999999, 0.17475244, 0.12834109999999999, 0.12017920000000004, 0.32711789999999996, 0.09189093000000004, 0.10660504999999998, 0.10001236000000002, 0.10859260000000004, 0.52214023, 0.08725700000000003, 0.50784197, 0.5912779, 0.23879457000000004, 0.86045769, 0.78558737, 0.88231552, 0.10625887, 0.3574697, 0.11893743000000001, 0.09659605999999998, 0.39086217, 0.08014860000000001, 0.07770747, 0.061891649999999965, 0.10925600000000002, 0.304129, 0.88093725, 0.8898302, 0.7568013, 0.22990500000000003, 0.08464766000000001, 0.05736593000000001, 0.08710010000000001, 0.10074245999999998, 0.91643119, 0.81252605, 0.5574013600000001, 0.85730901, 0.28187597, 0.88437331, 0.11686516000000002, 0.87622243, 0.15863740000000004, 0.7827824, 0.6874237000000001, 0.75840288, 0.10067380000000004, 0.879877865, 0.29030290000000003, 0.08011913000000004, 0.8967861500000001, 0.901599824, 0.90318924, 0.6995182600000001, 0.7745917099999999, 0.86911991, 0.85888228, 0.91559121, 0.80614316, 0.8895897, 0.90030888, 0.92148599, 0.88565862, 0.18649596000000002, 0.79032266, 0.9186275, 0.40770039999999996, 0.85584226, 0.22237249999999997, 0.80889353, 0.884705186, 0.85518706, 0.694327, 0.82956374, 0.88383195, 0.916011065, 0.881824225, 0.79698, 0.86050132, 0.82895032, 0.80401474, 0.904301286, 0.9055599, 0.87559727, 0.911494484, 0.915075024, 0.91162369, 0.89936471, 0.903980225, 0.68742326, 0.8893142940000001, 0.88516301, 0.89993736, 0.8315378099999999, 0.88186669, 0.72076428, 0.87837854, 0.904908955, 0.6934686999999999, 0.63787255, 0.912456304, 0.06660354000000002, 0.83541983, 0.1880522, 0.40810937, 0.5307646699999999, 0.6288733799999999, 0.10327595, 0.33413136, 0.65637553, 0.91629881, 0.90717089, 0.91697684, 0.5608788, 0.0796019, 0.6485609, 0.8716879200000001, 0.89596045, 0.70092463, 0.91542408, 0.84569857, 0.10584249999999995, 0.27401584, 0.47525083999999995, 0.29764533000000004, 0.59134322, 0.55071837, 0.475711, 0.14242909999999998, 0.09996985999999997, 0.10286576000000003, 0.08671099999999998, 0.35695279999999996, 0.11826782999999996, 0.12838210000000005, 0.51913595, 0.33867747000000004, 0.08854899999999999, 0.1380572, 0.17461574000000002, 0.41582125000000003, 0.10000335999999999, 0.13154339999999998, 0.55230883, 0.09307370000000004, 0.4948492, 0.09211530000000001, 0.06929189999999996, 0.904428184, 0.10342169999999995, 0.07359433000000004, 0.53523922, 0.26127409999999995, 0.16393899999999995, 0.11019889999999999, 0.08074979999999998, 0.08929100000000001, 0.06744366000000002, 0.06643560000000004, 0.08295392999999995, 0.87555143, 0.64314187, 0.8741326, 0.7393295799999999, 0.76247594, 0.91570076, 0.84415892, 0.79001853, 0.88965881, 0.7316899299999999, 0.8248810799999999, 0.69629645, 0.91346249, 0.844654, 0.09682703000000004, 0.12941369999999996, 0.79424706, 0.16723670000000002, 0.88720718, 0.68248212, 0.87324736, 0.92275813, 0.9225122, 0.73732507, 0.7268004699999999, 0.90093744, 0.92619929, 0.8206552, 0.92919922, 0.7339781000000001, 0.90945393, 0.4350885, 0.91591936, 0.85842031, 0.15343490000000004, 0.907099396, 0.61429903, 0.89809242, 0.8757112, 0.68612903, 0.06866280000000002, 0.16623723999999995, 0.91632652, 0.7166760999999999, 0.72054917, 0.9074727, 0.90405628, 0.7158038600000001, 0.78736603, 0.84629473, 0.35174483, 0.80035138, 0.79557756, 0.78427607, 0.5545087200000001, 0.11689174000000002, 0.57589212, 0.15171367000000002, 0.44717209999999996, 0.75048459, 0.10633179999999998, 0.84402424, 0.6862739, 0.8409670300000001, 0.900162995, 0.74295244, 0.62077722, 0.4077649, 0.87971398, 0.11325467, 0.344858, 0.3234621, 0.11761080000000002, 0.6752385000000001, 0.13726899999999997, 0.13153329999999996, 0.74674723, 0.06946600000000003, 0.1445067, 0.11126480000000005, 0.5745712000000001, 0.09733009999999997, 0.7592941, 0.1655873, 0.06960370000000005, 0.36718326999999995, 0.59114864, 0.76864511, 0.90787381, 0.10506230000000005, 0.32647013999999996, 0.1044967, 0.27375805, 0.64464527, 0.7088319000000001, 0.90851012, 0.10675966999999997, 0.81938568, 0.09694950000000002, 0.0716945, 0.10288143000000005, 0.27359915, 0.0845629, 0.09022699999999995, 0.09061503000000004, 0.08503210000000005, 0.12861060000000002, 0.20337415000000003, 0.07773079999999999, 0.8863855, 0.89900863, 0.08427379999999995, 0.6706487999999999, 0.54408425, 0.8910545599999999, 0.91640232, 0.09606093000000004, 0.6926261)
Center = (0.17012906, 0.12996328, 0.084913194, 0.13310885, 0.073673934, 0.13157666, 0.08739266, 0.43000567, 0.2675998, 0.30728555, 0.11995041, 0.02897943, 0.31984383, 0.12382984, 0.2885511, 0.13111705, 0.1143648, 0.12688589, 0.11102182, 0.1762594, 0.119481266, 0.3377232, 0.2970662, 0.2840467, 0.07846844, 0.219386, 0.13466722, 0.3409009, 0.10966027, 0.09289998, 0.10857326, 0.10018441, 0.08411789, 0.16031173, 0.11110428, 0.12930778, 0.15089431, 0.10310206, 0.08406225, 0.09311658, 0.09252891, 0.4206911, 0.081199825, 0.10639995, 0.08292416, 0.27179068, 0.19808078, 0.15298653, 0.1339427, 0.8580119, 0.80239844, 0.24119994, 0.08832574, 0.88180643, 0.30876765, 0.13906923, 0.68910164, 0.816893, 0.3823312, 0.43168905, 0.5374231, 0.42776626, 0.15913415, 0.9097289, 0.5832845, 0.13463888, 0.5612957, 0.17857477, 0.49314716, 0.8475822, 0.9099034, 0.12100732, 0.40642703, 0.5035685, 0.4905938, 0.73474514, 0.66051686, 0.77983963, 0.5242028, 0.6426592, 0.12495655, 0.10099268, 0.16802543, 0.14793655, 0.13474268, 0.22793451, 0.12878534, 0.84300476, 0.828611, 0.41148344, 0.41979814, 0.41610005, 0.8463952, 0.60036534, 0.7261035, 0.6375945, 0.2715281, 0.15601635, 0.8645201, 0.11802322, 0.11222693, 0.874928, 0.7860464, 0.50204325, 0.34419888, 0.46036258, 0.8764825, 0.087451994, 0.81396306, 0.8798471, 0.40106463, 0.33720106, 0.12341535, 0.09809956, 0.14805812, 0.21349218, 0.10085219, 0.10885081, 0.2618286, 0.19739005, 0.124311954, 0.57868534, 0.09363952, 0.09949833, 0.11683279, 0.32786787, 0.37885934, 0.35751188, 0.23420268, 0.18069413, 0.11890939, 0.25, 0.87546647, 0.19873804, 0.11755738, 0.12177235, 0.6716401, 0.8241794, 0.8125502, 0.7326407, 0.10395828, 0.8900085, 0.18098411, 0.112615466, 0.32402712, 0.4676669, 0.71863574, 0.9018425, 0.75556946, 0.91203594, 0.7648032, 0.119610816, 0.15599996, 0.22836974, 0.8065994, 0.8102879, 0.20045939, 0.88870335, 0.6691407, 0.16569391, 0.838197, 0.5707921, 0.85726726, 0.70125085, 0.8661729, 0.46545604, 0.65141666, 0.9304144, 0.8979219, 0.33144087, 0.27637067, 0.7161643, 0.74381095, 0.9020193, 0.86199135, 0.82604825, 0.4137712, 0.6660261, 0.8278599, 0.47283527, 0.37982368, 0.46036035, 0.5298751, 0.6271394, 0.5729733, 0.30657533, 0.073225886, 0.12550476, 0.24000993, 0.30860734, 0.9186049, 0.16393849, 0.3997305, 0.7856149, 0.2447303, 0.10285124, 0.5054629, 0.33289102, 0.92832196, 0.13589913, 0.2665704, 0.26335177, 0.08711845, 0.8060546, 0.6706396, 0.12955934, 0.27250725, 0.1639331, 0.095487386, 0.57461023, 0.13148138, 0.11403644, 0.10574287, 0.15711546, 0.5083037, 0.3531196, 0.37618157, 0.788144, 0.82921505, 0.33521676, 0.29930705, 0.12242377, 0.892332, 0.10757899, 0.40105057, 0.53049916, 0.3836279, 0.4406931, 0.6323522, 0.8933569, 0.82524756, 0.8716589, 0.8798208, 0.6728821, 0.90810907, 0.89339495, 0.89998764, 0.8914074, 0.47785977, 0.912743, 0.49215803, 0.4087221, 0.76120543, 0.13954231, 0.21441263, 0.11768448, 0.89374113, 0.6425303, 0.88106257, 0.90340394, 0.60913783, 0.9198514, 0.92229253, 0.93810835, 0.890744, 0.695871, 0.11906275, 0.1101698, 0.2431987, 0.770095, 0.91535234, 0.94263407, 0.9128999, 0.89925754, 0.08356881, 0.18747395, 0.44259864, 0.14269099, 0.71812403, 0.11562669, 0.88313484, 0.12377757, 0.8413626, 0.2172176, 0.3125763, 0.24159712, 0.8993262, 0.120122135, 0.7096971, 0.91988087, 0.10321385, 0.098400176, 0.09681076, 0.30048174, 0.22540829, 0.13088009, 0.14111772, 0.08440879, 0.19385684, 0.1104103, 0.09969112, 0.07851401, 0.11434138, 0.81350404, 0.20967734, 0.0813725, 0.5922996, 0.14415774, 0.7776275, 0.19110647, 0.115294814, 0.14481294, 0.305673, 0.17043626, 0.11616805, 0.083988935, 0.118175775, 0.20302, 0.13949868, 0.17104968, 0.19598526, 0.095698714, 0.0944401, 0.12440273, 0.088505516, 0.084924976, 0.08837631, 0.10063529, 0.096019775, 0.31257674, 0.110685706, 0.11483699, 0.10006264, 0.16846219, 0.11813331, 0.27923572, 0.12162146, 0.095091045, 0.3065313, 0.36212745, 0.087543696, 0.93339646, 0.16458017, 0.8119478, 0.59189063, 0.46923533, 0.37112662, 0.89672405, 0.66586864, 0.34362447, 0.08370119, 0.09282911, 0.08302316, 0.4391212, 0.9203981, 0.3514391, 0.12831208, 0.10403955, 0.29907537, 0.08457592, 0.15430143, 0.8941575, 0.72598416, 0.52474916, 0.70235467, 0.40865678, 0.44928163, 0.524289, 0.8575709, 0.90003014, 0.89713424, 0.913289, 0.6430472, 0.88173217, 0.8716179, 0.48086405, 0.66132253, 0.911451, 0.8619428, 0.82538426, 0.58417875, 0.89999664, 0.8684566, 0.44769117, 0.9069263, 0.5051508, 0.9078847, 0.9307081, 0.095571816, 0.8965783, 0.92640567, 0.46476078, 0.7387259, 0.836061, 0.8898011, 0.9192502, 0.910709, 0.93255634, 0.9335644, 0.91704607, 0.12444857, 0.35685813, 0.1258674, 0.26067042, 0.23752406, 0.08429924, 0.15584108, 0.20998147, 0.11034119, 0.26831007, 0.17511892, 0.30370355, 0.08653751, 0.155346, 0.90317297, 0.8705863, 0.20575294, 0.8327633, 0.11279282, 0.31751788, 0.12675264, 0.07724187, 0.0774878, 0.26267493, 0.27319953, 0.09906256, 0.07380071, 0.1793448, 0.07080078, 0.2660219, 0.09054607, 0.5649115, 0.08408064, 0.14157969, 0.8465651, 0.092900604, 0.38570097, 0.10190758, 0.1242888, 0.31387097, 0.9313372, 0.83376276, 0.08367348, 0.2833239, 0.27945083, 0.0925273, 0.09594372, 0.28419614, 0.21263397, 0.15370527, 0.64825517, 0.19964862, 0.20442244, 0.21572393, 0.44549128, 0.88310826, 0.42410788, 0.84828633, 0.5528279, 0.24951541, 0.8936682, 0.15597576, 0.3137261, 0.15903297, 0.099837005, 0.25704756, 0.37922278, 0.5922351, 0.12028602, 0.88674533, 0.655142, 0.6765379, 0.8823892, 0.3247615, 0.862731, 0.8684667, 0.25325277, 0.930534, 0.8554933, 0.8887352, 0.4254288, 0.9026699, 0.2407059, 0.8344127, 0.9303963, 0.63281673, 0.40885136, 0.23135489, 0.09212619, 0.8949377, 0.67352986, 0.8955033, 0.72624195, 0.35535473, 0.2911681, 0.09148988, 0.89324033, 0.18061432, 0.9030505, 0.9283055, 0.89711857, 0.72640085, 0.9154371, 0.909773, 0.90938497, 0.9149679, 0.8713894, 0.79662585, 0.9222692, 0.1136145, 0.10099137, 0.9157262, 0.3293512, 0.45591575, 0.10894544, 0.08359768, 0.90393907, 0.3073739)

wake=    ()
N1=      ()
N2=      ()
N3=      ()
REM=     ()
plt.figure(figsize=(15,5))
font1={'size':34,'weight' : 'normal',}
font2={'size':25,'weight' : 'normal',}
plt.title(u'预测统计',font1)
#x坐标的间隔设置和文字设置
N = len(Bottom)
ind = np.arange(N)  #[ 0  1  2  3  4  5  6  7  8  9 10 11 12]
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)

#y坐标的文字设置和间隔设置
plt.ylabel(u'概率',font2)
plt.yticks()


width = 1  # 设置条形图一个长条的宽度
p1 = plt.bar(ind, Bottom, width,label=('预测为N概率'), color='#2976bb')
p2 = plt.bar(ind, Center, width,label=('预测为A概率'),bottom=Bottom,color='#ffffb6')
# p3 = plt.bar(ind, Top, width, bottom=sum2,color='#ffffb6')
# p4 = plt.bar(ind, led, width, bottom=sum3,color='#9be5aa')
# p5 = plt.bar(ind, okk, width, bottom=sum4,color='#2976bb')


plt.legend(fontsize='25')

plt.show()
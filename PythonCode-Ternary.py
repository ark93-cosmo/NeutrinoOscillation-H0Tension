import matplotlib.pyplot as plt
!pip install mpltern
import mpltern#This is the package that is particular for ternary plots. See https://mpltern.readthedocs.io/en/latest/ for more details
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from mpltern.ternary.datasets import get_scatter_points
fig = plt.figure(figsize=(20.8, 15.8))
fig.subplots_adjust(left=0.05, right=0.45, wspace=0.2, hspace=0.4)

ax = fig.add_subplot(321, projection='ternary')
ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)
#This is to choose the label of the axis to be on the side of the triangle and not on the corners
ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')
#See Probabilities.nb file for these values
#NH-EU,Pure-Electron
ax.plot(0.00511318, 0.0106531, 0.984234,color='red',marker='d')
ax.plot(0.00936119, 0.0199585, 0.97068,color='magenta',marker='d')
ax.plot(0.0172579,0.0379832, 0.944759,color='darkmagenta',marker='d')
ax.plot(0.0496939, 0.119052, 0.831254,color='blue',marker='d')
ax.plot(0.132784, 0.360401, 0.506815,color='dodgerblue',marker='d')
ax.plot(0.176168, 0.494058, 0.329774,color='aqua',marker='d')
ax.plot(0.192375, 0.541326, 0.266299,color='orange',marker='d')
ax.plot(0.222185, 0.612622, 0.165194,color='green',marker='d')
ax.plot(0.232017, 0.62556, 0.142422,color='gold',marker='d')
#NH-LU,Pure-Electron

ax.plot(0.00436647, 0.00905251, 0.986581,color='red',marker='*')
ax.plot(0.00801001, 0.0169648, 0.975025,color='magenta',marker='*')
ax.plot(0.0148138,0.0323155, 0.952871,color='darkmagenta',marker='*')
ax.plot(0.0431395, 0.101899, 0.854961,color='blue',marker='*')
ax.plot(0.118724, 0.31722, 0.564057,color='dodgerblue',marker='*')
ax.plot(0.16054, 0.446397, 0.393063,color='aqua',marker='*')
ax.plot(0.176805, 0.495971, 0.327224,color='orange',marker='*')
ax.plot(0.208292, 0.583246, 0.208462,color='green',marker='*')
ax.plot(0.219491, 0.607711, 0.172799,color='gold',marker='*')

########################################################################
ax = fig.add_subplot(322, projection='ternary')

ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')
#IH-EU,Pure-Electron
ax.plot(0.00599377, 0.00844944, 0.985557,color='red',marker='d')
ax.plot(0.0112341, 0.015639, 0.973127,color='magenta',marker='d')
ax.plot(0.0214061,0.0292761, 0.949318,color='darkmagenta',marker='d')
ax.plot(0.0676375, 0.0879063, 0.844456,color='blue',marker='d')
ax.plot(0.212982, 0.249462, 0.537556,color='dodgerblue',marker='d')
ax.plot(0.30341, 0.33399, 0.362599,color='aqua',marker='d')
ax.plot(0.339432, 0.363307, 0.297261,color='orange',marker='d')
ax.plot(0.407104, 0.407288, 0.185608,color='green',marker='d')
ax.plot(0.428728, 0.415501, 0.155771,color='gold',marker='d')
#IH-LU,Pure-Electron

ax.plot(0.00509299, 0.00719879, 0.987708,color='red',marker='*')
ax.plot(0.00954746, 0.0133395, 0.977113,color='magenta',marker='*')
ax.plot(0.0182042,0.025022, 0.956774,color='darkmagenta',marker='*')
ax.plot(0.0577804, 0.0757755, 0.866444,color='blue',marker='*')
ax.plot(0.185776, 0.221527, 0.592696,color='dodgerblue',marker='*')
ax.plot(0.26975, 0.304151, 0.426099,color='aqua',marker='*')
ax.plot(0.304808, 0.335181, 0.360011,color='orange',marker='*')
ax.plot(0.375564, 0.389145, 0.235291,color='green',marker='*')
ax.plot(0.401035, 0.404238, 0.194727,color='gold',marker='*')
EU_label = mlines.Line2D([], [], color='black', marker='d', linestyle='None',
                          markersize=8, label='EU')
LU_label = mlines.Line2D([], [], color='black', marker='*', linestyle='None',
                          markersize=8, label='LU')
z_005_label = mlines.Line2D([], [], color='red', marker='.', linestyle='None',
                          markersize=8, label='z=0.05')
z_007_label = mlines.Line2D([], [], color='magenta', marker='.', linestyle='None',
                          markersize=8, label='z=0.07')
z_01_label = mlines.Line2D([], [], color='darkmagenta', marker='.', linestyle='None',
                          markersize=8, label='z=0.1')
z_02_label = mlines.Line2D([], [], color='blue', marker='.', linestyle='None',
                          markersize=8, label='z=0.2')
z_05_label = mlines.Line2D([], [], color='dodgerblue', marker='.', linestyle='None',
                          markersize=8, label='z=0.5')
z_08_label = mlines.Line2D([], [], color='aqua', marker='.', linestyle='None',
                          markersize=8, label='z=0.8')
z_1_label = mlines.Line2D([], [], color='orange', marker='.', linestyle='None',
                          markersize=8, label='z=1')
z_2_label = mlines.Line2D([], [], color='green', marker='.', linestyle='None',
                          markersize=8, label='z=2')
z_4_label = mlines.Line2D([], [], color='gold', marker='.', linestyle='None',
                          markersize=8, label='z=4')
#z_005_label = mlines.Line2D([], [], color='red', marker='.', linestyle='None',markersize=8, label='z=0.05')
plt.legend(handles=[EU_label,LU_label,z_005_label,z_007_label,z_01_label,z_02_label,z_05_label,z_08_label,
                    z_1_label,z_2_label,z_4_label,],loc='center right', bbox_to_anchor=(1.5, 0.5))
plt.savefig('Ternary-PureElectron.png', dpi=150, transparent=True)

############################Pure-Muon###############################################
ax = fig.add_subplot(323, projection='ternary')

ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')
#NH-EU,Pure-Muon
ax.plot(0.9882, 0.0062221, 0.00557828,color='red',marker='d')
ax.plot(0.978089, 0.0113694, 0.0105418,color='magenta',marker='d')
ax.plot(0.958839,0.0208443, 0.0203168,color='darkmagenta',marker='d')
ax.plot(0.87597, 0.0578669, 0.0661631,color='blue',marker='d')
ax.plot(0.6546, 0.127991, 0.217409,color='dodgerblue',marker='d')
ax.plot(0.5476, 0.139584, 0.312816,color='aqua',marker='d')
ax.plot(0.513114, 0.136757, 0.350129,color='orange',marker='d')
ax.plot(0.46654, 0.117104, 0.416356,color='green',marker='d')
ax.plot(0.459841, 0.105386, 0.434773,color='gold',marker='d')
#NH-LU,Pure-Muon

ax.plot(0.989954, 0.00531454, 0.00473161,color='red',marker='*')
ax.plot(0.981327, 0.00973541, 0.00893788,color='magenta',marker='*')
ax.plot(0.96485,0.0179266, 0.0172229,color='darkmagenta',marker='*')
ax.plot(0.893079, 0.0506816, 0.0562393,color='blue',marker='*')
ax.plot(0.69166, 0.119672, 0.188668,color='dodgerblue',marker='*')
ax.plot(0.584308, 0.138246, 0.277446,color='aqua',marker='*')
ax.plot(0.546165, 0.139559, 0.314276,color='orange',marker='*')
ax.plot(0.484623, 0.128922, 0.386455,color='green',marker='*')
ax.plot(0.46939, 0.119804, 0.410807,color='gold',marker='*')

##############################################################################
ax = fig.add_subplot(324, projection='ternary')

ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')

#IH-EU,Pure-Muon
ax.plot(0.99382, 0.000427844, 0.00575194,color='red',marker='D')
ax.plot(0.988481, 0.000900814, 0.0106182,color='magenta',marker='D')
ax.plot(0.978198,0.00200159, 0.0198002,color='darkmagenta',marker='D')
ax.plot(0.93196, 0.00931351, 0.0587261,color='blue',marker='D')
ax.plot(0.78412, 0.0543027, 0.161578,color='dodgerblue',marker='D')
ax.plot(0.684595, 0.103931, 0.211474,color='aqua',marker='D')
ax.plot(0.641376, 0.131194, 0.227429,color='orange',marker='D')
ax.plot(0.547665, 0.205052, 0.247283,color='green',marker='D')
ax.plot(0.509747, 0.241994, 0.248259,color='gold',marker='D')
#IH-LU,Pure-Muon

ax.plot(0.994742, 0.000354372, 0.00490325,color='red',marker='*')
ax.plot(0.990195, 0.00074071, 0.00906395,color='magenta',marker='*')
ax.plot(0.981426,0.00163171, 0.0169419,color='darkmagenta',marker='*')
ax.plot(0.941793, 0.00746799, 0.0507389,color='blue',marker='*')
ax.plot(0.812532, 0.04313, 0.144338,color='dodgerblue',marker='*')
ax.plot(0.722804, 0.0828399, 0.194356,color='aqua',marker='*')
ax.plot(0.682969, 0.104889, 0.212142,color='orange',marker='*')
ax.plot(0.594259, 0.165554, 0.240187,color='green',marker='*')
ax.plot(0.557222, 0.196455, 0.246322,color='gold',marker='*')
plt.savefig("Ternary-PureMuon.png",dpi=150, transparent=True)

##########################Pion Decay#########################################
ax = fig.add_subplot(325, projection='ternary')

ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')
#NH-EU,Pion Decay
ax.plot(0.779474, 0.000635804, 0.219891,color='red',marker='d')
ax.plot(0.772267, 0.00115545, 0.226578,color='magenta',marker='d')
ax.plot(0.76256,0.00213249, 0.235307,color='darkmagenta',marker='d')
ax.plot(0.738739, 0.00669417, 0.254567,color='blue',marker='d')
ax.plot(0.709785, 0.0290278, 0.261187,color='dodgerblue',marker='d')
ax.plot(0.697915, 0.0549346, 0.247151,color='aqua',marker='d')
ax.plot(0.691724, 0.0699694, 0.238307,color='orange',marker='d')
ax.plot(0.671798, 0.112944, 0.215258,color='green',marker='d')
ax.plot(0.659551, 0.135408, 0.205041,color='gold',marker='d')
#NH-LU,Pion Decay

ax.plot(0.781031, 0.000544245, 0.218425,color='red',marker='*')
ax.plot(0.77433, 0.000990134, 0.22468,color='magenta',marker='*')
ax.plot(0.765242,0.00182728, 0.232931,color='darkmagenta',marker='*')
ax.plot(0.742452, 0.00567136, 0.251876,color='blue',marker='*')
ax.plot(0.713409, 0.0234724, 0.263118,color='dodgerblue',marker='*')
ax.plot(0.702615, 0.0436795, 0.253706,color='aqua',marker='*')
ax.plot(0.697702, 0.0554538, 0.246844,color='orange',marker='*')
ax.plot(0.683147, 0.0895964, 0.227256,color='green',marker='*')
ax.plot(0.674417, 0.107799, 0.217785,color='gold',marker='*')
######################################################################
ax = fig.add_subplot(326, projection='ternary')

ax.grid()
ax.set_tlabel('Nμ', size=24)
ax.set_llabel('Nτ', size=24)
ax.set_rlabel('Ne', size=24)

ax.taxis.set_label_position('tick1')
ax.laxis.set_label_position('tick1')
ax.raxis.set_label_position('tick1')
#IH-EU,Pion Decay
ax.plot(0.791967, 0.00231448, 0.205719,color='red',marker='D')
ax.plot(0.788703, 0.00434355, 0.206954,color='magenta',marker='D')
ax.plot(0.783877,0.00830118, 0.207822,color='darkmagenta',marker='D')
ax.plot(0.769131, 0.0266582, 0.20421,color='blue',marker='D')
ax.plot(0.7388, 0.0897525, 0.171448,color='dodgerblue',marker='D')
ax.plot(0.721256, 0.135779, 0.142965,color='aqua',marker='D')
ax.plot(0.713263, 0.156783, 0.129954,color='orange',marker='D')
ax.plot(0.69328, 0.205009, 0.101711,color='green',marker='D')
ax.plot(0.683366, 0.22586, 0.0907741,color='gold',marker='D')
#IH-LU,Pion Decay

ax.plot(0.79264, 0.00196629, 0.205394,color='red',marker='*')
ax.plot(0.789663, 0.0036898, 0.206647,color='magenta',marker='*')
ax.plot(0.785264,0.00705255, 0.207684,color='darkmagenta',marker='*')
ax.plot(0.771791, 0.0226894, 0.20552,color='blue',marker='*')
ax.plot(0.743914, 0.0771504, 0.178936,color='dodgerblue',marker='*')
ax.plot(0.728034, 0.117746, 0.15422,color='aqua',marker='*')
ax.plot(0.720964, 0.136557, 0.14248,color='orange',marker='*')
ax.plot(0.703822, 0.180518, 0.115661,color='green',marker='*')
ax.plot(0.695568, 0.199892, 0.10454,color='gold',marker='*')
plt.savefig("Ternary-PionDecay.png",dpi=150, transparent=True)

plt.savefig("output.pdf",dpi=150)
plt.show()

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
ax.plot(0.00108915, 0.00520295, 0.993708,color='red',marker='d')
ax.plot(0.00320356, 0.00853603, 0.98826,color='magenta',marker='d')
ax.plot(0.00774452,0.0145159, 0.97774,color='darkmagenta',marker='d')
ax.plot(0.0305369, 0.0395298, 0.929933,color='blue',marker='d')
ax.plot(0.111806, 0.117242, 0.770952,color='dodgerblue',marker='d')
ax.plot(0.171193, 0.171168, 0.657638,color='aqua',marker='d')
ax.plot(0.198134, 0.195348, 0.606517,color='orange',marker='d')
ax.plot(0.259163, 0.249946, 0.490891,color='green',marker='d')
ax.plot(0.284956, 0.27309, 0.441954,color='gold',marker='d')
#NH-LU,Pure-Electron

ax.plot(0.000236589, 0.000372685, 0.999391,color='red',marker='*')
ax.plot(0.000443868, 0.000693069, 0.998863,color='magenta',marker='*')
ax.plot(0.000845207, 0.00131127, 0.997844,color='darkmagenta',marker='*')
ax.plot(0.0026799, 0.00411715, 0.993203,color='blue',marker='*')
ax.plot(0.00894234, 0.0133918, 0.977666,color='dodgerblue',marker='*')
ax.plot(0.0136144, 0.0199151, 0.96647,color='aqua',marker='*')
ax.plot(0.0157981, 0.0228241, 0.961378,color='orange',marker='*')
ax.plot(0.0209687, 0.0292975, 0.949734,color='green',marker='*')
ax.plot(0.0232819, 0.0319792, 0.944739,color='gold',marker='*')

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
ax.plot(0.00328508, 0.0026874, 0.994028,color='red',marker='d')
ax.plot(0.00612958, 0.00501438, 0.988856,color='magenta',marker='d')
ax.plot(0.0116242, 0.00950934, 0.978866,color='darkmagenta',marker='d')
ax.plot(0.0366092, 0.0299486, 0.933442,color='blue',marker='d')
ax.plot(0.119925, 0.0981065, 0.781968,color='dodgerblue',marker='d')
ax.plot(0.179565, 0.146895, 0.67354,color='aqua',marker='d')
ax.plot(0.206555, 0.168975, 0.624469,color='orange',marker='d')
ax.plot(0.267848, 0.219116, 0.513037,color='green',marker='d')
ax.plot(0.293914, 0.24044, 0.465647,color='gold',marker='d')
#IH-LU,Pure-Electron

ax.plot(0.000517111, 0.000261883, 0.999221,color='red',marker='*')
ax.plot(0.000965723, 0.000487075, 0.998547,color='magenta',marker='*')
ax.plot(0.0018293, 0.000923171, 0.997248,color='darkmagenta',marker='*')
ax.plot(0.00570079, 0.00292909, 0.99137,color='blue',marker='*')
ax.plot(0.0179264, 0.00987953, 0.972194,color='dodgerblue',marker='*')
ax.plot(0.0259532, 0.0151081, 0.958939,color='aqua',marker='*')
ax.plot(0.0293529, 0.0175514, 0.953096,color='orange',marker='*')
ax.plot(0.0364206, 0.0233066, 0.940273,color='green',marker='*')
ax.plot(0.0390964, 0.025856, 0.935048,color='gold',marker='*')
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
ax.plot(0.992115, 0.0021603, 0.00572438,color='red',marker='d')
ax.plot(0.985291, 0.00520174, 0.00950679,color='magenta',marker='d')
ax.plot(0.972119, 0.0115321, 0.0163489,color='darkmagenta',marker='d')
ax.plot(0.912374, 0.0424406, 0.0451851,color='blue',marker='d')
ax.plot(0.715143, 0.150534, 0.134323,color='dodgerblue',marker='d')
ax.plot(0.576187, 0.228918, 0.194895,color='aqua',marker='d')
ax.plot(0.514038, 0.264411, 0.221551,color='orange',marker='d')
ax.plot(0.375015, 0.344802, 0.280183,color='green',marker='d')
ax.plot(0.316972, 0.378834, 0.304194,color='gold',marker='d')
#NH-LU,Pure-Muon

ax.plot(0.993406, 0.0063451, 0.000249187,color='red',marker='*')
ax.plot(0.987694, 0.0118427, 0.000463247,color='magenta',marker='*')
ax.plot(0.976657, 0.0224657, 0.000877686,color='darkmagenta',marker='*')
ax.plot(0.926389, 0.0708258, 0.00278487,color='blue',marker='*')
ax.plot(0.757727, 0.232841, 0.00943227,color='dodgerblue',marker='*')
ax.plot(0.635807, 0.349696, 0.014497,color='aqua',marker='*')
ax.plot(0.580224, 0.402886, 0.0168898,color='orange',marker='*')
ax.plot(0.452808, 0.524579, 0.0226131,color='green',marker='*')
ax.plot(0.397992, 0.57681, 0.0251978,color='gold',marker='*')

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
ax.plot(0.993271, 0.00344401, 0.00328508,color='red',marker='D')
ax.plot(0.987444, 0.00642613, 0.00612958,color='magenta',marker='D')
ax.plot(0.976189, 0.0121866, 0.0116242,color='darkmagenta',marker='D')
ax.plot(0.925011, 0.0383803, 0.0366092,color='blue',marker='D')
ax.plot(0.754347, 0.125727, 0.119925,color='dodgerblue',marker='D')
ax.plot(0.632183, 0.188252, 0.179565,color='aqua',marker='D')
ax.plot(0.576896, 0.216549, 0.206555,color='orange',marker='D')
ax.plot(0.451346, 0.280806, 0.267848,color='green',marker='D')
ax.plot(0.397953, 0.308133, 0.293914,color='gold',marker='D')
#IH-LU,Pure-Muon

ax.plot(0.990694, 0.00877559, 0.000530306,color='red',marker='*')
ax.plot(0.982648, 0.0163657, 0.000986627,color='magenta',marker='*')
ax.plot(0.967135, 0.0309994, 0.00186576,color='darkmagenta',marker='*')
ax.plot(0.897112, 0.0970601, 0.00582771,color='blue',marker='*')
ax.plot(0.670373, 0.311088, 0.0185391,color='dodgerblue',marker='*')
ax.plot(0.515625, 0.457327, 0.0270487,color='aqua',marker='*')
ax.plot(0.448105, 0.521196, 0.0306991,color='orange',marker='*')
ax.plot(0.301987, 0.659605, 0.0384086,color='green',marker='*')
ax.plot(0.243556, 0.715057, 0.0413878,color='gold',marker='*')
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
ax.plot(0.791221, 0.00572428, 0.203054,color='red',marker='d')
ax.plot(0.784802, 0.0110103, 0.204187,color='magenta',marker='d')
ax.plot(0.772874, 0.021342, 0.205784,color='darkmagenta',marker='d')
ax.plot(0.72101, 0.0687745, 0.210216,color='blue',marker='d')
ax.plot(0.556471, 0.226379, 0.21715,color='dodgerblue',marker='d')
ax.plot(0.443568, 0.337202, 0.21923,color='aqua',marker='d')
ax.plot(0.39379, 0.386585, 0.219625,color='orange',marker='d')
ax.plot(0.284294, 0.49638, 0.219326,color='green',marker='d')
ax.plot(0.239502, 0.541825, 0.218672,color='gold',marker='d')
#NH-LU,Pion Decay

ax.plot(0.793041, 0.00394193, 0.203017,color='red',marker='*')
ax.plot(0.787921, 0.0073573, 0.204722,color='magenta',marker='*')
ax.plot(0.778378, 0.0139587, 0.207663,color='darkmagenta',marker='*')
ax.plot(0.736574, 0.0440435, 0.219382,color='blue',marker='*')
ax.plot(0.600516, 0.145266, 0.254218,color='dodgerblue',marker='*')
ax.plot(0.503351, 0.218758, 0.277892,color='aqua',marker='*')
ax.plot(0.459202, 0.252373, 0.288425,color='orange',marker='*')
ax.plot(0.358207, 0.329754, 0.312039,color='green',marker='*')
ax.plot(0.314813, 0.363214, 0.321973,color='gold',marker='*')
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
ax.plot(0.794942, 0.00572633, 0.199331,color='red',marker='D')
ax.plot(0.790281, 0.0106847, 0.199034,color='magenta',marker='D')
ax.plot(0.781168, 0.0202626, 0.19857,color='darkmagenta',marker='D')
ax.plot(0.739207, 0.0638146, 0.196978,color='blue',marker='D')
ax.plot(0.597885, 0.209046, 0.193069,color='dodgerblue',marker='D')
ax.plot(0.49625, 0.313005, 0.190745,color='aqua',marker='D')
ax.plot(0.45017, 0.360053, 0.189776,color='orange',marker='D')
ax.plot(0.34536, 0.466894, 0.187747,color='green',marker='D')
ax.plot(0.300713, 0.51233, 0.186956,color='gold',marker='D')
#IH-LU,Pion Decay

ax.plot(0.794422, 0.00589379, 0.199684,color='red',marker='*')
ax.plot(0.788572, 0.0109897, 0.200438,color='magenta',marker='*')
ax.plot(0.776894, 0.0208123, 0.202293,color='darkmagenta',marker='*')
ax.plot(0.722308, 0.0651147, 0.212577,color='blue',marker='*')
ax.plot(0.54087, 0.208121, 0.251009,color='dodgerblue',marker='*')
ax.plot(0.415734, 0.305222, 0.279044,color='aqua',marker='*')
ax.plot(0.360971, 0.347419, 0.29161,color='orange',marker='*')
ax.plot(0.242237, 0.438241, 0.319522,color='green',marker='*')
ax.plot(0.1947, 0.474296, 0.331004,color='gold',marker='*')
plt.savefig("Ternary-PionDecay.png",dpi=150, transparent=True)

plt.savefig("output.pdf",dpi=150)
plt.show()

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = 'C:/Windows/Fonts/malgun.ttf'

if platform.system() == 'Darwin':
    print('Hangul OK in your Mac!')
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    print('Hangul OK in your Windows!')
    rc('font', family=font_name)
else:
    print('Unknown system')

plt.rcParams['axes.unicode_minus'] = False
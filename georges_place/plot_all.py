import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plt.rcParams.update({'font.size': 30})

pdfdir = './figs/'
l_save = True   # if False show graphs in the screen

files = ['Li_allFiles.csv', 'Mg_allFiles.csv']
outnames = ['Li_distrof_', 'Mg_distrof_']
titles = ['Li Batteries', 'Mg Batteries']


for ifl, fl in enumerate(files):
    d= pd.read_csv(fl, sep=',')
    HEADERS = list(d.head())
    for h in HEADERS:
        data = list(d[h])
        l_numbers = all(isinstance(item, float) for item in data)
        # make graphs for the following cases
        proceed = l_numbers  # you have numerical values
        proceed = proceed and not '_vol' in h   # not chemical elements
        proceed = proceed and not '_Vol' in h   # not chemical elements
        if proceed:
            # for charge use 'green' and discharge use 'red'
            # Maybe it is wrong the way I separate them.
            # If it is wrong use one color for everything for simplicity.
            if '_dis' in h or '_Dis' in h:
                color = 'red'
            else:
                color = 'green'
            sns.distplot(data, hist=True, kde=False, bins=10, color = color, hist_kws={'edgecolor':'black'})
            plt.title(titles[ifl], fontsize=18)
            plt.xlabel(h, fontsize=40)
            plt.ylabel('# of appearances', fontsize=30)
            if l_save:
                print('HERE', h)
                # I replaced '/' with '_' otherwise I cannot save them in files in linux
                h1 = h.replace('/','_')
                fpdf = outnames[ifl] + h1 + '.png'
                plt.savefig(pdfdir + fpdf,bbox_inches='tight', pad_inches=0.1)
                plt.gcf().clear(); plt.gca().clear(); plt.close();
            else:
                plt.show()

            print ('fpdf= ', fpdf)
        else:
            print (h, 'is not plotted')

###############################################################################
# Some standard modules
import os
import sys
import copy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import squarify
###############################################################################
whtext = " Kernwaffen\n"
gbforces = "für boden-gestützte\nRaketensysteme"

russiadf = pd.read_excel("russia-notebook.xlsx") # Data from Kristensen/Korda 2022, Bulletin of the Atomic Scientists
russiadf['strNumber'] = russiadf['Number'].astype(str)
russiadf['exLabel'] = russiadf['strNumber'] + whtext + russiadf['Type']
russiadf.loc[russiadf['Number'] == 90, 'exLabel'] = 90

for i in range(12):
    
    plt.figure(figsize=(8, 4))
    squarify.plot(sizes=russiadf['Number'],
                  #              label=russiadf['Type'],
                  label=russiadf['exLabel'],
                  color=russiadf['Color-{:02d}'.format(i)],
                  pad = True,
                  text_kwargs={'fontname': 'Fira Sans Condensed', 'fontsize': 12, 'color': 'white'})
    plt.text(70, 100, gbforces,
             fontname='Fira Sans Condensed', fontsize = 12,
             ha = 'center', va = 'baseline')
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("{:02d}.svg".format(i), transparent=True)
    plt.savefig("{:02d}.pdf".format(i), transparent=True)
    #plt.show()
    plt.clf()


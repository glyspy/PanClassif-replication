def mtrain(names, homepath):
    import numpy as np
    import pandas as pd
    import warnings
    warnings.filterwarnings("ignore")

    # Reading data and doing work
    cresult = pd.DataFrame()
    nresult = pd.DataFrame()
    for index in range(len(names)):
        Cancer = pd.read_csv(homepath + "/train_data/cancer/" + names[index] + ".txt.bz2", header=None, delimiter="\t")
        Normal = pd.read_csv(homepath + "/train_data/normal/" + names[index] + ".txt.bz2", header=None, delimiter="\t")
        
        Cancer = Cancer.T
        Normal = Normal.T

        Cancer['target'] = names[index]
        Normal['target'] = "normal"

        cresult = pd.concat([Cancer, cresult])
        nresult = pd.concat([Normal, nresult])
        
    # Merging all the cancer and normal data together and saving them
    cresult.to_csv(homepath + '/train_data/mul_Cancer.txt.bz2', compression="bz2", sep='\t', header=None, index=None, index_label=None) # type: ignore
    nresult.to_csv(homepath + '/train_data/mul_Normal.txt.bz2', compression="bz2", sep='\t', header=None, index=None, index_label=None) # type: ignore


def mtest(names, homepath):
    import warnings
    warnings.filterwarnings("ignore")
    import numpy as np
    import pandas as pd

    # Reading data and doing work
    cresult = pd.DataFrame()
    nresult = pd.DataFrame()
    for index in range(len(names)):
        Cancer = pd.read_csv(homepath + "/test_data/cancer/" + names[index] + ".txt.bz2", header=None, delimiter="\t")
        Normal = pd.read_csv(homepath + "/test_data/normal/" + names[index] + ".txt.bz2", header=None, delimiter="\t")
        
        Cancer = Cancer.T
        Normal = Normal.T

        Cancer['target'] = names[index]
        Normal['target'] = "normal"

        cresult = pd.concat([Cancer, cresult])
        nresult = pd.concat([Normal, nresult])
        
    # Merging all the cancer and normal data together and saving them
    cresult.to_csv(homepath + '/test_data/mul_Cancer.txt.bz2', compression="bz2", sep='\t', header=None, index=None, index_label=None) # type: ignore
    nresult.to_csv(homepath + '/test_data/mul_Normal.txt.bz2', compression="bz2", sep='\t', header=None, index=None, index_label=None) # type: ignore

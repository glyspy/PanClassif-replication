# PanClassif-replication

This is a repository for the replication project of [PanClassif](https://www.sciencedirect.com/science/article/pii/S0888754322000015).
The original GitHub repository of this package can be found in this link: (https://github.com/Zwei-inc/panclassif).

The data used in this project could not be added in this repository due to size. However, they can be found on this [Google Drive folder](https://drive.google.com/drive/folders/1MtnOmECZvEVSH9bFvYWkqrc7lJEIUKeQ?usp=sharing).
The analysis was completed for two cancer groups "rare", "common", that exist as folders in the link above.
Each folder of these groups contains a folder for normal samples, cancer samples, magic smoothed data, and knn smoothed data.
The notebooks in order to run and be able to load the data, have been created with relative paths, so the only required task for a full replication is to have each folder - "rare" and "common" - located in the home directory of this repository, if cloned.

### Contents
* panclassif folder, containing all the necessary Python functions for the pipeline execution.
* MAGIC_smoothing.ipynb, code for the generation of MAGIC smoothed data
* panclassif_replication.ipynb, replication of the panclassif pipeline with default parameters
* panclassif_analysis_knn.ipynb, extended work with added hyperparameter tuning for Random Forrest using k-NN smoothed data (Case I)
* panclassif_analysis_magic.ipynb, extended work with added hyperparamer tuning for Random Forrest using MAGIC smoothed data (Case II)

#### Disclaimer
Initially the official PanClassif repository was forked, and extended work and bug fixes were committed from the beginning of this project through a [branch](https://github.com/glyspy/PanClassif-Replication-Project/tree/replication-modification-branch).
However, due to unresolved technical issues, the final updates could not be pushed there, so this new repository was created.

TAG=2022Test

# Produce slimmed trees
conda activate py37
python3 slim.py >& output/$TAG/logs/slim.log
conda deactivate

# Produce fits and plots
conda activate root6
python3 fit.py >& output/$TAG/logs/fit.log
conda deactivate

# Produce summary tables 
conda activate root6
python3 summary.py >& output/$TAG/logs/summary.log
conda deactivate

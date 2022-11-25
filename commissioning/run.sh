conda deactivate

# Produce slimmed trees
conda activate py37
python3 slim.py >& output/logs/slim.log
conda deactivate

# Produce fits and plots
conda activate root6
python3 fit.py >& output/logs/fit.log
conda deactivate

# Produce summary tables 
conda activate root6
python3 summary.py >& output/logs/summary.log
conda deactivate

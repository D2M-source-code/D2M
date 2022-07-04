# for baseline evaluation, change model_num into Dreamer

import os
task = 'dmc_humanoid_walk'
model = 'D2M_Dreamer'
if not os.path.exists('log_files/' + task + '/' + model + '/'):
    os.makedirs('log_files/' + task + '/' + model + '/')
i = 0
for gpu_id in range(5):
    for per_gpu in range(1):
        comand = 'nohup python -u dreamer.py --logdir ./logdir/{task}/{model}/{i} --task {task} --gpu_id {gpu_id} ' \
                 '--model_num {model} --steps 5100000 --separate_schema D2M > ./log_files/{task}/{model}/{i}.log 2>&1 ' \
                 '&'.format(model=model, task=task, i=i, gpu_id=gpu_id)
        os.system(comand)
        i = i + 1

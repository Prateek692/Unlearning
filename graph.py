import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# with open('optdigits.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
# with open('optdigits.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# robustlogit = pd.DataFrame(data)
# # Errors for both method
# errors_mart_optdigits=mart[2].to_numpy().astype(int)
# errors_robustlogit_optdigits=robustlogit[2].to_numpy().astype(int)
# x_values = np.arange(1, len(errors_mart_optdigits) + 1)
# # Plot the graph
# plt.plot(x_values, errors_mart_optdigits,  linestyle='-', color='b', label='MART')
# plt.plot(x_values, errors_robustlogit_optdigits, linestyle='-', color='r', label='Robust LogitBoost')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('Optdigits Dataset')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_optdigits.png') 
# plt.close()




# with open('comp_cpu.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
# with open('comp_cpu.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# robustlogit = pd.DataFrame(data)
# # Errors for both method
# errors_mart_comp_cpu=mart[2].to_numpy().astype(int)
# errors_robustlogit_comp_cpu=robustlogit[2].to_numpy().astype(int)
# x_values = np.arange(1, len(errors_mart_comp_cpu) + 1)
# # Plot the graph
# plt.plot(x_values, errors_mart_comp_cpu,  linestyle='-', color='b', label='MART')
# plt.plot(x_values, errors_robustlogit_comp_cpu, linestyle='-', color='r', label='Robust LogitBoost')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('Comp_CPU Dataset')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_compcpu.png') 
# plt.close()

# with open('covtype.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
# with open('covtype.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# robustlogit = pd.DataFrame(data)
# # Errors for both method
# errors_mart_covtype=mart[2].to_numpy().astype(int)
# errors_robustlogit_covtype=robustlogit[2].to_numpy().astype(int)
# x_values = np.arange(1, len(errors_mart_covtype) + 1)
# # Plot the graph
# plt.plot(x_values, errors_mart_covtype,  linestyle='-', color='b', label='MART')
# plt.plot(x_values, errors_robustlogit_covtype, linestyle='-', color='r', label='Robust LogitBoost')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('Covtype Dataset')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_covtype.png') 
# plt.close()

# with open('ijcnn1.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
# with open('ijcnn1.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# robustlogit = pd.DataFrame(data)
# # Errors for both method
# errors_mart_ijcnn=mart[2].to_numpy().astype(int)
# errors_robustlogit_ijcnn=robustlogit[2].to_numpy().astype(int)
# x_values = np.arange(1, len(errors_mart_ijcnn) + 1)
# # Plot the graph
# plt.plot(x_values, errors_mart_ijcnn,  linestyle='-', color='b', label='MART')
# plt.plot(x_values, errors_robustlogit_ijcnn, linestyle='-', color='r', label='Robust LogitBoost')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('IJCNN1 Dataset')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_ijcnn1.png') 
# plt.close()





# with open('pendigits.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
# with open('pendigits.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# robustlogit = pd.DataFrame(data)
# # Errors for both method
# errors_mart_pendigits=mart[2].to_numpy().astype(int)
# errors_robustlogit_pendigits=robustlogit[2].to_numpy().astype(int)
# x_values = np.arange(1, len(errors_mart_pendigits) + 1)
# # Plot the graph
# plt.plot(x_values, errors_mart_pendigits,  linestyle='-', color='b', label='MART')
# plt.plot(x_values, errors_robustlogit_pendigits, linestyle='-', color='r', label='Robust LogitBoost')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('Pendigits Dataset')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_pendigits.png') 
# plt.close()


# with open('coffee_bean.test.csv_mart_J20_v0.1.testlog', 'r') as file:
#     lines = file.readlines()
# data = [re.split(r'\s+', line.strip()) for line in lines]
# mart = pd.DataFrame(data)
with open('intel_image.test.csv_robustlogit_J20_v0.1.testlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
robustlogit = pd.DataFrame(data)
with open('intel_image.test.csv_robustlogit_J20_v0.1.unlearnlog', 'r') as file:
    lines = file.readlines()
data = [re.split(r'\s+', line.strip()) for line in lines]
robustlogit_unlearn = pd.DataFrame(data)
test_data = pd.read_csv('./data/intel_image.test.csv')
# Errors for both method

# errors_mart_coffee=mart[2].to_numpy().astype(int)
errors_robustlogit_coffee=robustlogit[2].to_numpy().astype(int) / len(test_data.index) * 100
errors_robustlogit_coffee_ul=robustlogit_unlearn[2].to_numpy().astype(int) / len(test_data.index) * 100
x_values = np.arange(1, len(errors_robustlogit_coffee) + 1)
# Plot the graph
# plt.plot(x_values, errors_mart_coffee,  linestyle='-', color='b', label='MART')
plt.plot(x_values, errors_robustlogit_coffee - errors_robustlogit_coffee_ul, linestyle='dashed', color='r', label='MART Original')
# plt.plot(x_values, errors_robustlogit_coffee_ul, linestyle='dotted', color='b', label='MART Unlearned')
# Add labels and title
plt.xlabel('Iterations')
plt.ylabel('Errors(in %)')
plt.title('Intel Image Dataset')
# Add legend
plt.legend()
# Show the plot
plt.savefig('graph_intelw.png') 
plt.close()





# #MART
# plt.plot(x_values, errors_mart_pendigits,  linestyle='-', color='b', label='Pendigits')
# # plt.plot(x_values, errors_mart_comp_cpu, linestyle='-', color='r', label='Comp_CPU')
# plt.plot(x_values, errors_mart_covtype,  linestyle='-', color='g', label='Covtype')
# plt.plot(x_values, errors_mart_optdigits, linestyle='-', color='y', label='Optdigits')
# plt.plot(x_values, errors_mart_ijcnn,  linestyle='-', color='m', label='IJCNN')
# plt.plot(x_values, errors_mart_coffee,  linestyle='-', color='r', label='Coffee Bean')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('MART Across different Datasets')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_mart.png') 
# plt.close()

# #ROBUST
# plt.plot(x_values, errors_robustlogit_pendigits,  linestyle='-', color='b', label='Pendigits')
# # plt.plot(x_values, errors_robustlogit_comp_cpu, linestyle='-', color='r', label='Comp_CPU')
# plt.plot(x_values, errors_robustlogit_covtype,  linestyle='-', color='g', label='Covtype')
# plt.plot(x_values, errors_robustlogit_optdigits, linestyle='-', color='y', label='Optdigits')
# plt.plot(x_values, errors_robustlogit_ijcnn,  linestyle='-', color='m', label='IJCNN')
# plt.plot(x_values, errors_robustlogit_coffee, linestyle='-', color='r', label='Coffee Bean')
# # Add labels and title
# plt.xlabel('Iterations')
# plt.ylabel('Errors')
# plt.title('Robust LogitBoost Across different Datasets')
# # Add legend
# plt.legend()
# # Show the plot
# plt.savefig('graph_robustlogit.png') 
# plt.close()

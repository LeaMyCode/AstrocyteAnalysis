# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 08:52:10 2025

@author: leaga
"""

from tkinter import filedialog
import pandas as pd
import os



#########################
#
# Please decode your conditions (if you have it coded, otherwise leave this empty)
#
#########################
global replacements
replacements = {
    'A1_' : 'Male_ctrl_24h_+MG_A_', 
    'A2' : 'Male_H7N7_24h_+MG_A_',
    'A3' : 'Male_ctrl_24h_-MG_A_',
    'A4' : 'Female_ctrl_24h_-MG_A_',
    'A5' : 'Female_ctrl_24h_+MG_A_',
    'A6' : 'Female_H7N7_24h_+MG_A_',
    'A7' : 'Male_ctrl_6h_-MG_A_',
    'A8' : 'Female_ctrl_6h_-MG_A_',
    'A9' : 'Female_ctrl_6h_+MG_A_',
    'A10' : 'Female_H7N7_6h_+MG_A_',
    'A11' : 'Male_H7N7_24h_-MG_A_',
    'A12' : 'Male_ctrl_6h_+MG_A_',
    'A13' : 'Male_H7N7_6h_+MG_A_',
    'A14' : 'Male_H7N7_6h_-MG_A_',
    'A15' : 'Female_H7N7_6h_-MG_A_',
    'A16' : 'Female_H7N7_24h_-MG_A_',
    
    'B1_' : 'Male_H7N7_6h_-MG_B_',
    'B2' : 'Male_ctrl_24h_-MG_B_',
    'B3' : 'Female_ctrl_24h_-MG_B_',
    'B4' : 'Male_H7N7_6h_+MG_B_',
    'B5' : 'Female_H7N7_24h_-MG_B_',
    'B6' : 'Female_H7N7_24h_+MG_B_',
    'B7' : 'Male_H7N7_24h_+MG_B_',
    'B8' : 'Female_ctrl_6h_-MG_B_',
    'B9' : 'Male_ctrl_24h_+MG_B_',
    'B10' : 'Female_H7N7_6h_-MG_B_',
    'B11' : 'Female_H7N7_6h_+MG_B_',
    'B12' : 'Male_ctrl_6h_+MG_B_',
    'B13' : 'Male_H7N7_24h_-MG_B_',
    'B14' : 'Female_ctrl_24h_+MG_B_',
    'B15' : 'Female_ctrl_6h_+MG_B_',
    'B16' : 'Male_ctrl_6h_-MG_B_',
    
    
    'C1_' : 'Male_ctrl_6h_+MG_C_',
    'C2' : 'Male_ctrl_6h_-MG_C_',
    'C3' : 'Female_H7N7_24h_+MG_C_',
    'C4' : 'Female_H7N7_24h_-MG_C_',
    'C5' : 'Female_ctrl_6h_+MG_C_',
    'C6' : 'Female_ctrl_6h_-MG_C_',
    'C7' : 'Male_ctrl_24h_+MG_C_',
    'C8' : 'Male_ctrl_24h_-MG_C_',
    'C9' : 'Male_H7N7_6h_+MG_C_',
    'C10' : 'Male_H7N7_6h_-MG_C_',
    'C11' : 'Female_ctrl_24h_+MG_C_',
    'C12' : 'Female_ctrl_24h_-MG_C_',
    'C13' : 'Female_H7N7_6h_+MG_C_',
    'C14' : 'Female_H7N7_6h_-MG_C_',
    'C15' : 'Male_H7N7_24h_+MG_C_',
    'C16' : 'Male_H7N7_24h_-MG_C_'
}

def Decoder (value):
    for old, new in replacements.items():
        if old in value:
            value = value.replace(old, new)
            
    return value

data = {
        'file' : [],
        'GFAP_area' : [],
        'GFAP_mean_int' : [],
        'GLT-1_mean_int_inAstro' : [],
        'GLT-1_mean_int_whole' : []}

data_norm = {
        'file' : [],
        'GFAP_area' : [],
        'GFAP_mean_int' : [],
        'GLT-1_mean_int_inAstro' : [],
        'GLT-1_mean_int_whole' : []}


root_path = filedialog.askdirectory(title="Please select your folder with data")
results_path = os.path.join(root_path,"Analysis")
if not os.path.exists(results_path):
    os.makedirs(results_path)

for file in os.listdir(root_path):
    if file == "Analysis":
        continue  
    file_path = os.path.join(root_path, file)
    
    if file.endswith(".png") or file.endswith(".zip"):
        continue
    
    if file.endswith("-GFAP.csv"):
    
        file_header = (file.split("-"))[0]
        data['file'].append(Decoder(file_header))
        
        GFAP = pd.read_csv(os.path.join(root_path, file_header + "-GFAP.csv"), usecols=['Area', 'Mean'])
        data['GFAP_area'].append(GFAP['Area'].tolist()[0])
        data['GFAP_mean_int'].append(GFAP['Mean'].tolist()[0])
        
        GLT = pd.read_csv(os.path.join(root_path, file_header + "-GLT.csv"), usecols=['Area', 'Mean'])
        data['GLT-1_mean_int_inAstro'].append(GLT['Mean'].tolist()[0])
        
        GLT_whole = pd.read_csv(os.path.join(root_path, file_header + "-GLT_whole.csv"), usecols=['Area', 'Mean'])
        data['GLT-1_mean_int_whole'].append(GLT_whole['Mean'].tolist()[0])
        
    else:
        continue


df_data = pd.DataFrame(data)
df_data = df_data.sort_values(by='file', ascending=False)
df_data.to_csv(results_path + r'\hyperexcitability.csv', index=False, header=True)

#########################
#
# Normalization
#
#########################

df_data['Round'] = df_data['file'].str.extract(r'_([ABC])_')
df_data['Time'] = df_data['file'].str.extract(r'_([0-9]+h)_')


normalized_data = df_data.copy()

for round_letter in ['A', 'B', 'C']:
    for time_point in ['6h', '24h']:
        # Subset current group
        current_group = df_data[(df_data['Round'] == round_letter) & (df_data['Time'] == time_point)]

        # Calculate mean of Female_CTRL_XXh_+MG in that group
        ref_values = current_group[current_group['file'].str.contains('Female_ctrl') & current_group['file'].str.contains(r'\+MG')]
        
        if not ref_values.empty:
            ref_GFAP_area = ref_values['GFAP_area'].mean()
            ref_GFAP_mean_int = ref_values['GFAP_mean_int'].mean()
            ref_GLT1_inAstro = ref_values['GLT-1_mean_int_inAstro'].mean()
            ref_GLT1_whole = ref_values['GLT-1_mean_int_whole'].mean()

            # Normalize all rows in that round/time group
            mask = (normalized_data['Round'] == round_letter) & (normalized_data['Time'] == time_point)
            normalized_data.loc[mask, 'GFAP_area'] = normalized_data.loc[mask, 'GFAP_area'] / ref_GFAP_area
            normalized_data.loc[mask, 'GFAP_mean_int'] = normalized_data.loc[mask, 'GFAP_mean_int'] / ref_GFAP_mean_int
            normalized_data.loc[mask, 'GLT-1_mean_int_inAstro'] = normalized_data.loc[mask, 'GLT-1_mean_int_inAstro'] / ref_GLT1_inAstro
            normalized_data.loc[mask, 'GLT-1_mean_int_whole'] = normalized_data.loc[mask, 'GLT-1_mean_int_whole'] / ref_GLT1_whole


normalized_data.to_csv(os.path.join(results_path, 'hyperexcitability_normalized.csv'), index=False)

        
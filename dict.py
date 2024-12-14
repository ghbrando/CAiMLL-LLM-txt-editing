aggregated_acronyms_dict = {
    #Add your acronyms here
    "CNR": "?",
    "ASNRDA": "?",
    "T2": "?",
    "SOCOM": "?",
    "ONR": "?",
}

aggregated_errors_dict = {
    #Add your errors here
    
    #From file_0c538c99_5f0e_47a3_95ad_c9d56f12e8ee
    "Naval X": "NavalX",
    "Commander�s": "Commanders",
    "O&R": "ONR"

}

file_0c538c99_5f0e_47a3_95ad_c9d56f12e8ee = {
    "Navel X": "NavelX",
    "Commander�s": "Commanders",
    "O&R": "ONR"
}

file_0ab1a881_8dfc_44b3_88c5_f51a08f3f82d = {

}

file_0001e03f_6950_4c59_8007_8f99c3d5d4c3 = {

}
file_154ba492_58d0_4e70_9456_661907d4a916 = {
    "Port Wyoming": "Port Hueneme",
    "holography": "holographically"
}

file_1814117d_1d34_47de_837c_4f7249d42664 = {

}

def writeTo(dict, path):
    with open(path, 'w', encoding='utf-8') as file:
        for key, value in dict.items():
            file.write(f"{key} -> {value}\n")

''' 
 Use this function when you want to write out your dictionary to a file, the first parameter is the dictionary 
 you want to write out, the second parameter is the path to the file you want to write to

 writeTo(file_0c538c99_5f0e_47a3_95ad_c9d56f12e8ee, 'corrected.txt')
''' 

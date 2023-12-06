import os
import shutil
import re

path1 = './Movie_Poster_Metadata/groundtruth'
temp_path = './Movie_Poster_Metadata/temp_groundtruth'
path2 = './Movie_Poster_Metadata/updated_groundtruth'


def reconstruct_metadata():
    dir_list = os.listdir(path1)

    if not os.path.exists(temp_path):
        os.makedirs(temp_path)

    if not os.path.exists(path2):
        os.makedirs(path2)
    else: 
        print('directories already exists. not cleaning metadata')
        return None

    #adding comma between json objects from path1
    for file_name in dir_list:
        with open(path1+ '/' + file_name, 'r', encoding='utf-16-le') as file1:
            temp_file = open(temp_path + '/' + file_name, 'w', encoding='utf-8')
            for line in file1.readlines():
                #adding comma at the end of each poster metdata for ease of seperation
                line = line.replace('}\n','},\n') 
                #read all lines starting with """_id"
                y = re.findall('^ \'_id\'', line)
                if not y:
                    temp_file.write(line)
        file1.close()
        temp_file.close()

    dir_list = os.listdir(temp_path)

    # #create final json array from temp_file's json objects
    for file_name in dir_list:
        with open(temp_path + '/' + file_name, 'r',  encoding = 'utf-8') as temp_file:
            file2 = open(path2 + '/' + file_name, 'w', encoding = 'utf-8')
            lines = temp_file.readlines()
            lines = lines[1:-1] 
            # Remove "_id" field from each JSON object
            modified_lines = []
            for line in lines:
                # Check if the line contains "_id"
                if '"_id"' in line:
                # Remove the entire line (i.e., the "_id" field)
                    continue

                # Append the line if it doesn't contain "_id"
                modified_lines.append(line)
            file2.write('[{')
            file2.writelines(modified_lines)
            file2.write('}]')
        temp_file.close()
        file2.close()

    # for file_name in dir_list:
    #     with open(temp_path + '/' + file_name, 'r', encoding='utf-8') as temp_file:
    #         file2 = open(path2 + '/' + file_name, 'w', encoding='utf-8')

    #         # Read all lines from temp_file
    #         lines = temp_file.readlines()
    #         lines = lines[1:-1] 
    #         # Remove "_id" field from each JSON object
    #         modified_lines = []
    #         for line in lines:
    #             # Check if the line contains "_id" and skip it
    #             if '"_id"' in line:
    #                 continue

    #             # Remove any leading or trailing commas
    #             line = line.strip(',\n')
                
    #             modified_lines.append(line)

    #         # Write the modified lines to file2
    #         file2.write('[{')
    #         file2.writelines(modified_lines)
    #         file2.write('}]')
    shutil.rmtree(temp_path) #delete temporary file
    # print('okay got it')
    return None        
                 

reconstruct_metadata()
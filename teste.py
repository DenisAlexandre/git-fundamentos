import os
def search_path(job_name):  
  for subdir, dirs, files in os.walk(os.getcwd()):      
    for file in files:        
      if job_name in file:            
        print(file)            
        #print(os.path.join(subdir, file))            
        filepath = subdir + os.sep + file
            
        if filepath.endswith(".py"):                
          path_sql = filepath            
        if filepath.endswith(".sql"):                
          path_py = filepath
  
  return path_sql, path_py

job_name = "job1"
path_sql, path_py = search_path(job_name)
print(path_sql)
print(path_py)

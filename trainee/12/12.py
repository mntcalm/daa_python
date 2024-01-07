import os

def delete_files_func(path, file_extension):
  deleted_files = []
  for file in os.listdir(path):
    file_path = os.path.join(path, file)
    file_name, file_ext = os.path.splitext(file)
    if file_ext == file_extension:
      os.remove(file_path)
      deleted_files.append(file)
  return deleted_files

print(delete_files_func(path='/home/calltop/daa_python/trainee/12/test', file_extension='.txt'))

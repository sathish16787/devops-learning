with open('app.log','r') as log_file:
  line_list = log_file.readlines()


info_count = 0
error_count = 0
warning_count = 0

for line in line_list:
  clean_line = line.strip()
  if clean_line:
    status_msg = line.split()[0]
    if status_msg == "[ERROR]":
      error_count += 1
    elif status_msg == "[INFO]":
      info_count += 1
    elif status_msg == "[WARNING]":
      warning_count += 1

log_file.close()

print(f"INFO Count: {info_count}")
print(f"WARNING Count: {warning_count}")
print(f"ERROR Count: {error_count}")
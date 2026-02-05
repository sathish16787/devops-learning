import sys


def count_logs(file_name):
  counts = {
  "INFO" : 0,
  "ERROR" : 0,
  "WARNING" : 0,
  "DEBUG" : 0,
  "CRITICAL" : 0
  }

  with open(file_name,'r') as log_file:
    line_list = log_file.readlines()
    for line in line_list:
      clean_line = line.strip()
      if clean_line:
        status_msg = line.split()[0].strip('[]')
        if status_msg in counts:
          counts[status_msg] += 1
  return counts

def print_results(counts):
  print(f"INFO: {counts.get('INFO')}")
  print(f"WARNING: {counts.get('WARNING')}")
  print(f"ERROR: {counts.get('ERROR')}")
  print(f"CRITICAL: {counts.get('CRITICAL')}")
  print(f"DEBUG: {counts.get('DEBUG')}")

def main():
  default_log = 'app.log'
  if len(sys.argv) == 2:
    file_name = sys.argv[1]
  else: 
    file_name = default_log


  try:
    error_status_count = (count_logs(file_name))
    print_results(error_status_count)

  except FileNotFoundError:
    print(f"ERROR: File '{file_name}' not found")
    print("Please check if the file exists and try again.")

  except Exception as e:
     print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

    
  
  






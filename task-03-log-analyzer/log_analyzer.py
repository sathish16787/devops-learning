import json
import sys

def parse_log_files(file_name):
  total_log_line = 0
  log_level_counts = {}
  service_level_counts = {}

  with open(file_name) as log_file:
    # line_list = log_file.readlines()
    for line in log_file:
      clean_line = line.strip()
      if clean_line:
        total_log_line += 1
        log_level_msg = line.split()[2].strip('[]')
        service_msg = line.split()[3].strip('[]')

        if log_level_msg not in log_level_counts:
          log_level_counts[log_level_msg] = 1
        else:
          log_level_counts[log_level_msg] += 1

        if service_msg not in service_level_counts:
          service_level_counts[service_msg] = 1
        else:
          service_level_counts[service_msg] += 1

    unique_service = list(service_level_counts.keys())
    error_rate = log_level_counts.get("ERROR",0)
    if total_log_line > 0:
      error_rate_percentage = error_rate / total_log_line * 100
    else:
      error_rate_percentage = 0.0


      

  return {
    "total_logs":total_log_line,
    "log_levels":log_level_counts, 
    "services": service_level_counts,
    "unique_services": unique_service,
    "error_rate_percent":error_rate_percentage
    }


def main():
  default_log = 'app_detailed.log'
  default_output_log = 'log_counts.json'
  if len(sys.argv) == 3:
    file_name = sys.argv[1]
    output_log_file = sys.argv[2]
  elif len(sys.argv) == 2: 
    file_name = sys.argv[1]
    output_log_file = 'log_counts.json'
  else:
    file_name = default_log
    output_log_file = default_output_log

  try:
    data = parse_log_files(file_name)
  except FileNotFoundError:
    print(f"ERROR: File '{file_name}' not found")
    print("Please check if the file exists and try again.")
    return 1
  except Exception as e:
     print(f"Unexpected error: {e}")
     return 1
  
  print(f"Analysis complete!")
  print(f"Total logs processed: {data['total_logs']}")
  print(f"Error rate: {data['error_rate_percent']}")
  print(f"Results saved to: {output_log_file}")
  with open(output_log_file, "w") as json_file:
    json.dump(data, json_file,indent=2, sort_keys=False)

if __name__ == "__main__":
    main()



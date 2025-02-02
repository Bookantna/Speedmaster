import subprocess
import time
import csv

def ping_server(host, total_pings, interval_seconds, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Result'])  # Write the header

        for _ in range(total_pings):
            # Run ping command
            result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # Get the current timestamp
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            
            # Prepare the result
            if result.returncode == 0:
                result_text = f"Success: {result.stdout.decode().strip()}"
            else:
                result_text = f"Error: {result.stderr.decode().strip()}"
            
            # Write the result to the CSV file
            writer.writerow([timestamp, result_text])
            
            # Wait for the specified interval before the next ping
            time.sleep(interval_seconds)

if __name__ == "__main__":
    # Define the Cloudflare DNS server
    cloudflare_dns = '1.1.1.1'
    
    # Define the number of pings and interval in seconds
    num_pings = 60
    interval = 60  # Ping every 60 seconds
    
    # Define the output file name
    output_file = 'ping_results.csv'
    
    ping_server(cloudflare_dns, num_pings, interval, output_file)

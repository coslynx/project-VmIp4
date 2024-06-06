import sys
import time
import random
from datetime import datetime

def generate_report(attack_details, attack_results):
    report = "DDoS Attack Report\n\n"
    
    report += "Target: {}\n".format(attack_details['target'])
    report += "Attack Type: {}\n".format(attack_details['attack_type'])
    report += "Attack Duration: {} seconds\n".format(attack_details['duration'])
    report += "Attack Intensity: {} packets/s\n\n".format(attack_details['intensity'])
    
    report += "Attack Started at: {}\n".format(datetime.fromtimestamp(attack_details['start_time']).strftime('%Y-%m-%d %H:%M:%S'))
    report += "Attack Ended at: {}\n\n".format(datetime.fromtimestamp(attack_details['end_time']).strftime('%Y-%m-%d %H:%M:%S'))
    
    report += "Attack Results:\n"
    report += "Total Packets Sent: {}\n".format(attack_results['total_packets'])
    report += "Successful Packets: {}\n".format(attack_results['successful_packets'])
    report += "Failed Packets: {}\n".format(attack_results['failed_packets'])
    report += "Success Rate: {:.2f}%\n".format(attack_results['success_rate'] * 100)
    
    return report

def save_report(report):
    file_name = "ddos_attack_report_{}.txt".format(int(time.time()))
    with open(file_name, 'w') as file:
        file.write(report)
    return file_name

def generate_and_save_report(attack_details, attack_results):
    report = generate_report(attack_details, attack_results)
    file_name = save_report(report)
    return file_name

if __name__ == "__main__":
    attack_details = {
        'target': '127.0.0.1',
        'attack_type': 'UDP Flood',
        'duration': 60,
        'intensity': 1000,
        'start_time': time.time(),
        'end_time': time.time() + 60
    }
    
    attack_results = {
        'total_packets': 10000,
        'successful_packets': 9500,
        'failed_packets': 500,
        'success_rate': 0.95
    }
    
    report_file = generate_and_save_report(attack_details, attack_results)
    print("Report generated and saved as: {}".format(report_file))
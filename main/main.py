import tkinter as tk
from tkinter import messagebox
import nmap
 
 
class NetworkScannerGUI:
   def __init__(self, root):
       self.root = root
       self.root.title("Network Scanner - The Pycodes")
       self.root.geometry("600x400")
 
 
       self.ip_label = tk.Label(root, text="Enter Router IP:")
       self.ip_label.pack()
 
 
       self.ip_entry = tk.Entry(root, width=30, font="arial, 13")
       self.ip_entry.pack()
 
 
       self.scan_button = tk.Button(root, text="Scan Network", command=self.scan_network)
       self.scan_button.pack()
 
 
       self.result_label = tk.Label(root, text="", font="arial, 12")
       self.result_label.place(x=30,y=100)
 
 
   def scan_network(self):
       ip_address = self.ip_entry.get()
       if not ip_address:
           messagebox.showerror("Error", "Please enter the router's IP address.")
           return
 
 
       ip_range = ip_address + '/24'
 
 
       try:
           nm = nmap.PortScanner()
           nm.scan(hosts=ip_range, arguments='-sn')
           result_text = ""
           for host in nm.all_hosts():
               status = nm[host]['status']['state']
               hostnames = nm[host]['hostnames']
               device_names = ', '.join(hostname['name'] for hostname in hostnames) if hostnames else 'Unknown'
               result_text += f"Host: {host}\tStatus: {status}\tDevice Name: {device_names}\n"
           self.result_label.config(text=result_text)
       except nmap.PortScannerError as e:
           messagebox.showerror("Error", f"An error occurred while scanning: {e}")
 
 
if __name__ == "__main__":
   root = tk.Tk()
   app = NetworkScannerGUI(root)
   root.mainloop()

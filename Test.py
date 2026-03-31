import win32com.client

# Start LabVIEW
labview = win32com.client.Dispatch("LabVIEW.Application")

# Path to your VI file
vi_path = r"F:\Shankh_Academy\Labview Series\Temperature monitor\Panel Diagram.vi"

# Open VI
vi = labview.GetVIReference(vi_path)

# Show front panel
vi.FPWinOpen = True

print("VI Opened Successfully!")
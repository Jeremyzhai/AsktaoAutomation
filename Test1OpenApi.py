from virtualbox import VirtualBox, Session

vbox = VirtualBox()
session = Session()
machine = vbox.find_machine("Windows11")  ## for example: "ubuntu"

# Define authentication data with the username "zhai" without a password
session.username = "zhai"

# If you want to run it normally:
proc = machine.launch_vm_process(session, "gui", [])
proc.wait_for_completion(timeout=-1)

session = proc.create_session()
time.sleep(35)
gs = session.console.guest.create_session('zhai', '')
process, stdout, stderr = gs.execute('C:\\Windows\\System32\\cmd.exe', ['/C', 'tasklist'])
print stdout
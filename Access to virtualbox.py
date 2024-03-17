from virtualbox import VirtualBox, Session

vbox = VirtualBox()
session = Session()
machine = vbox.find_machine("Windows11")  ## for example: "ubuntu"
# If you want to run it normally:
proc = machine.launch_vm_process(session, "gui", [])
# If you want to run it in background:
# proc = machine.launch_vm_process(session, "headless")
proc.wait_for_completion(timeout=-1)
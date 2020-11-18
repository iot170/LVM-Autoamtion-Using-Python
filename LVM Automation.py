import os

def lvmcreate():
  lvminput = input("You want to create lvm y/n? :")
  if lvminput == 'y':
    os.system("fdisk -l") 
    print()
    pv = input("Enter your Disks name for creating PV:") 
        
    os.system("pvcreate {}".format(pv))
    os.system("pvdisplay {}".format(pv))
    print("=============================================================================")
    vgname = input("Enter VG Name:")
    os.system("vgcreate {} {}".format(vgname, pv)) 
    os.system("vgdisplay {}".format(vgname))
    print(vgname)
    print("=============================================================================")

    lvsize = input("Enter size of LV in {K,M,G}: ")
    lvname = input("Enter LV Name: ")
    os.system("lvcreate --size {} -n {} {} ".format(lvsize, lvname, vgname))
    os.system("lvdisplay")
    print("=============================================================================")

    path = input("Enter path of disk :")
    os.system("mkfs.ext4 {}".format(path))
    print("=============================================================================")

    dirname = input("Enter directory name: ")
    os.system("mkdir {}".format(dirname))
    os.system("mount {} {}".format(path, dirname))

  elif lvminput == 'n':
    print("Try Again!!")
  else:
    print("Select available optins")
print("================================================================================")

print(" \t\t\tWelcome to the LVM Automation")
print("\t\t\t-------------------------------")

while True:
  print("================================================================================")
  print("Press 1 to Create PV,VG,LV and mount with datanode directory")
  print("Press 2 to Display all PVS")
  print("Press 3 to Display all VGS")
  print("Press 4 to Display all LVS")
  print("Press 5 to Extend LV size")
  print("Press 6 to Reduce LV size")
  print("Press 0 to close \n")
  print("================================================================================")

  cmd = input("Enter your choice {0-6} :")
  if cmd == '1':
    lvmcreate()
    print("=============================================================================")

  elif cmd == '2':
    os.system("pvs")
    print("=============================================================================")

  elif cmd == '3':
    os.system("vgs")
    print("=============================================================================")

  elif cmd == '4':
    os.system("lvs")
    print("=============================================================================")

  elif cmd == '5':
    extendesize = input("Enter size how many you want to extend :")
    os.system("df -hT")
    path = input("Enter path of Disk :")
    os.system("lvextend --size +{} {}".format(extendesize, path))
  elif cmd == '0':
    break
  else:
    print("Sorry!!")
  
  

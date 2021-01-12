import subprocess
import re

def main():
    command_output= subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output= True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", str(command_output)))
    if len(profile_names) != 0 :
        for names in profile_names:
            check = subprocess.run(["netsh", "wlan", "show", "profiles", names], capture_output= True).stdout.decode()
            if re.search(" Security key           : Absent", str(check)):
                continue
            else:
                paswd = subprocess.run(["netsh", "wlan", "show", "profiles", names ,"key=clear"], capture_output= True).stdout.decode()
                get = re.search("Key Content            :(.*)\r", paswd)           
                if get == None:
                    print (f"profile {names} password None")
                else:    
                    profile = {
                        'ssid' : names,
                        'Password' : get[1],
                    }
                    print (profile)


if __name__ == "__main__":
    main()



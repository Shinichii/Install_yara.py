import os

os.system(“bootstrap.sh”)
os.system(“configure”)
os.system(“make”)
os.system(“make install”)
os.system(“make check”)
os.system(“echo Verification, vous devriez voir apparaitre sur votre ecran dummy my_first_rule”)
os.system(“echo ‘rule dummy { condition : true }’ > my_first_rule”)
os.system(“yara my_first_rule my_first_rule”)

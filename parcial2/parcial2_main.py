from parcial2_func import *

print(r""" 
 __  __                                            _              _   
 \ \/ /     _ __ ___   ___ _ __     _ __ ___  _   _| |_ __ _ _ __ | |_ 
  \  /_____| '_ ` _ \ / _ \ '_ \   | '_ ` _ \| | | | __/ _` | '_ \| __|
  /  \_____| | | | | |  __/ | | |  | | | | | | |_| | || (_| | | | | |_ 
 /_/\_\    |_| |_| |_|\___|_| |_|  |_| |_| |_|\__,_|\__\__,_|_| |_|\__|
                                                                      
       _               _                                              
   ___| |__   ___  ___| | _____ _ __                                  
  / __| '_ \ / _ \/ __| |/ / _ \ '__|                                 
 | (__| | | |  __/ (__|   <  __/ |                                    
  \___|_| |_|\___|\___|_|\_\___|_|               


  Bienvenido a Mutant Checker!
""")


output = is_mutant()
print()
if type(output) == bool:
	print(f'El resultado del mutant checker es "{output}"')
else:
	print(output)

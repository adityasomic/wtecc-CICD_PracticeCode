import sys,io,os
 
try:
    # Clean up any open project
    if projects.primary:
        projects.primary.close()
 
    # Define the file name for the project
    project_name = "Somic Template V19P4.project"
 
    # Define the path where the project is stored
    project_path =r"C:\Users\bhandwalkar\OneDrive - Somic Verwaltungs GmbH\Desktop\Codesys\RABBIT\Codesys_scripts"
    # Load the existing project
    proj = projects.open(os.path.join(project_path, project_name))
except Exception as exception:
    print("Error: " + str(exception))
    if not system.trace:
       print("Please turn on the 'Script Tracing' function to get detailed information about the script execution.")

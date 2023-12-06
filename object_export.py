import sys,io,os
 
# Specify the project file name
project_name = "Somic Template V19P4.project"
 
# Define the path where the project should be/is stored
project_path =r"C:\Users\bhandwalkar\OneDrive - Somic Verwaltungs GmbH\Desktop\Codesys\RABBIT\Codesys_scripts"
 
# Define the path where the exported objects should be stored
object_path = os.path.join(project_path, "Objects")
 
def collect_objects(project_reference):
    # List that stores all POU nodes
    project_objects = []
 
    # Collect all the leaf nodes.
    for node in project_reference.get_children(True):
        project_objects.append(node)
 
    for i in project_objects:
        print("Found: ", i.type, i.guid, i.get_name())
    return project_objects
 
def export_objects(collected_objects, project_reference):
    if not os.path.exists(object_path):
        os.makedirs(object_path)
 
    # Export the files.
    for candidate in collected_objects:
        # Create a list of objects to export:
        # The object itself
        objects = [candidate]
 
        # And sub-objects (POUs can have actions, properties, ...)
        objects.extend(candidate.get_children(True))
 
        # And the parent folders.
        parent = candidate.parent
        while ((not parent.is_root) and parent.is_folder):
            objects.append(parent)
            parent = parent.parent
 
        # Create a unique file name
        filename = os.path.join(object_path, "%s__%s.export" % (candidate.get_name(), candidate.guid))
 
        # Print some user information
        print("Exporting " + str(len(objects)) + " objects to: " + filename)
 
        # And actually export the project
        project_reference.export_native(objects, filename)

try:
    # Clean up any open project
    if projects.primary:
        projects.primary.close()
 
    # Open a project first
    project_reference = projects.open(os.path.join(project_path, project_name))
 
    # Collect the objects
    collected_objects = collect_objects(project_reference)
 
    export_objects(collected_objects, project_reference)
except Exception as exception:
    print("Error: " + str(exception))
    if not system.trace:
       print("Please turn on the 'Script Tracing' function to get detailed information about the script execution.")
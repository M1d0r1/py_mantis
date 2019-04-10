from model.project import Project
from utils.randomdata import RandomData
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:",["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 4
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

status_list = ["development", "release", "stable", "obsolete"]
view_status_list = ["public", "private"]


testdata = [Project(name="Name" + RandomData.get_random_string(), status = RandomData.get_random_list_value(status_list), inherit = RandomData.get_random_bool(), view_status =RandomData.get_random_list_value(view_status_list), description=RandomData.get_random_multistring())
            for i in range(n-1)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "..", f)

with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json", indent = 2)
    out_file.write(jsonpickle.encode(testdata))
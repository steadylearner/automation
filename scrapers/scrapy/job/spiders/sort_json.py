# import os
# import sys

# import json

# with open(sys.argv[1], 'r') as reader:
#     json_str = reader.read()
#     json_lists = json.loads(json_str) # dict, read

#     with open(sys.argv[1], 'w+') as writer:
#         sorted_list = sorted(json_lists, key = lambda i: i["date"], reverse = True) # only work for list of dicts
#         json_sorted_str = json.dumps(sorted_list, indent=4) # write
#         writer.write(json_sorted_str)


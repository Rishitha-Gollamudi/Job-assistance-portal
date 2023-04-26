import pickle
from tree import Node, Tree
import json

def tree_to_dict(node):
    return {"data": node.data, "children": [tree_to_dict(child) for child in node.children]}

def dict_to_tree(node_dict):
    node = Node(node_dict["data"])
    for child_dict in node_dict["children"]:
        child_node = dict_to_tree(child_dict)
        node.children.append(child_node)
    return node

def save_json(file_path,save_file_path):
    # read the JSON file into a string
    with open(file_path, 'rb') as f:
        job_tree = pickle.load(f)
    tree_dict = tree_to_dict(job_tree.root)
    json_str = json.dumps(tree_dict)
    with open(save_file_path, "w") as f:
        f.write(json_str)
    return 

def json_reading(file_path):
    # read the JSON file into a string
    with open(file_path, "r") as f:
        json_str = f.read()
    tree_dict = json.loads(json_str)
    return dict_to_tree(tree_dict)

# save_json('job_tree.pickle',"tree.json")
# root = json_reading("tree.json")

with open('job_tree.pickle', 'rb') as f:
    job_tree = pickle.load(f)
print(job_tree.root.children)
job_tree.root.children[-1].children[-4].children[0].data = job_tree.root.children[2].children[-4].children[0].data
print(job_tree.root.children[5].children[-4].children[0].data )
for i in range(6):
   print(job_tree.root.children[-1].children[-4].children[0].data)
import json
from tree import Node, Tree

def generate_job_tree(comp_data,data_ques,salary_data1,query,attr_list):
   root_node = Node(query)  
   node_questions = Node('question')
   node_min_salary = Node('min_sal')
   node_max_salary = Node('max_sal')
   node_med_salary = Node('med_sal')
   #print(data)
   data = comp_data['data']
   salary_data = salary_data1['data']
   for i in range(len(data)):
       #print(data[i].keys())
    #    comp_name = data[i]['employer_name']
    #    print(data[i])
       comp_name = data[i][0]
       comp_node = Node(comp_name)
       for j in range(len(attr_list)):
            temp_node = Node(attr_list[j])
            # temp_node.add_child(Node(data[i][attr_list[j]]))
            temp_node.add_child(Node(data[i][j+1]))
            comp_node.add_child(temp_node)
       root_node.add_child(comp_node)
   questions = []
   for k in range(len(data_ques)):
       questions.append(data_ques[k]["questions"])
   node_questions.add_child(Node(questions))
   node_min_salary.add_child(Node(salary_data[0]['min_salary']))
   node_max_salary.add_child(Node(salary_data[0]['max_salary']))
   node_med_salary.add_child(Node(salary_data[0]['median_salary']))
   root_node.add_child(node_questions)
   root_node.add_child(node_min_salary)
   root_node.add_child(node_max_salary)
   root_node.add_child(node_med_salary)
#    job_tree = Tree()
#    job_tree.add_root(root_node)
   return root_node
def create_json_from_tree(main_node,tree):
#    print(main_node[1].data)
   entries = len(main_node)
   data = []
   for i in range(entries-4):
      temp = []
      temp.append(main_node[i].data)
      temp.append(tree.find(main_node[i], 'job_employment_type')[0].data)
      temp.append(tree.find(main_node[i], 'job_title')[0].data)
      temp.append(tree.find(main_node[i], 'job_apply_link')[0].data) 
      temp.append(tree.find(main_node[i], 'job_description')[0].data)
      temp.append(tree.find(main_node[i], 'job_posted_at_datetime_utc')[0].data)
      data.append(temp)
   return {'data':data}

def create_questions_json_from_tree(main_node,tree):
#    print(main_node[1].data)
   questions = main_node[-4].children[0].data
   data = []
   for ques in questions:
      temp = {"questions":ques,"company":""}
      data.append(temp)
   return data


def create_salary_json_from_tree(main_node,tree):
#    print(main_node[1].data)
   min_salary = main_node[-3].children[0].data
   max_salary = main_node[-2].children[0].data
   median_salary = main_node[-1].children[0].data
   data = [{'min_salary':min_salary,'max_salary':max_salary,'median_salary':median_salary}]
   return data

with open(r'C:\Users\grishita\Downloads\Data Engineer_san diego_job_listings.json','r') as myfile:  
  data = json.load(myfile)  
# print((data))

with open('company_questions.json','r') as myfile:  
  data_ques = json.load(myfile)

with open (r'C:\Users\grishita\Downloads\software engineer_tempe_job_salary.json','r') as myfile:
   salary_data = json.load(myfile)
attribute_list = ["job_employment_type","job_title","job_apply_link","job_description","job_posted_at_datetime_utc"]
query = 'Data Engineer'


main_tree  = Tree()
main_tree.add_root(Node('main'))

if main_tree.find(main_tree.root, query):
   
   query_node = main_tree.find_node(main_tree.root, query)
#    print('################################')
#    print(query_node[0].children[0].data)
#    print('################################')
   dict = create_json_from_tree(query_node,main_tree)
else:
   query_tree = generate_job_tree(data,data_ques,salary_data,query,attribute_list)
   main_tree.root.add_child(query_tree)

if main_tree.find(main_tree.root, query):
   query_node = main_tree.find_node(main_tree.root, query)
   dict = create_json_from_tree(query_node,main_tree)
   print(dict)









   

# query_tree = generate_job_tree(data,data_ques,salary_data,query,attribute_list)
# main_tree.root.add_child(query_tree)  
# query_node = main_tree.find_node(main_tree.root, query)
# print(query_node[0].children[0].data)
#    


# for i in range(5):
#   print(i)
#   print(query_tree.root.children[i].data)
#   print(query_tree.find(query_tree.root.children[i], 'job_role')[0].data)
#   print(query_tree.find(query_tree.root.children[i], 'company_city')[0].data)
#   print(query_tree.find(query_tree.root.children[i], 'job_description')[0].data)
#   print(query_tree.find(query_tree.root.children[i], 'job_salary')[0].data)
# print((query_tree.find(query_tree.root, 'question')[0].data))

# for i in (query_tree.find(query_tree.root, 'question')[0].data).split("."):
#    print(i)

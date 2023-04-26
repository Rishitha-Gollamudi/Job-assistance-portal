from flask import Flask, render_template, request,Response
import os
import json
import pandas as pd
import pickle
# from data_extraction_code.data_reviews import Reviews
from data_API.api import job_search
from data_extraction_code.data_questions import questions
from tree import Node, Tree

app = Flask(__name__)


def generate_job_tree(comp_data,data_ques,salary_data,query,attr_list):
   root_node = Node(query)  
   node_questions = Node('question')
   node_min_salary = Node('min_sal')
   node_max_salary = Node('max_sal')
   node_med_salary = Node('med_sal')
   data = comp_data['data']
#    salary_data = salary_data1['data']
   for i in range(len(data)):
       comp_name = data[i][0]
       comp_node = Node(comp_name)
       for j in range(len(attr_list)):
            temp_node = Node(attr_list[j])
            # print(attr_list[j],data[i][j+1])
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
   return root_node

def create_job_json_from_tree(main_node,tree):
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
      temp.append(tree.find(main_node[i], 'Qualifications')[0].data)
 
      temp.append(tree.find(main_node[i], 'Benefits')[0].data)
    #   print(main_node[i].children)
      for k in main_node[i].children:
          print(k.data)
      data.append(temp)
   return {'data':data}

def create_questions_json_from_tree(main_node,tree):
   questions = main_node[-4].children[0].data
   data = []
   for ques in questions:
      temp = {"questions":ques,"company":""}
      data.append(temp)
   return data

def create_salary_json_from_tree(main_node,tree):
   min_salary = main_node[-3].children[0].data
   max_salary = main_node[-2].children[0].data
   median_salary = main_node[-1].children[0].data
   data = [{'min_salary':min_salary,'max_salary':max_salary,'median_salary':median_salary}]
   return data
    
@app.route("/")  
def home():
    return render_template("index.html")
@app.route("/qs/<job_role>", methods=['GET'])  
def qs(job_role):
    return render_template("qs.html",job_role=job_role)
@app.route("/data",methods = ['GET','POST'])
def results():
    if request.method == "POST":
        job_role = request.form['role']
        job_location = request.form['loc']
        query = job_role.lower() + "_" + job_location.lower()


        ### replace with tree###########


        # val=os.path.exists(f'static/{job_role}_{job_location}_job_listings.json')
        # if val==True:
        #     with open(f'static/{job_role}_{job_location}_job_listings.json','r') as myfile:  
        #         results = json.load(myfile)
        # else:
        #     results = job_search.job_listings(job_role,job_location)

        #     salary = job_search.job_salary(job_role,job_location)

        # question_list = questions.questions(job_role,job_location)


        # print(salary)
        # print(question_list)
        if not os.path.exists("job_tree.pickle"):
            job_tree  = Tree()
            job_tree.add_root(Node('main'))
            with open('job_tree.pickle', 'wb') as f:
                pickle.dump(job_tree, f)
        else: 
            with open('job_tree.pickle', 'rb') as f:
                job_tree = pickle.load(f)
        if job_tree.find(job_tree.root, query):
            query_node = job_tree.find_node(job_tree.root, query)
            job_data = create_job_json_from_tree(query_node,job_tree)
            question_data = create_questions_json_from_tree(query_node,job_tree)
            salary_data = create_salary_json_from_tree(query_node,job_tree)
            ####create json

            with open("static/job_listings.json", 'w') as myfile:
                myfile.write(json.dumps(job_data,indent = 4))
            with open("static/company_questions.json", 'w') as myfile:
                myfile.write(json.dumps(question_data,indent = 4))
            with open("static/company_salary.json", 'w') as myfile:
                myfile.write(json.dumps(salary_data,indent = 4))

        else:
            results = job_search.job_listings(job_role,job_location)
            attribute_list = ["job_employment_type","job_title","job_apply_link","job_description","job_posted_at_datetime_utc",'Qualifications','Benefits']
            salary_data = job_search.job_salary(job_role,job_location)
            question_data = questions.questions(job_role,job_location)
            query_node = generate_job_tree(results,question_data,salary_data,query,attribute_list)
            job_tree.root.add_child(query_node)
            with open('job_tree.pickle', 'wb') as f:
                pickle.dump(job_tree, f)



        
        # with open(f'company_info.pickle', 'rb') as f:
        #     query_tree = pickle.load(f)

            
        #     if job_location == query_tree.find(query_tree.root, 'location')[0].data:
                
        # lst=Reviews.company_reviews('Zoox')
        
    return render_template('table.html',job_role = job_role,job_location= job_location,salary_data=salary_data)


if __name__ == "__main__":
    app.run(debug=True, port= 5001)
import requests
import json
import jobsecrets


class job_search:
    def job_listings(job,loc):
        
          
        url = "https://jsearch.p.rapidapi.com/search"

        querystring = {"query":f"{job} in {loc}, USA","page":"1","num_pages":"1"}
        key2 = jobsecrets.jobs_api_key

        headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": key2,
	"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

        response = requests.get(url, headers=headers, params=querystring)

        response=response.json()
    
        job_list = []
        for i in range(len(response['data'])):
            temp = [
                response['data'][i]['employer_name'],
               response['data'][i]['job_employment_type'],
                response['data'][i]['job_title'] ,
               response['data'][i]['job_apply_link'] ,
                 response['data'][i]['job_description'],
                response['data'][i]['job_posted_at_datetime_utc'] 
    
               
            ]
            if 'Qualifications' in  response['data'][i]['job_highlights'].keys():
                temp.append( response['data'][i]['job_highlights']['Qualifications'])
            else:
                temp.append('No Qualifications data available')
            if 'Benefits' in  response['data'][i]['job_highlights'].keys():
                temp.append( response['data'][i]['job_highlights']['Benefits'])
            else:
                temp.append('No benefits data available')
            job_list.append(temp)

        final_list = {'data':job_list}

        #  job_list={ 
        #         'employer_name':response['data'][i]['employer_name'],
        #         'job_employment_type': response['data'][i]['job_employment_type'],
        #         'job_title':response['data'][i]['job_title'] ,
        #         'job_apply_link':response['data'][i]['job_apply_link'] ,
        #         'job_description': response['data'][i]['job_description'],
        #         'job_posted_at_datetime_utc':response['data'][i]['job_posted_at_datetime_utc'] ,
        #         'Qualifications': response['data'][i]['job_highlights']['Qualifications'],
        #         'Benefits':response['data'][i]['job_highlights']['Benefits'] ,
        #     }
        # store all the details in a JSON
        with open("static/job_listings_raw.json", 'w') as myfile:
            myfile.write(json.dumps(response,indent = 4))
        # store specific details in a JSON
        with open("static/job_listings.json", 'w') as myfile:
            myfile.write(json.dumps(final_list,indent = 4))

        
        return final_list
    
    def job_salary(job,loc):
       

        url = "https://job-salary-data.p.rapidapi.com/job-salary"

        querystring = {"job_title":f"{job}","location":f"{loc}, usa","radius":"200"}
        key1 = jobsecrets.salary_api_key
        #key1 = '3b374677cbmshf6e6351ca7d60abp1155f1jsn2951405a43d0'
        headers = {
                "content-type": "application/octet-stream",
                "X-RapidAPI-Key": key1,
                "X-RapidAPI-Host": "job-salary-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        response=response.json()
        data = [{'min_salary':response['data'][0]['min_salary'],'max_salary':response['data'][0]['max_salary'],'median_salary':response['data'][0]['median_salary']}]
        # store all the details in a JSO
        with open(f"static/job_salary.json", 'w') as myfile:
            myfile.write(json.dumps(data,indent = 4))
        return data
    
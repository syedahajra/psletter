from flask import Flask,render_template,request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key="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"
#openai.api_key = "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"

messages=[]

@app.route('/',methods=['GET', 'POST'] )
def home():
    return render_template('index.html')

@app.route("/psstatement", methods=['GET', 'POST'])
def ps_statement():
    if request.method=='POST':
        
        system_msg="write an entire personal statement to a univeristy for a student on information provided by user."
        messages.append({"role": "system", "content": system_msg})
        #if interested in specific project

        q="Interested in specific project:"
         

        ans=request.form['projectOption']
        messages.append({"role": "user", "content":q+ ans})

        #project title, supervisor name, application

        q="Project title of the project interested in:"
         

        ans=request.form['project_title']
        messages.append({"role": "user", "content":q + ans})

        q="Research Application of the project interested in:"
         

        ans=request.form['research_application']
        messages.append({"role": "user", "content":q + ans})

        q="Supervisor name of the project interested in:"
         

        ans=request.form['research_supervisor']
        messages.append({"role": "user", "content":q + ans})

        #research area

        q="Research area interested in:"
         

        ans=request.form['research_area']
        messages.append({"role": "user", "content":q + ans})

        """response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})"""
        
        #prev job details

        q="Previously worked (job or internship) at:"
         

        ans=request.form['organization_name']
        messages.append({"role": "user", "content":q+ ans})

        q="Project worked upon at job or internship:"
         

        ans=request.form['job_project']
        messages.append({"role": "user", "content":q+ ans})

        #fyp details

        q="Final Year Project title:"
         

        ans=request.form['my_project_title']
        messages.append({"role": "user", "content":q+ ans})

        q2="Final Year Project's relevancy to the project want to work upon:"
        #messages.append({"role": "assistant", "content": q2})

        ans=request.form['my_project_details']
        messages.append({"role": "user", "content":q + ans})

        #courses i took

        q="Series of courses taken that sparked interest in this research area:"
         

        ans=request.form['series_of_courses']
        messages.append({"role": "user", "content":q + ans})

        #seminar/conference

        q="Title of seminar or conference that made interested in this research area:"
         

        ans=request.form['seminar_name']
        messages.append({"role": "user", "content":q + ans})

        #novel tech

       #q="Interested in novel technologies:"
        #messages.append({"role": "assistant", "content": q})

        #ans=request.form['explore_tech']
        #messages.append({"role": "user", "content": ans})

        #effect on society

        q="How this research area effects society:"
         
        ans=request.form['personal_social_effect']
        messages.append({"role": "user", "content":q + ans})

        """response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})"""

        #taking details of undergrad

       # q3="How have your undergraduate studies prepared you for advanced research or coursework in your desired graduate program?"
        #messages.append({"role": "assistant", "content": q3})

        q="solid foundation in the fundamental theories, concepts, and methodologies through courses: "
        
        ans=request.form['foundation_courses']
        messages.append({"role": "user", "content":q + ans})

        q="Maintained a high CGPA of: "
        
        ans=request.form['cgpa']
        messages.append({"role": "user", "content":q + ans})

        q="Recieved awards: "
        
        ans=request.form['academic_awards']
        messages.append({"role": "user", "content":q + ans})

        q="Was member of student organization/society: "
        q1="with post: "
        ans=request.form['sto_name']
        ans1=request.form['sto_post']
        messages.append({"role": "user", "content":q + ans + q1 + ans1})

        """response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})"""

        #analytical skills
    
        ans=request.form['analytical']
        ans1=request.form['analytical_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})
        
            #comm skils
        ans=request.form['communication']
        ans1=request.form['communication_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #adaptability skils
        ans=request.form['adaptability']
        ans1=request.form['adaptability_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #leadership skils
        ans=request.form['Leadership']
        ans1=request.form['Leadership_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #teamwork skils
        ans=request.form['teamwork']
        ans1=request.form['teamwork_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #continuous learning
        ans=request.form['continuouslearning']
        ans1=request.form['continuouslearning_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #time manage skills
        ans=request.form['timemanage']
        ans1=request.form['timemanage_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        """response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})"""

        #personal background, cultural experiences, or personal challenges contribute to your understanding of the subject matte

        #appreciation
        ans=request.form['appreciation']
        ans1=request.form['appreciation_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #tackle complex
        ans=request.form['complexprob']
        ans1=request.form['complexprob_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #innovative sol
        ans=request.form['innovativesol']
        ans1=request.form['innovativesol_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #comparative perspective
        ans=request.form['comparativepers']
        ans1=request.form['comparativepers_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #bridge gap
        ans=request.form['bridgegap']
        ans1=request.form['bridgegap_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        """ans="Now write a personal statement to university according to previous paragraphs you generated."
        messages.append({"role": "user", "content": ans})"""

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        with open('personal_statement.txt', 'w') as personal_statement:
           personal_statement.write(reply)
        print("\n"+reply+"\n")
        return render_template('psstatement.html',reply=reply)
    
    return render_template("psstatement.html")

@app.route('/recomletter',methods=['GET', 'POST'] )
def recom_letter():
    if request.method=='POST':
        
        system_msg="write an entire recommendation letter for graduate school application on information provided by user."
        messages.append({"role": "system", "content": system_msg})
       
        #your intro

        ans=request.form['your_name']
        messages.append({"role": "user", "content":"Recommender's Name"+ ans})
        
        ans=request.form['your_position']
        messages.append({"role": "user", "content":"Recommender's Position"+ ans})

        ans=request.form['your_organization']
        messages.append({"role": "user", "content":"Recommender's Organization"+ ans})

        ans=request.form['your_experience']
        messages.append({"role": "user", "content":"Recommender's Experience"+ ans})

        ans=request.form['your_academicbg']
        messages.append({"role": "user", "content":"Recommender's Academic background:"+ ans})

        ans=request.form['your_achievements']
        messages.append({"role": "user", "content":"Recommender's Achievements:"+ ans})

        #their intro
        ans=request.form['student_name']
        messages.append({"role": "user", "content":"Students name:"+ ans})

        ans=request.form['grad_prog']
        messages.append({"role": "user", "content":"Graduate program student is applying to:"+ ans})

        #relationship

        ans=request.form['academic_relationship']
        ans1=request.form['how_academic']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        ans=request.form['professional_relationship']
        ans1=request.form['how_professional']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        ans=request.form['supervisory_relationship']
        ans1=request.form['how_supervisory']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        ans=request.form['collabrative_relationship']
        ans1=request.form['how_collabrative']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        ans=request.form['community_involvement']
        ans1=request.form['how_community']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #skills
        #analytical skills
    
        ans=request.form['analytical']
        ans1=request.form['analytical_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})
        
            #comm skils
        ans=request.form['communication']
        ans1=request.form['communication_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #adaptability skils
        ans=request.form['adaptability']
        ans1=request.form['adaptability_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #leadership skils
        ans=request.form['Leadership']
        ans1=request.form['Leadership_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #teamwork skils
        ans=request.form['teamwork']
        ans1=request.form['teamwork_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #continuous learning
        ans=request.form['continuouslearning']
        ans1=request.form['continuouslearning_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        #time manage skills
        ans=request.form['timemanage']
        ans1=request.form['timemanage_example']
        messages.append({"role": "user", "content":ans + ":" + ans1})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        with open('recom_letter.txt', 'w') as recom_letter:
           recom_letter.write(reply)
        print("\n"+reply+"\n")
        return render_template('recomletter.html',reply=reply)

    return render_template('recomletter.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)
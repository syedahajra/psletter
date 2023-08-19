from flask import Flask,render_template,request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key="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"

@app.route('/',methods=['GET', 'POST'] )
def home():
    return render_template('index.html')

@app.route('/features',methods=['GET', 'POST'] )
def features():
    return render_template('features.html')

@app.route('/researchstatement',methods=['GET', 'POST'] )
def researchstatement():
    if request.method=='POST':

        messages=[]
        system_msg="write paragraphs for research statementfor faculty position on information provided by user."
        messages.append({"role": "system", "content": system_msg})

        ans = request.form['your_name']
        if ans != "":
            messages.append({"role": "user", "content": "Name:" + ans})

        ans = request.form['degree']
        if ans != "":
            messages.append({"role": "user", "content": "Highest Degree:" + ans})

        ans = request.form['specialization']
        if ans != "":
            messages.append({"role": "user", "content": "Specialization in:" + ans})

        ans = request.form['uni_name']
        if ans != "":
            messages.append({"role": "user", "content": "University from which specialization is done:" + ans})

        messages.append({"role": "user", "content": "Write only introductory paragraph:" + ans})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        ans = request.form['research']
        if ans != "":
            messages.append({"role": "user", "content": "Current research you are working on:" + ans})

        ans = request.form['research_imp']
        if ans != "":
            messages.append({"role": "user", "content": "Current research importance:" + ans})

        ans=request.form['techniques_used']
        if ans != "":
            messages.append({"role": "user", "content":"Methodologies and Techniques Employed in current Research:"+ ans})

        ans=request.form['contribution_field']
        if ans != "":
            messages.append({"role": "user", "content":"Contributions to the Field of Research:"+ ans})

        ans=request.form['research_applied']
        if ans != "":
            messages.append({"role": "user", "content":"Potential Commercial and Academic Applications of my current Research:"+ ans})

        ans=request.form['research_impact']
        if ans != "":
            messages.append({"role": "user", "content":"Impact on Related Fields and Interdisciplinary Connections:"+ ans})

        ans=request.form['research_new_ques']
        if ans != "":
            messages.append({"role": "user", "content":"Emerging Research Questions and Future Directions:"+ ans})

        ans=request.form['major_findings']
        if ans != "":
            messages.append({"role": "user", "content":"Key Discoveries, Results, and Significance of Research Outcomes:"+ ans})

        ans=request.form['preliminary_results']
        if ans != "":
            messages.append({"role": "user", "content":"Initial Insights and Early Discoveries from my current Research:"+ ans})

        messages.append({"role": "user", "content":"Generate paragraph(s) for my current research"+ ans})
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        print(reply)
        ans=request.form['prevresearchtog']
        messages.append({"role": "user", "content":"Was your previous research area different from current:"+ ans})

        if ans=="Yes":

            ans=request.form['prevresearch_area']
            if ans != "":
                messages.append({"role": "user", "content":"Previous research area:"+ ans})

            ans=request.form['prevresearch']
            if ans != "":
                messages.append({"role": "user", "content":"previous research:"+ ans})

            ans=request.form['prevresearch_results']
            if ans != "":
                messages.append({"role": "user", "content":"Results and findings of previous research:"+ ans})

            ans=request.form['prevresearch_affect']
            if ans != "":
                messages.append({"role": "user", "content":" how previous research affect the field/research community:"+ ans})

            ans=request.form['publishedpapers']
            if ans != "":
                messages.append({"role": "user", "content":"details about any papers you have published:"+ ans})

            ans=request.form['awards']
            if ans != "":
                messages.append({"role": "user", "content":"Have you received any awards or recognitions for your research?"+ ans})

            ans=request.form['citations']
            if ans != "":
                messages.append({"role": "user", "content":"How widely has your research been cited? "+ ans})

            ans=request.form['followup']
            if ans != "":
                messages.append({"role": "user", "content":"provide some insights into how your current research findings (if any) have led to any follow-up studies or new research questions:"+ ans})

            messages.append({"role": "user", "content":"Generate paragraph for my previous research"+ ans})

            response = openai.ChatCompletion.create(
                model = "gpt-3.5-turbo",
                messages=messages)

            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print(messages)
        
        ans=request.form['futureresearch_area']
        if ans != "":
            messages.append({"role": "user", "content":"Research area you want to work in future:"+ ans})

        ans=request.form['futureresearch_why']
        if ans != "":
            messages.append({"role": "user", "content":"If changing research area then why:"+ ans})

        ans=request.form['develop_new_skills']
        if ans != "":
            messages.append({"role": "user", "content":"How do you plan to develop new skills and knowledge for your future research:"+ ans})

        ans=request.form['futureresearch_imp']
        if ans != "":
            messages.append({"role": "user", "content":"Importance and Relevance of Future Research:"+ ans})

        ans=request.form['futuretechniques_used']
        if ans != "":
            messages.append({"role": "user", "content":"Methodologies and Techniques that will be employed in the Research:"+ ans})

        ans=request.form['futurecontribution_field']
        if ans != "":
            messages.append({"role": "user", "content":"Envisioned Contributions to the Field Through Future Research:"+ ans})

        ans=request.form['futureresearch_applied']
        if ans != "":
            messages.append({"role": "user", "content":"Future Applications of Research: Commercial and Academic Impact:"+ ans})

        ans=request.form['futuresearch_impact']
        if ans != "":
            messages.append({"role": "user", "content":"Potential Cross-Disciplinary Impact of Future Research:"+ ans})

        messages.append({"role": "user", "content":"Generate paragraph(s) for my future research"+ ans})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        messages.append({"role": "user", "content":"Now using the paragraphs you generated write an entire research statement focusing on current research and including previous research (if any) and future research."})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})

        return render_template('researchstatement.html',reply=reply)

    return render_template('researchstatement.html')

@app.route('/teachingstatement',methods=['GET', 'POST'] )
def teachingstatement():
    if request.method=='POST':
        messages=[]
        system_msg="write an entire teaching statement for user on information provided by user."
        messages.append({"role": "system", "content": system_msg})

        ans=request.form['your_name']
        messages.append({"role": "user", "content":"Name:"+ ans})

        ans=request.form['degree']
        messages.append({"role": "user", "content":"Highest Degree:"+ ans})

        ans=request.form['specialization']
        messages.append({"role": "user", "content":"Specialization in:"+ ans})

        ans=request.form['uni_name']
        messages.append({"role": "user", "content":"Univeristy from which specialization is done:"+ ans})

        ans=request.form['your_prev_subj']
        messages.append({"role": "user", "content":"subject(s) that i have previously taught:"+ ans})

        ans=request.form['your_subj']
        messages.append({"role": "user", "content":"subject(s) wanting to teach:"+ ans})

        ans=request.form['your_experience']
        messages.append({"role": "user", "content":"Experience:"+ ans})

        ans=request.form['your_position']
        messages.append({"role": "user", "content":"Position:"+ ans})

        ans=request.form['your_organization']
        messages.append({"role": "user", "content":"Organizations previously worked in:"+ ans})

        ans=request.form['relevant_position']
        messages.append({"role": "user", "content":"any other relevant position:"+ ans})

        ans=request.form['learning_occurs']
        messages.append({"role": "user", "content":"My conception of how learning occurs:"+ ans})

        ans=request.form['teaching_method']
        messages.append({"role": "user", "content":"A description of how my teaching facilitates student learning:"+ ans})

        ans=request.form['reason_teaching_method']
        messages.append({"role": "user", "content":"A reflection of why I teach the way you do:"+ ans})

        ans=request.form['goals']
        messages.append({"role": "user", "content":"the goals I have for myself and for my students:"+ ans})
        
        ans=request.form['evidence']
        messages.append({"role": "user", "content":"What, for me, constitutes evidence of student learning::"+ ans})

        ans=request.form['inclusive_learning']
        messages.append({"role": "user", "content":"The ways in which you create an inclusive learning environment:"+ ans})

        ans=request.form['your_interests']
        messages.append({"role": "user", "content":"Your interests in new techniques, activities, and types of learning:"+ ans})
        
        #print(messages)
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        
        return render_template('teachingstatement.html',reply=reply)

    return render_template('teachingstatement.html')

@app.route("/psstatement", methods=['GET', 'POST'])
def ps_statement():
    if request.method=='POST':
        messages=[]
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
        
        return render_template('psstatement.html',reply=reply)
    
    return render_template("psstatement.html")

@app.route('/recomletter',methods=['GET', 'POST'] )
def recom_letter():
    if request.method=='POST':
        messages=[]
        system_msg="write an entire recommendation letter for graduate school application on information provided by user."
        messages.append({"role": "system", "content": system_msg})
       
        #your intro

        ans=request.form['your_name']
        messages.append({"role": "user", "content":"Recommender's Name:"+ ans})
        
        ans=request.form['your_position']
        messages.append({"role": "user", "content":"Recommender's Position:"+ ans})

        ans=request.form['your_organization']
        messages.append({"role": "user", "content":"Recommender's Organization:"+ ans})

        ans=request.form['your_experience']
        messages.append({"role": "user", "content":"Recommender's Experience:"+ ans})

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

        #recompower
        ans=request.form['recompower']
        messages.append({"role": "user", "content": ans})

        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=messages)

        reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        
        return render_template('recomletter.html',reply=reply)

    return render_template('recomletter.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000, host="0.0.0.0")
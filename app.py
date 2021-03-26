from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
#from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__)
model=pickle.load(open('logi_model.pkl','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


#standard_to = StandardScaler()
scaler = MinMaxScaler()
@app.route("/predict", methods=['POST'])
def predict():
    temp_array = list()
    
    

    if request.method == 'POST':
        loan_amnt = float(request.form['loan_amnt'])
        term = float(request.form['term'])
        int_rate = float(request.form['int_rate'])
        earliest_cr_line=float(request.form['earliest_cr_line'])
        annual_inc = float(request.form['annual_inc'])
        dti = float(request.form['dti'])
       
    
      
        open_acc= float(request.form['open_acc'])
        pub_rec= float(request.form['pub_rec'])
        revol_bal= float(request.form['revol_bal'])
        revol_util= float(request.form['revol_util'])
        total_acc= float(request.form['total_acc'])
        pub_rec_bankruptcies= float(request.form['pub_rec_bankruptcies'])
       
        mort_acc= float(request.form['mort_acc'])
        home_ownership=request.form['home_ownership']
        if(home_ownership =='MORTGAGE'):
            temp_array = temp_array + [1,0,0,0,0]
        elif(home_ownership =='NONE'):
            temp_array = temp_array + [0,1,0,0,0]
        elif(home_ownership =='OTHER'):
            temp_array = temp_array + [0,0,1,0,0]  
        elif(home_ownership =='OWN'):
            temp_array = temp_array + [0,0,0,1,0]  
        elif(home_ownership =='RENT'):
            temp_array = temp_array + [0,0,0,0,1]    
        else:
             temp_array = temp_array + [0,0,0,0,0] 
            
        verification_status =request.form['verification_status']
        if(verification_status =='Source Verified'):
            temp_array = temp_array + [1,0]
        elif(verification_status == 'Verified'):
            temp_array = temp_array + [0,1]
        else:
            temp_array = temp_array + [0,0]
                  
            
        initial_list_status =request.form['initial_list_status']
        if(initial_list_status =='w'):
            temp_array = temp_array + [1]
        else:
            temp_array = temp_array + [0]
            
        application_type=request.form['application_type']
        if(application_type =='INDIVIDUAL'):
            temp_array = temp_array + [1,0]
        elif(application_type =='JOINT'):
            temp_array = temp_array + [0,1]
        else:
            temp_array = temp_array + [0,0]
            
        zip_code =request.form['zip_code']
        if(zip_code =='05113'):
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0]
        elif(zip_code=='11650'):
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0]
        elif(zip_code=='22690'):
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0]
        elif(zip_code=='29597'):
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0]
        elif(zip_code=='30723'):
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0]
        elif(zip_code=='48052'):
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0]
        elif(zip_code=='70466'):
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0]
        elif(zip_code=='86630'):
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0]
        elif(zip_code=='93700'):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1]
           
        else:
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0]
            
        purpose =request.form['purpose']
        if(purpose =='credit_card'):
            temp_array = temp_array + [1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(purpose =='debt_consolidation'):
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif(purpose =='educational'):
            temp_array = temp_array + [0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif(purpose =='home_improvement'):
            temp_array = temp_array + [0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif(purpose =='house'):
            temp_array = temp_array + [0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif(purpose =='major_purchase'):
            temp_array = temp_array + [0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif(purpose =='medical'):
            temp_array = temp_array + [0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif(purpose =='moving'):
            temp_array = temp_array + [0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif(purpose =='other'):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif(purpose =='renewable_energy'):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif(purpose =='small_business'):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif(purpose =='vacation'):
            temp_array = temp_array + [0,1,0,0,0,0,0,0,0,0,0,1,0]
        elif(purpose =='wedding'):
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,1]
        else:
            temp_array = temp_array + [0,0,0,0,0,0,0,0,0,0,0,0,0]
            
    
            
        sub_grade=request.form['sub_grade']
        if(sub_grade=='A2'):
            temp_array = temp_array +[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='A3'):
            temp_array = temp_array +[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='A4'):
            temp_array = temp_array +[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='A5'):
            temp_array = temp_array +[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='B1'):
            temp_array = temp_array +[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='B2'):
            temp_array = temp_array +[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='B3'):
            temp_array = temp_array +[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='B4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='B5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='C1'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='C2'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='C3'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='C4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='C5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='D1'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='D2'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='D3'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='D4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='D5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='E1'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='E2'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='E3'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='E4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='E5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='F1'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
        elif(sub_grade=='F2'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
        elif(sub_grade=='F3'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
        elif(sub_grade=='F4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        elif(sub_grade=='F5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
        elif(sub_grade=='G1'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
        elif(sub_grade=='G2'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
        elif(sub_grade=='G3'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
        elif(sub_grade=='G4'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
        elif(sub_grade=='G5'):
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        else:
            temp_array = temp_array +[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
        temp_array = temp_array + [loan_amnt, term, int_rate, annual_inc, dti, open_acc, pub_rec, revol_bal, revol_util,
                       total_acc,mort_acc,earliest_cr_line,pub_rec_bankruptcies ]
        
        final_feat =np.array([temp_array])
        
        prediction=model.predict(final_feat)
        output=prediction[0]
        
        
        if output==1:
            return render_template('index.html',prediction_text="Loan Status-Charged Off")
        else:
            return render_template('index.html',prediction_text="Loan Status-Fully Paid")
        
    else:
        
        return render_template('index.html')

        
if __name__=="__main__":
    app.run(debug=True)
        
        
        
            
            
            
            
            
            
            
            
            
    
            
        
            
            
            
             
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


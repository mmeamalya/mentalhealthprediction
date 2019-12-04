from flask import Flask, render_template, request
from datas import identified, discemploy, sought, bff, handled, fami, curemploy, ilfil, anonprev, iview, comfy, comforttalk
from datas import discussprevious, rtypes, discowork, wilcow, formal, seekhelp, past, anon, gender,interview, spv, inter, age
import pandas as pd

from prediction import prediction, prob

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        if data['identified']=='No':
            data['identified'] = 0
        else:
            data['identified'] = 1
        if data['discussprev']=='No':
            data['discussprev'] = 0
        else:
            data['discussprev'] = 1
        if data['discowork']=='No':
            data['discowork'] = 0
        else:
            data['discowork'] = 1
        if data['discemploy']=='No':
            data['discemploy'] = 0
        else:
            data['discemploy'] = 1
        if data['sought']=='No':
            data['sought'] = 0
        else:
            data['sought'] = 1
        data['bff'] = int(data['bff'])
        data['handled'] = (data['handled'])
        data['wilcow'] = (data['wilcow'])
        data['formal'] = (data['formal'])
        data['seekhelp'] = (data['seekhelp'])
        data['fami'] = (data['fami'])
        data['curemploy'] = (data['curemploy'])
        data['past'] = (data['past'])
        data['ilfil'] = (data['ilfil'])
        data['anon'] = (data['anon'])
        data['anonprev'] = (data['anonprev'])
        data['gender'] = (data['gender'])
        data['iview'] = (data['iview'])
        data['interview'] = (data['interview'])
        data['comfy'] = (data['comfy'])
        data['spv'] = (data['spv'])
        data['comforttalk'] = (data['comforttalk'])
        data['inter'] = (data['inter'])
        data['age'] = (data['age'])
        tempkey = []
        tempvalues = []
        for key, value in data.items():
            tempkey .append(key)
            tempvalues.append(value)
        print(data)
    
 
        hasil = prediction(tempvalues)
        proba = prob(tempvalues)
        maxprob = proba.max()
        
        if hasil==['Possibly']:
            return render_template('resultpossibly.html', hasil_pred=maxprob)
        if hasil==['Yes']:
            return render_template('resultyes.html', hasil_pred=maxprob)
        if hasil==['No']:
            return render_template('resultno.html', hasil_pred=maxprob)

    return render_template('prediction.html',dataage=age,datainter=inter,datacomforttalk=comforttalk,dataspv=spv,datacomfy=comfy,datainterview=interview,dataiview=iview,datagender=gender,dataanonprev=anonprev,dataanon=anon,datailfil=ilfil,datapast=past,datacuremploy=curemploy,datafami=fami,dataseekhelp=seekhelp,dataformal=formal,datawilcow=wilcow,datahandled=handled,databff=bff,datasought=sought,datadiscemploy=discemploy,data_identified = sorted(identified),datadiscowork=discowork,datadiscussprev=discussprevious)

@app.route('/login')
def login():
    return render_template('login.html')
  
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about',methods=['GET','POST'])
def about():
    # if request.method == "GET":
    #     return render_template('prediction.html')
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True, port=1111)  
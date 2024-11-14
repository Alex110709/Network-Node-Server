from flask import Flask, render_template, request, jsonify, session
import manage as m
import setting as s
app = Flask(__name__)

@app.route('/API', methods=['POST'])
def post():
   H_API = request.headers.get("API")
   if H_API == "getnetdata":
      cur=m.connect()
      name=m.get(cur,"name")
      cur=m.get(cur,"cur")
      return jsonify({'result': 'success', 'name':name,'cur':cur})
   elif H_API == "getplayerdata":
       session = request.form["session"]
       email = request.form["email"]
       cur = m.connect()
       rdata = m.getplayerdata(cur,session)
       if rdata == "NID":
           m.crpld(cur, session, email)
           return jsonify({'result': 'success', 'money': m.getplayerdata(cur, session)})
       else:
           return jsonify({'result':'success','money':m.getplayerdata(cur,session)})
   elif H_API == "send":
       session = request.form["session"]
       to = request.form["to"]
       aum = request.form["aum"]
       print(aum)
       con = m.connect()
       rec=m.send(con,session,to,int(aum))
       return jsonify({'result':'success','msg':rec})
   elif H_API == "admin":
       api_key=request.headers.get("KEY")
       ADA=request.headers.get("ADA")
       if api_key==s.API_KEY:
           if ADA=="":
               print("1",ADA)
           else:
               return jsonify({'result':'success','msg':'wrong ADA'})
       else:
           return jsonify({'result':'success','msg':'wrong key'})




if __name__ == '__main__':
   app.run('0.0.0.0',port=s.prot,debug=True)
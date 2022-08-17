from flask import *
application = Flask(__name__)
userdetails = {}
import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://test-cd762-default-rtdb.firebaseio.com/"})

@application.route('/',methods=["GET","POST"])
def hello_world():
   fdb= db.reference("/")
   global userdetails
   if(request.form):
      btnpressed = request.form['btn']
      if(btnpressed  == 'Login'):
         return render_template("Loginpage.html",var = "Please Enter Details")
      if(btnpressed  == 'Mobchange'):
         return render_template("Mobchange.html")
      if(btnpressed  == 'Mobchangesubmit'):
         newmob = request.form['newmobile']
         fdb.update({"Mob":newmob})
         userdetails = fdb.get()
         return render_template("details.html",sun = userdetails['Name'],pwd = userdetails['Password'],
                                eid =userdetails['Email'] ,mob =userdetails['Mob'] )
      
      if(btnpressed  == 'Profile'):
         userdetails = fdb.get()
         return render_template("details.html",sun = userdetails['Name'],pwd = userdetails['Password'],
                                eid =userdetails['Email'] ,mob =userdetails['Mob'] )
      if(btnpressed  == 'Signup'):
         return render_template("Signuppage.html",var = "Please Enter Details")
      if(btnpressed == 'SignupSubmit'):
         sun =  request.form['Susername']
         spwd =  request.form['Spassword']
         seid=  request.form['Semail']
         smob =  request.form['Smobile']
         fdb.update({"Name":sun,
                        "Password":spwd,
                        "Email":seid,
                        "Mob":smob})
         return render_template("Loginpage.html",var ="Signedup successfully , Please login now" )
      if(btnpressed == 'LoginSubmit'):
         userdetails = fdb.get()
         lun =  request.form['lusername']
         lpwd =  request.form['lpassword']
         sun = userdetails['Name']
         spwd =  userdetails['Password']
         if((sun == lun) and (spwd == lpwd)):
            return render_template("profile.html" )
         else:
            return render_template("Loginpage.html",var ="Invalid Details" )
      
   return render_template("homepage.html",var = "Please select anyone")

if __name__ == '__main__':
    application.run(debug = True,port = 5047)

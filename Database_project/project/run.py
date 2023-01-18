from Database_project.project.data_base_  import create_app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from Database_project.project.data_base_  import bcrypt,db

app= create_app()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#limiter = Limiter(
 #  app,
  # key_func=get_remote_address,
  # default_limits=["20 per minute", "1 per second"],
#)



    





def j():
  with app.app_context():
    #db.drop_all()
    #db.create_all()
    '''expert1=Expert(nom='0',numero=0, email='0')
    expert=Expert(genre='Mr.',nom='Admin',numero=12345,TYPE='Admin', email='test0001@gmail.com',visibility=False )
    db.session.add(expert1)
    db.session.add(expert)
    db.session.commit()
    expert1.id =0
    expert1.visibility=False
    hashed_password = bcrypt.generate_password_hash('12345').decode('utf-8')
    expert.password=hashed_password
    db.session.commit()'''



#db.drop_all() apturl==0.5.2;cffi==1.14.5
#db.create_all()



    
            
    

        
if __name__ == '__main__':
  #j()
  app.run(debug=True)



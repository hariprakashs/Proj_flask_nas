from application import app,db
from flask import render_template, request, json, Response

products = [{'ProductID':'PD1','Name':'Cashew nuts (grade 1)--180','Buying_rate':'760','Selling_rate':'850'},
{'ProductID':'PD2','Name':'Cashew nuts (grade 2)--240','Buying_rate':'680','Selling_rate':'750'},
{'ProductID':'PD3','Name':'Cashew nuts broken','Buying_rate':'600','Selling_rate':'660'},
{'ProductID':'PD4','Name':'Badam','Buying_rate':'560','Selling_rate':'750'},
{'ProductID':'PD5','Name':'Pista','Buying_rate':'1280','Selling_rate':'1650'},
{'ProductID':'PD6','Name':'Salted Pista','Buying_rate':'980','Selling_rate':'1100'},
{'ProductID':'PD7','Name':'Sesame oil - grade 1','Buying_rate':'260','Selling_rate':'320'},
{'ProductID':'PD8','Name':'Sesame oil - grade 2','Buying_rate':'190','Selling_rate':'250'},
{'ProductID':'PD9','Name':'Sesame oil - grade 3','Buying_rate':'130','Selling_rate':'190'},
{'ProductID':'PD10','Name':'Coconut oil','Buying_rate':'240','Selling_rate':'320'},
{'ProductID':'PD11','Name':'Groundnut oil','Buying_rate':'170','Selling_rate':'250'},
{'ProductID':'PD12','Name':'Mustard oil','Buying_rate':'115','Selling_rate':'180'},
{'ProductID':'PD13','Name':'Castor oil','Buying_rate':'150','Selling_rate':'200'},
{'ProductID':'PD14','Name':'Pure Ghee','Buying_rate':'540','Selling_rate':'650'},
{'ProductID':'PD17','Name':'Figs','Buying_rate':'740','Selling_rate':'810'},
{'ProductID':'PD15','Name':'Walnut (Grade 2)','Buying_rate':'940','Selling_rate':'1150'},
{'ProductID':'PD16','Name':'Walnut (Grade 1)','Buying_rate':'1200','Selling_rate':'1650'},
{'ProductID':'PD18','Name':'Dry Grapes','Buying_rate':'280','Selling_rate':'330'},
{'ProductID':'PD19','Name':'Amla candy','Buying_rate':'280','Selling_rate':'325'},
{'ProductID':'PD20','Name':'Dry Kiwi','Buying_rate':'520','Selling_rate':'600'},
{'ProductID':'PD21','Name':'Flax seeds','Buying_rate':'250','Selling_rate':'320'},
{'ProductID':'PD22','Name':'Pumpkin Seeds','Buying_rate':'250','Selling_rate':'350'},
{'ProductID':'PD23','Name':'Apricot  (200gmspack)','Buying_rate':'90','Selling_rate':'130'},
{'ProductID':'PD24','Name':'Elachi','Buying_rate':'2800','Selling_rate':'3600'},
{'ProductID':'PD25','Name':'Star Anise','Buying_rate':'600','Selling_rate':'1400'},
{'ProductID':'PD26','Name':'Clove','Buying_rate':'840','Selling_rate':'1240'},
{'ProductID':'PD27','Name':'Roll Cinnamon','Buying_rate':'1180','Selling_rate':'1800'},
{'ProductID':'PD28','Name':'Cinnamon Stick','Buying_rate':'350','Selling_rate':'750'},
{'ProductID':'PD29','Name':'Mace/Javithri','Buying_rate':'1800','Selling_rate':'2400'},
{'ProductID':'PD30','Name':'Black dates','Buying_rate':'280','Selling_rate':'340'},
{'ProductID':'PD31','Name':'Roja Gulkand(500gms)','Buying_rate':'60','Selling_rate':'80'},
{'ProductID':'PD32','Name':'Honey','Buying_rate':'500','Selling_rate':'640'}]

@app.route('/')
@app.route('/home',methods=["GET","POST"])
def index():
    return render_template('index.html',index=True)

@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/shop')
def shop():
    return render_template('shop.html',shop=True,products=products)

@app.route('/complete',methods=["GET","POST"])
def complete():
    ProductID = request.form['ProductID']
    Name = request.form['Name']
    Selling_rate = request.form['Selling_rate']
    return render_template('complete.html',data={"id":ProductID,"name":Name,"rate":Selling_rate})


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/api')
@app.route('/api/<pid>')
def api(pid=None):
    if pid == None:
        vdata = products
    else:
        vdata = products[int(pid)]

    return Response(json.dumps(vdata),mimetype="application/json")

if __name__ == '__main__':
    app.run()

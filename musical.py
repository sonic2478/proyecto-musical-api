from flask import Flask,render_template,url_for,request,redirect,flash
from flask_mysqldb import MySQL
from config import config 
from werkzeug.security import generate_password_hash
from models.ModelUser import ModelUser
from models.entities.User import User
from flask_login import LoginManager, login_user, logout_user
from flask_mail import Mail,Message
musicalApp = Flask(__name__)
musicalApp.config['MAIL_SERVER'] = 'smtp.gmail.com'
musicalApp.config['MAIL_PORT'] = 587
musicalApp.config['MAIL_USE_TLS'] = True
musicalApp.config['MAIL_USE_SSL'] = False
musicalApp.config['MAIL_USERNAME'] = 'alvarezmares24@gmail.com'
musicalApp.config['MAIL_PASSWORD'] = 'iqomquudxyhixryq'
musicalApp.config['MAIL_DEFAULT_SENDER'] = 'alvarezmares24@gmail.com'
musicalApp.config['MAIL_ASCII_ATTACHMENTS'] = True

db = MySQL(musicalApp)
LMmusical = LoginManager(musicalApp)
mail = Mail(musicalApp)

@LMmusical.user_loader
def loader_user(id):
    return ModelUser.get_by_id(db,id) 

@musicalApp.route('/')
def home():
    return render_template('home.html')

@musicalApp.route('/usuario',methods=['GET','POST'])
def usuario():
        return render_template('usuario.html')

@musicalApp.route('/admin')
def admin():
    return render_template('admin.html')

@musicalApp.route('/signin',methods=['GET','POST'])
def signin():
    if request.method == 'POST':
        regUsuario = db.connection.cursor()
        nombreu = request.form['nombreu']
        correou = request.form['correou']
        claveu = request.form['claveu']
        claveCifrada = generate_password_hash(claveu)
        regUsuario.execute("INSERT INTO usuario (nombreu,correou,claveu) VALUES (%s,%s,%s)",(nombreu,correou,claveCifrada))
        db.connection.commit()
        msg = Message(subject = 'Bienvenido a musicalApp',recipients=[correou])
        msg.html = render_template('user_mail.html', nombrem = nombreu)
        mail.send(msg)
        return redirect(url_for('home'))

    else:
        return render_template('home.html')
@musicalApp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = User(0,None,request.form['correou'],request.form['claveu'],None)
        usuarioAut = ModelUser.login(db,usuario)
        if usuarioAut is not None:
            if usuarioAut.claveu:
                login_user(usuarioAut)
                if usuarioAut.perfilu == 'A':
                    return render_template('admin.html')
                else:
                    SelCancion = db.connection.cursor()
                    SelCancion.execute("SELECT * FROM cancion")
                    c = SelCancion.fetchall()
                    return render_template('usuario.html', canciones = c)
            else:
                flash('No andes robando cuentas perro')
                return redirect(request.url)
        else:
            flash('Usuario inexistente')
            return redirect(request.url)
    else:
        return render_template('home.html')
    
@musicalApp.route('/logout', methods=['GET', 'POST'])
def logout():
        logout_user()
        return redirect(url_for('home'))

@musicalApp.route('/sUsuario', methods=['GET', 'POST'])
def sUsuario():
    SelUsuario = db.connection.cursor()
    SelUsuario.execute("SELECT * FROM usuario")
    u = SelUsuario.fetchall()
    return render_template('profiles.html', usuarios = u)

@musicalApp.route('/uUsuario/<string:id>', methods=['GET', 'POST'])
def uUsuario(id):
    if request.method == 'POST':
        UpUsuario = db.connection.cursor()
        nombreu = request.form['nombreu']
        correou = request.form['correou']
        claveu = request.form['claveu']
        claveCifrada = generate_password_hash(claveu)
        perfilu = request.form['perfilu']
        UpUsuario.execute("UPDATE usuario SET nombreu=%s, correou=%s, claveu=%s, perfilu=%s WHERE id=%s", (nombreu,correou,claveCifrada,perfilu,id))
        db.connection.commit()
        flash('USUARIO ACTUALIZADO')
        return redirect(url_for('sUsuario'))
    else:
        return redirect(request.url)
    
@musicalApp.route('/uUsuarioP/<string:id>', methods=['GET', 'POST'])
def uUsuarioP(id):
    if request.method == 'POST':
        UpUsuario = db.connection.cursor()
        usuario = User(0,None,request.form['correou'],request.form['claveu'],None)
        usuarioAut = ModelUser.login(db,usuario)
        nombreu = request.form['nombreu']
        correou = request.form['correou']
        claveu = request.form['claveu']
        claveCifrada = generate_password_hash(claveu)
        if usuarioAut is not None:
            if usuarioAut.claveu:
                login_user(usuarioAut)
                if usuarioAut.perfilu == 'A':
                    return render_template('admin.html')
                else:
                    SelCancion = db.connection.cursor()
                    SelCancion.execute("SELECT * FROM cancion")
                    c = SelCancion.fetchall()
                    UpUsuario.execute("UPDATE usuario SET nombreu=%s, correou=%s, claveu=%s WHERE id=%s", (nombreu,correou,claveCifrada,id))
                    db.connection.commit()
                    flash('USUARIO ACTUALIZADO')
                    return render_template('usuario.html', canciones = c)
            else:
                flash('No andes robando cuentas perro')
                return redirect(request.url)
        else:
            flash('Usuario inexistente')
            return redirect(request.url)
        
    else:
        return redirect(request.url)
    
@musicalApp.route('/dUsuario/<string:id>', methods=['GET', 'POST'])
def dUsuario(id):
        if request.method == 'POST':
            DelUsuario = db.connection.cursor()
            DelUsuario.execute("DELETE FROM usuario WHERE id=%s",(id,))
            db.connection.commit()
            flash('Usuario Eliminado')
            return redirect(url_for('sUsuario'))
        else:
            return redirect(request.url)
        
@musicalApp.route('/iUsuario',methods=['GET','POST'])
def iUsuario():
    if request.method == 'POST':
        regUsuario = db.connection.cursor()
        nombreu = request.form['nombreu']
        correou = request.form['correou']
        claveu = request.form['claveu']
        claveCifrada = generate_password_hash(claveu)
        perfilu = request.form['perfilu']
        regUsuario.execute("INSERT INTO usuario (nombreu,correou,claveu,perfilu) VALUES (%s,%s,%s,%s)",(nombreu,correou,claveCifrada,perfilu))
        db.connection.commit()
        flash('Usuario agregado')
        return redirect(url_for('sUsuario'))
    else:
        redirect(request.url)

@musicalApp.route('/sProducto', methods=['GET', 'POST'])
def sProducto():
    SelProducto = db.connection.cursor()
    SelProducto.execute("SELECT * FROM cancion")
    p = SelProducto.fetchall()
    return render_template('productos.html', productos = p)

@musicalApp.route('/uProducto/<string:idcancion>', methods=['GET', 'POST'])
def uProducto(idcancion):
    if request.method == 'POST':
        UpProducto = db.connection.cursor()
        nombrec = request.form['nombrec']
        artistac = request.form['artistac']
        albumc = request.form['albumc']
        fechac = request.form['fechac']
        generoc = request.form['generoc']
        nombreimg = request.form['nombreimg']
        fechareg = request.form['fechareg']
        urlc = request.form['urlc']
        UpProducto.execute("UPDATE cancion SET nombrec=%s, artistac=%s, albumc=%s, fechac=%s, generoc=%s, nombreimg=%s, fechareg=%s, urlc=%s WHERE idcancion=%s", (nombrec,artistac,albumc,fechac,generoc,nombreimg,fechareg,urlc,idcancion))
        db.connection.commit()
        flash('CANCIÓN ACTUALIZADA')
        return redirect(url_for('sProducto'))
    else:
        return redirect(request.url)
    
@musicalApp.route('/dProducto/<string:idcancion>', methods=['GET', 'POST'])
def dProducto(idcancion):
        if request.method == 'POST':
            DelCancion = db.connection.cursor()
            DelCancion.execute("DELETE FROM cancion WHERE idcancion=%s",(idcancion,))
            db.connection.commit()
            flash('Canción Eliminada')
            return redirect(url_for('sProducto')) 
        else:
            return redirect(request.url)
        
@musicalApp.route('/iProducto', methods=['GET', 'POST'])
def iProducto():
    if request.method == 'POST':
        RegProducto = db.connection.cursor()
        nombrec = request.form['nombrec']
        artistac = request.form['artistac']
        albumc = request.form['albumc']
        fechac = request.form['fechac']
        generoc = request.form['generoc']
        nombreimg = request.form['nombreimg']
        fechareg = request.form['fechareg']
        urlc = request.form['urlc']
        RegProducto.execute("INSERT INTO cancion (nombrec,artistac,albumc,fechac,generoc,nombreimg,fechareg,urlc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(nombrec,artistac,albumc,fechac,generoc,nombreimg,fechareg,urlc))
        db.connection.commit()
        flash('Canción agregada')
        return redirect(url_for('sProducto'))
    else:
        return redirect(request.url)




if __name__ == '__main__':
    musicalApp.config.from_object(config['development'])
    musicalApp.run(debug=True,port=3300)




from flask import Flask, render_template, request, Response, redirect, url_for, jsonify
import sqlite3
from dbman import getcats, getsubcats, maketask, get_all_tasks, deltaskbyid
app = Flask(__name__)


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

def stringify(what):
    input_string1 = str(what)
    translation_table = str.maketrans(
        "", "", "!@#$%^&*()_-+={}[]|\:;\"'<>,.?/`~")
    output_string1 = input_string1.translate(translation_table)
    print(output_string1)
    return output_string1




@app.route("/submit" , methods=['GET', 'POST'])
def submit():
    item = request.form.get('itemtoadd')
    prio = request.form.get('prio')
    cats = request.form.get('allcats')
    subs = request.form.get('subcats')
    maketask(cats, subs, item, prio)
    print('aintnowaythisran')
    print('profile made')
    return redirect(url_for('main'))


@app.route("/submitupd" , methods=['GET', 'POST'])
def submitupd():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    if request.form.get('makeacat'):
        catmake = request.form.get('makeacat')
        cur.execute("insert into todo (cat) VALUES (?)", (catmake,))
        con.commit()
        con.close() 
        print('catmade')
        return redirect(url_for('main'))
    else:
        con = sqlite3.connect("todo.db")
        item = request.form.get('makeaclass')
        cats = request.form.get('allcats')
        cur = con.cursor()
        cur.execute("insert into todo (cat, class) VALUES (?,?)", (cats, item))
        con.commit()
        con.close() 
        return redirect(url_for('main'))


#wait stop wiat a minute
#we select a dropdown and that triggers a function (get_dropmenfirst) wich updates the second one 
#(upddropmentwo)loops back to main sets second dropdown from function





@app.route('/get_subcats', methods=['POST'])
def get_subcats_endpoint():
    selected_cat = request.json.get('selected_cat')
    subcats = getsubcats(selected_cat)
    return jsonify({'subcats': subcats})



@app.route('/process_checkboxes', methods=['POST'])
def process_checkboxes():
    selected_tasks = request.form.getlist('task_ids')
    print(selected_tasks)
    if request.form.get('process') == 'delete':
        print('delete selected')
        deltaskbyid(selected_tasks)
    else:
        print('not deleting')
    
    # Redirect moment
    return redirect(url_for('main'))





@app.route('/', methods=['GET', 'POST'])
def main():
    allcats = getcats()
    tasks = get_all_tasks()

    return render_template('sign.html', allcats=allcats, tasks=tasks)



if __name__ == '__main__':
    
    Flask.run(app, debug=True,port=5001)

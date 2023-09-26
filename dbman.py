import sqlite3


#con = sqlite3.connect("db.db")
#cur = con.cursor()

def maketable():
    #forbidden
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    cur.execute("create table todo (id INTEGER PRIMARY KEY AUTOINCREMENT, cat, class, name, prio)")
    print('done')
    con.close()

#insert into todo (cat, class, name, prio) VALUES ('home', 'projects', 'todoapp', 1);



def stringify(what):
    input_string1 = str(what)
    translation_table = str.maketrans(
        "", "", "!@#$%^&*(_-+={}[]|\:;\"'<>,.?/`~")
    output_string1 = input_string1.translate(translation_table)
    
    return output_string1

def deltaskbyid(task_ids):
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    for task_id in task_ids:
        cur.execute("DELETE FROM todo WHERE id = ?", (task_id,))
    con.commit()
    con.close()

def maketask(cat, clas, name, prio):
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    print("not in use")
    cur.execute("insert into todo (cat, class, name, prio) VALUES (?,?,?,?)", (cat, clas, name, prio))
    con.commit()
    con.close()
    print('task made')
   
def get_all_tasks():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    tasks = cur.execute("SELECT id, cat, class, name, prio FROM todo WHERE cat IS NOT NULL AND class IS NOT NULL AND name IS NOT NULL AND prio IS NOT NULL ORDER BY name").fetchall()
    con.close()
    return tasks

        
def getcats():
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    cats = cur.execute("SELECT DISTINCT cat FROM todo")
    all_cats = [item[0] for item in cats.fetchall()]
    con.close()
    return all_cats

def getsubcats(cat):
    con = sqlite3.connect("todo.db")
    cur = con.cursor()
    subcats = cur.execute("SELECT DISTINCT class FROM todo where cat = ?", (cat,))
    all_subcats = [item[0] for item in subcats.fetchall()]
    con.close()
    return all_subcats
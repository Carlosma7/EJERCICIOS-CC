from invoke import task, run

# Tarea de crear y lanzar los procesos
@task 
def start(c):
	run("pm2 start app2.py --name fruits --interpreter python3 -i 3")

# Tarea de parar los procesos
@task 
def stop(c):
	run("pm2 stop fruits")

# Tarea de relanzar los procesos
@task 
def reload(c):
	run("pm2 reload fruits")

# Tarea de describir los procesos
@task 
def describe(c):
	run("pm2 describe fruits")

# Tarea de eliminar los procesos
@task
def delete(c):
	run("pm2 delete fruits")

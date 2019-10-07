# Desarrollo-Web-I
Repo de los proyectos

Comandos utiles de GIT:


branch - rama del repo master

    
    git config --global user.name <pongan su user>
    git config --global user.email <pongan su mail>


    git clone <repo>  ------ Clona el repositorio
    git clone <repo> <nombre>  ------ Clona el repositorio y le cambia el nombre al directorio
    git clone <repo> --branch <branch a clonar> ------ Clona rama del repositorio
    git pull ------ Nos trae los cambios del repo
    git remote -v ------ Nos dice a donde apunta nuestro repo

    git status ------ Estado del arbol de trabajo
    git branch ------ Nos dice en que branch estamos
    
    git branch <nombre> ------ Crea una nueva branch
    git checkout <branch> ------ Cambia de branch
    --------------------ATAJO --------------------
    git checkout -b <branch> ------ Crea y checkoutea al nuevo branch
    
    git checkout <archivo> ------ Desestima los cambios hechos en ese archivo
    git add <archivo> ------ Agregar archivo para registrar cambios
    git commit ------ Hace un commit de nuestros cambios
    --------------------ATAJO --------------------
    git commit -m "Aca va nuestro mensaje para el commit"
    git diff ------ Nos muestra los cambios
    git push origin:<nombre-branch> ------ Manda los cambios comiteados al branch BATMAN


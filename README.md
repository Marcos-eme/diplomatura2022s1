# diplomatura2022s1
- inventory.yaml
  Editar ip en ansible_host y colocar el ip del nodo destino. Tener en cuenta que se debe agregar la ssh key del control-node al authorized keys del managed-node con "ssh -copy-id user@host"
- configurar-docker.yaml
  En caso de que sea necesario, se puede instalar docker en el managed node con este playbook. Para eso correr: 
  ansible-playbook -i inventory.yaml configurar-docker.yaml 
- playbook.yaml
  ansible-playbook -i inventory.yaml playbook.yaml 
  Dentro de las variables tiene definido nombre a setear al nuevo contenedor que se creará, repositorio de donde va a buscar la imagen y la version de la respectiva imagen.
  El playbook realiza las siguientes tareas: 
  Tasks: 
    - Correr imagen desde docker hub. Con docker run hace un pull y ejecuta un contenedor con el nombre seteado en las variables y guarda el output del contenedor en una variable.
    - Imprimi el resultado del contenedor ejecutado. En este caso se vera los estipulado en la consigna para el script python
    - Se listan los contenedores creados 
    - Se borra el contenedor que se creo previamente.
    

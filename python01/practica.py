# platform.system()

# Esta función devuelve una cadena que muestra el nombre del sistema operativo en el dispositivo actual que se utiliza para ejecutar el programa.
# Example 7: Displaying the OS name

# import module
import platform
  
# displaying OS name
print('Operating system:', platform.system())


# platform.python_version()
# Esta función devuelve una cadena que muestra la versión de Python que se está ejecutando actualmente en el sistema. La versión de python se devuelve de la siguiente manera:

# 'major.minor.patchlevel'
# Example 13: Displaying the python version


# Python program to display python version
  
# import module
import platform
  
# displaying python version
print('Python version:', platform.python_version())


# # El método platform.version() devuelve la versión de lanzamiento del sistema operativo subyacente (encubierto). Este método devuelve una cadena vacía si no puede determinar la versión del sistema operativo.

# # import module
# import platform

# displaying version
print("platform.version() = %s" % (platform.version()))




















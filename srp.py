
#Principio de responsabilidad única

# - Una clase debe tener una sola razón para cambiar
# - No debe cargarse con múltiples responsabilidades y una sola responsabilidad no
#   debe distribuirse entre varias clases ni mezclarse con otras responsabilidades.
# - La razón es que cuantos más cambios se soliciten en el futuro, más cambios 
#   tendrá que aplicar la clase.

class Journal:
    """
    Solo debe tener la responsabilidad de interactuar con los texto que interactuan en la clase.
    Agregar y borrar.
    """
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # ¡WARNING! : estos métodos sobran en la clase caen en otra responsabilidad de la clase
    #             que corresponde a guardar los textos.

    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


#Mejor práctica : El proceso de guardado debe ir en una clase con una única responsabilidad.
class PersistenceManager:
    @staticmethod
    def save_to_file(j, file):
        file = open(file, "w")
        file.write(str(j))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
j.add_entry("Hola mundo!")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'C:\\Users\\cflorelu\\Documents\\1_Ternium\\Design-Patterns-in-Python\\data\\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())

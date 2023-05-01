frases = ['A molecule is made up of atoms', "A simple molecule can have two atoms",
          "The structure of a molecule can be very complex",
          "A large molecule may consist of thousands of atoms",
          'A molecule is the smallest unit of a chemical compound that still retains its chemical properties',
          'The structure of a molecule can be very complex and can determine its properties and behavior',
          'Water molecules are made up of two hydrogen atoms and one oxygen atom',
          'In organic chemistry molecules often contain carbon atoms bonded together in a chain',
          'Analyzing the behavior of molecules is an important part of physical chemistry research',
          'Scientists can use computational simulations to study large molecules that are too complex to analyze experimentally',
          'The pharmacological properties of a drug can depend on the size and structure of the molecule',
          'Molecules can form unique shapes and configurations that allow them to serve specific biological functions',
          'A molecule is a group of two or more atoms that are chemically bonded together',
          'Molecules are the basic building blocks of all living things on Earth']

def create_phrases():
    global frases
    res = []
    for i in range(len(frases)):
        tmp = frases[i].replace(" ", '')
        res.append(tmp.upper())
    return res

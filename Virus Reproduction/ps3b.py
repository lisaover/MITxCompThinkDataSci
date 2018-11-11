# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab

random.seed(0)

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        
        prob = random.random()
        if prob < self.getClearProb():
            return True
        else:
            return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        
        try:
            prob = random.random()
        
            if (self.getMaxBirthProb() == 0.0):
                replicate = False
            elif (self.getMaxBirthProb() == 1.0) and (popDensity < 1):
                replicate = True 
            elif (prob < (self.getMaxBirthProb()*(1-popDensity))) and (popDensity < 1):
                replicate = True
            else:
                replicate = False
            
            if replicate == True:
                new_virus = SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
            
            if not replicate:
                raise NoChildException(None)
                
        except (NameError, ValueError, TypeError, ZeroDivisionError, AttributeError):
            raise NoChildException(None)
        except NoChildException:
            pass
        else:
            return new_virus
        

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)        


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        if self.viruses:
            controller = SimpleVirus(self.viruses[0].maxBirthProb, self.viruses[0].clearProb)
            
        # for each virus, check if it clears
        total = self.getTotalPop()
        deaths = 0
        
        for i in range(total):
            if controller.doesClear():
                deaths += 1
        for j in range(deaths):
            self.viruses.pop()
        
        # calculate the current population density
        if self.getMaxPop() > 0:
            popDensity = self.getTotalPop()/self.getMaxPop()
        else:
            popDensity = 1
        
        # for each virus, check if the virus reproduces
        total = self.getTotalPop()
        births = []
        if self.viruses:
            for i in range(total):
                newVirus = SimpleVirus.reproduce(controller, popDensity)
                if newVirus == None:
                    pass
                else:
                    births.append(newVirus)           
        for birth in births:
            self.viruses.append(birth)
                
        return len(self.viruses)

'''
v1 = SimpleVirus(0.96, 0.02)
viruses = [v1]
for i in range(20):
    viruses.append(v1.reproduce(0.0))
print(viruses)
'''
'''
print('always reproduce, always clear')
virus = SimpleVirus(1.0, 1.0) # always reproduce, always clear (answer is 0)
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print(patient.getTotalPop())

print('always reproduce, never clear')
virus = SimpleVirus(1.0, 0.0) # always reproduce, never clear
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print(patient.getTotalPop())

print('never reproduce, never clear')
virus = SimpleVirus(0.0, 0.0)
patient = Patient([virus], 100) # never reproduce, never clear (answer is 1)
for i in range(100):
    patient.update()
print(patient.getTotalPop())

print('never reproduce, always clear')
virus = SimpleVirus(0.0, 1.0) # never reproduce, always clear (answer is 0)
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print(patient.getTotalPop())
'''

#
# PROBLEM 2
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    # create and populate variables to store step and population info
    pop_record = []
    #timesteps = []
    for n in range(300):
        #timesteps.append(k)
        pop_record.append(0)

    for i in range(numTrials):
        
        # create viruses list
        viruses = []
        for j in range(numViruses):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        # create patient with viruses
        patient = Patient(viruses, maxPop)
        
        # run simulation for 300 timesteps
        for k in range(300):
            pop_record[k] = pop_record[k] + patient.update()

    # average each element in pop_record
    pop_record[:] = [x/numTrials for x in pop_record]
    
    pylab.plot(pop_record, label = "SimpleVirus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc = "best")        
            
    return pylab.show()

#simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)

#
# PROBLEM 3
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        if drug not in self.getResistances():
            return False
        else:
            return self.getResistances()[drug]


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        
        try:
            from copy import deepcopy
            # set a flag to track reproduction status based on resistance
            resist = True

            for drug in activeDrugs:
                if (drug not in self.getResistances()) or (self.getResistances()[drug] == False):
                    resist = False 
            
            # create a new resistances dictionary for offspring
            drug_resistances = deepcopy(self.getResistances())
            # if prob < mutProb for a given drug then switch the resistance
            # that is, if True make False and vice versa
            for drug in drug_resistances:
                if self.getMutProb == 0.0:
                    pass
                elif self.getMutProb == 1.0:
                    drug_resistances[drug] = not drug_resistances[drug]
                else:
                    # draw random number to compare to mutProb
                    prob = random.random()
                    if prob < self.getMutProb():
                        drug_resistances[drug] = not drug_resistances[drug]           

            if resist:
                prob = random.random()
                if (self.getMaxBirthProb() == 0.0):
                    replicate = False
                elif (self.getMaxBirthProb() == 1.0) and (popDensity < 1):
                    replicate = True 
                elif (prob < (self.getMaxBirthProb()*(1-popDensity))) and (popDensity < 1):
                    replicate = True
                else:
                    replicate = False
            
                if replicate == True:
                    new_virus = ResistantVirus(self.maxBirthProb, self.clearProb, drug_resistances, self.mutProb)
            
                if not replicate:
                    raise NoChildException(None)
            else:
                raise NoChildException(None)
                
        except (NameError, ValueError, TypeError, ZeroDivisionError, AttributeError):
            raise NoChildException(None)
        except NoChildException:
            pass
        else:
            return new_virus
'''
maxBirthProb = 1.0
clearProb = 0.0
resistances = {'Drug1': False, 'Drug2': True, 'Drug3': False ,'Drug4': True}
mutProb = 0.9
popDensity = 0.4
activeDrugs = ['Drug2','Drug4']
v = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
print(v.reproduce(popDensity, activeDrugs))
'''

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        Patient.__init__(self, viruses, maxPop)
        self.activeDrugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.activeDrugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = len(self.viruses)
        for virus in self.getViruses():   
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    count -= 1
                    break
        return count

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        # for each virus, check if it clears
        total = self.getTotalPop()
        deaths = 0
        
        for i in range(total):
            if self.viruses[i].doesClear():
                deaths += 1
        for j in range(deaths):
            self.viruses.pop()
        
        # calculate the current population density
        if self.getMaxPop() > 0:
            popDensity = self.getTotalPop()/self.getMaxPop()
        else:
            popDensity = 1
        
        # for each virus, check if the virus reproduces
        total = self.getTotalPop()
        births = []
        if self.viruses:
            for i in range(total):
                newVirus = self.viruses[i].reproduce(popDensity, self.getPrescriptions())
                if newVirus == None:
                    pass
                else:
                    births.append(newVirus)           
        for birth in births:
            self.viruses.append(birth)
                
        return len(self.viruses)

'''
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False}, 0.0)
patient = TreatedPatient([virus1, virus2], 1000000)
patient.addPrescription("drug1")
for i in range(5):
    patient.update()
print(patient.getTotalPop())
print(patient.getResistPop(["drug1"]))
# above results in resistant viruses being 1 less than total population
'''
'''
virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)
print(patient.getResistPop(['drug1'])) # 2
print(patient.getResistPop(['drug2'])) # 2
print(patient.getResistPop(['drug1','drug2'])) # 1
print(patient.getResistPop(['drug3'])) # 0
print(patient.getResistPop(['drug1', 'drug3'])) # 0
print(patient.getResistPop(['drug1','drug2', 'drug3'])) # 0
'''

'''
resistances = {'Drug1': False, 'Drug2': True, 'Drug3': False ,'Drug4': True}

print('always reproduce, always clear')
virus = ResistantVirus(1.0, 1.0, resistances, .95) # always reproduce, always clear (answer is 0)
patient = TreatedPatient([virus], 100)
patient.addPrescription('Drug4')
for i in range(10):
    patient.update()
print(patient.getTotalPop())

print('always reproduce, never clear')
virus = ResistantVirus(1.0, 0.0, resistances, .95)  # always reproduce, never clear
patient = TreatedPatient([virus], 100)
patient.addPrescription('Drug4')
for i in range(10):
    patient.update()
print(patient.getTotalPop())

print('never reproduce, never clear')
virus = ResistantVirus(0.0, 0.0, resistances, .95) # never reproduce, never clear (answer is 1)
patient = TreatedPatient([virus], 100) 
patient.addPrescription('Drug4')
for i in range(10):
    patient.update()
print(patient.getTotalPop())

print('never reproduce, always clear')
virus = ResistantVirus(0.0, 1.0, resistances, .95) # never reproduce, always clear (answer is 0)
patient = TreatedPatient([virus], 100)
patient.addPrescription('Drug4')
for i in range(10):
    patient.update()
print(patient.getTotalPop())
'''

#
# PROBLEM 4
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    # create and populate variables to store population and 
    # resistant population info
    pop_record = []
    resist_record = []
    for n in range(300):
        pop_record.append(0)
        resist_record.append(0)

    for i in range(numTrials):
        
        # create viruses list
        viruses = []
        for j in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        # create patient with viruses
        patient = TreatedPatient(viruses, maxPop)
        
        # run simulation for 150 timesteps without the drug
        for k in range(150):
            pop_record[k] = pop_record[k] + patient.update()
            resist_record[k] = resist_record[k] + patient.getResistPop(['guttagonol'])
            
        # run simulation for 150 timesteps with the drug
        patient.addPrescription('guttagonol')
        for r in range(150, 300):
            pop_record[r] = pop_record[r] + patient.update()
            resist_record[r] = resist_record[r] + patient.getResistPop(['guttagonol'])

    # average each element in pop_record
    pop_record[:] = [x1/numTrials for x1 in pop_record]
    resist_record[:] = [x2/numTrials for x2 in resist_record]
    #print(pop_record)
    #print(resist_record)
    
    pylab.plot(pop_record, label = "Avg Total Virus Population")
    pylab.plot(resist_record, label = "Avg Guttagonol-resistant Virus Population")
    pylab.title("ResistantVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Population")
    pylab.legend(loc = "best")        
            
    return pylab.show()

viruses = []

maxBirthProb = 0.1
clearProb = 0.05
resistances = {'guttagonol': False}
mutProb = 0.005
numTrials = 100
numViruses = 100
maxPop = 1000

'''
simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                      mutProb, numTrials)
'''
'''
simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)
simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)
simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
'''

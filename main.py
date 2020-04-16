from ShortestPath.Main import Main
import random
from builtins import staticmethod



#filename = "input_easy.txt"
#filename = "input_med.txt"
filename = "input_hard.txt"
main = Main(filename)
main.citireDate()


GRAF = main.g
DIM_POPULATIE = main.g.getNrNoduri()
##TARGET = main.drumMinim().get_l()

CROMOZOMI_CASTIGATORI = 1
TOURNAMENT_SELECTION_SIZE = 3

RATA_MUTATIE = 0.25

class Cromozom:
    ''''''
    def __init__(self):
        self.__individ = [];
        
        
        for i in range(1,DIM_POPULATIE +1):
            self.__individ.append(i);
        
        random.shuffle(self.__individ)
        
    def set_individ(self,list):
        self.__individ = list    
            
    def get_individ(self):
        return self.__individ
    
    
    def get_fitness(self):
        fitness = 0;
        for i in range(0,len(self.__individ)-1):
            dist = GRAF.get_distanta(self.__individ[i],self.__individ[i+1])
            fitness = fitness + dist
        
        
        dist = GRAF.get_distanta(self.__individ[-1],self.__individ[0])
        fitness +=dist
        
        return fitness
    
    def __str__(self):
        string = "[";
        for i in self.__individ:
            string += str(i) + " , "
        
        string += str(self.__individ[0]) + "]"
        return string
    
    
    
class Populatie:
    def __init__(self,size):
        
        self.__cromozomi = [];
        for i in range(size):
            self.__cromozomi.append(Cromozom())
        
    
    def get_cromozomi(self): 
        self.__cromozomi.sort(key=lambda x: x.get_fitness(), reverse=False)
        return self.__cromozomi
    
    

class AlgEvolutiv:
    ''''''
    
 
    
    @staticmethod
    def evolve_population(populatie):
        return AlgEvolutiv.mutate_population(AlgEvolutiv.crossover_population(populatie))
    
    @staticmethod
    def crossover_population(populatie):
        crossoverPopulation = Populatie(0)
        
        for i in range(CROMOZOMI_CASTIGATORI):
            crossoverPopulation.get_cromozomi().append(populatie.get_cromozomi()[i])
        
        i = CROMOZOMI_CASTIGATORI
        while i < DIM_POPULATIE:
            cromozom1 = AlgEvolutiv.select_tournament_population(populatie).get_cromozomi()[0]
            cromozom2 = AlgEvolutiv.select_tournament_population(populatie).get_cromozomi()[0]
            crossoverPopulation.get_cromozomi().append(AlgEvolutiv.crossover_chromosomes(cromozom1, cromozom2));
            i+=1
        
        return crossoverPopulation
    
    @staticmethod
    def mutate_population(populatie):
        for i in range(CROMOZOMI_CASTIGATORI,DIM_POPULATIE):
            AlgEvolutiv.mutate_chromosomes(populatie.get_cromozomi()[i])
            
        return populatie
        
    @staticmethod
    def crossover_chromosomes(cromozom1,cromozom2):
        cromozom_rez = Cromozom()
        
        lista_perm = [0] * DIM_POPULATIE
        
        start = random.randint(0,DIM_POPULATIE-1)
        stop = random.randint(0,DIM_POPULATIE-1)
        
        if start == stop:
            return cromozom1
        
        if start > stop:
            aux = start
            start = stop
            stop = aux
            
        while start <= stop:
            lista_perm[start] = cromozom1.get_individ()[start]
            start+=1
        
        
        i1 = stop+1
        i2 = stop+1
        
        while 0 in lista_perm:
            if i1 == DIM_POPULATIE:
                i1 = 0
            
            if i2 == DIM_POPULATIE:
                i2 = 0
                
            if cromozom2.get_individ()[i2] in lista_perm:
                i2 +=1
            else:
                lista_perm[i1] = cromozom2.get_individ()[i2]
                i1+=1
                i2+=1
        
        
        cromozom_rez.set_individ(lista_perm)
        return cromozom_rez
    
    @staticmethod
    def mutate_chromosomes(cromozom):
        for i in range(DIM_POPULATIE):
            if random.random() < RATA_MUTATIE:
                ind1 = random.randint(0,DIM_POPULATIE-1)
                ind2 = random.randint(0,DIM_POPULATIE-1)
                
                aux = cromozom.get_individ()[ind1]
                cromozom.get_individ()[ind1] = cromozom.get_individ()[ind2]
                cromozom.get_individ()[ind2] = aux
                    
                return
            
        
    @staticmethod
    def select_tournament_population(pop):
        tournament_pop = Populatie(0)
        
        for i in range(TOURNAMENT_SELECTION_SIZE):
            size = len(pop.get_cromozomi())
            tournament_pop.get_cromozomi().append(pop.get_cromozomi()[random.randint(0,size-1)])
            
        
        
        return tournament_pop
        
    
    
    def __init__(self,nrGeneratii):
        populatie = Populatie(8);

        gen = 0
        print_populatie(populatie, gen)
        
        while gen < nrGeneratii:
            
            populatie = AlgEvolutiv.evolve_population(populatie)
            gen+=1
            print_populatie(populatie, gen)


def print_populatie(pop,gen_nr):
    print("\n.........................")
    print("Generation " + str(gen_nr))
    print("...........................")
    i = 0
    for x in pop.get_cromozomi():
        print("Cromozomul " + str(i) + " : " + x.__str__() + " ; FITNESS = " + str(x.get_fitness()))
        i +=1
    
    
        

start = AlgEvolutiv(10)


    



    
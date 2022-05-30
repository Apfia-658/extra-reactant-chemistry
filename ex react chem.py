beaker = 83.01 #input mass of beaker
total_beaker = 90.27 #input mass of beaker and siver nitrate
masschem_one = round(total_beaker - beaker, 3) #calculates mass of chem one, rounds to 3 decimals
print ("mass of chem 1= " + str(masschem_one) + " grams")

molmasschem_one = 169.8731
molchem_one = round(masschem_one / molmasschem_one, 3) #calculates mols chem one, rounds to 3 decimals
print ("mols of chem 1= " + str(molchem_one) + " mols")

mass_soln = 165.59 #input mass of solution
masssolnchem_two = 172.93 #input mass of solution + chem 2
masschem_two = round(masssolnchem_two - mass_soln, 3) #calculates mass of chem 2, rounds to 3 decimals
print("mass of chem 2= " + str(masschem_two) + " grams")

molmasschem_two = 63.546
molchem_two = round(masschem_two / molmasschem_two, 3)
print ("mols of chem 2= " + str(molchem_two) + " mols")  #calculates mols of chem 2, rounds to 3 decimals

x= 2 #input ratio of moles
y= 1
molchem_one_req = round((molchem_two * x) / y , 3) #calculates mols of AgNO3 needed to react completely with copper
print(str(molchem_one_req)+ " mols of chem one required") 

if molchem_one - molchem_one_req == 0:
    print("Stoichiometric mixture")
elif molchem_one - molchem_one_req > 0:
    print("chem 1 is the excess reactant")
    print("chem 2 is the limiting reactant")
    excess_reactant= round(molchem_one - molchem_one_req, 3)
    print(str(excess_reactant)+ " mols of chem 1 left over")
    x=2 #input mole ratio
    molschem_one_produced = molchem_two* 2
    print(str(molschem_one_produced) + " mols of chem 2")
elif molchem_one - molchem_one_req < 0:
    print("chem 2 is the excess reactant")
    print("chem 1 is the limiting reactant")
    x=2 #input mole ratio
    molchem_two_req = round(molchem_one/2, 3)
    excess_reactant = round(molchem_two - molchem_two_req, 3) 
    print(str(excess_reactant) + " mols of chem 2 left over")


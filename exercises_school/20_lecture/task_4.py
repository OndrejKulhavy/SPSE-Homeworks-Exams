import numpy as np

brute_force = np.array([1, 2, 3, 0.1932, 1.1247, 2.2435, 2243, 2124, 2143])
print(brute_force.shape)

brute_1 = brute_force.reshape(3, 3)
print(brute_1)

velikost, spotreba_cas, spotreba_pamet = np.array_split(brute_force, 3)
print(velikost, spotreba_cas, spotreba_pamet)

brute_4 = np.concatenate([velikost, spotreba_cas, spotreba_pamet])
print(brute_4)

 #spojeni po ose 1
vysledek = np.stack((velikost, spotreba_cas, spotreba_pamet), axis=1)

 #vertikalni spojeni, po sloupcich
vysledek = np.vstack((velikost, spotreba_cas, spotreba_pamet))

#horizontalni spojeni, po radcich
vysledek = np.hstack((velikost, spotreba_cas, spotreba_pamet))

#spojeni do hloubky, po rozmerech
vysledek = np.dstack((velikost, spotreba_cas, spotreba_pamet))


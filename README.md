# Q-hackers
Given the current COVID-19 public health crisis that has affected humans worldwide, we sought to model the spread of infection via random simulation of a form of
Brownian motion, where people, simulated as dots, move through a crowded area past one another. If an uninfected person passes within a fixed distance of an
infected person (in COVID's case, this distance could be the CDC-recommended threshold distance of 6 feet) the uninfected person is subject to a nonzero
probability of infection, acquiring the disease randomly. While classical computers can simulate this randomness with pseudo-random techniques, their deterministic
approach to computation does not allow them to truly generate random simulations in a way that is authentic to the real world, and this is where our quantum
approach comes in. We use a fixed probability of infection (10% in the model provided here) to rotate a person's corresponding "infection vector" from |psi> = |0> 
(no infection) to |psi> = c1 |0> + c2 |1> where |c2|^2 represents the probability of infection. We then measure this pure state to be either |0> or |1> with their
corresponding appropriate proabilities of non-infection or infection with genuine randomness, updating their infection status via a color change in the animated
model (black = not infected, red = infected). In the future, we hope to expand this to more complex models of random infection, beyond the simple binomially 
distributed infection variable employed here to more complex models of propagation studied in modern epidemiology. 

Welcome to Gossa!
=================

We say it //g-uh-s-s-ah//, as in the animal fossa but with a "g". It stands for GUSA, or Global Uncertainty and Sensitivity Analysis.

Although it is likely that the intent of this code will soon diverge from that, we would like the name to stick.

Design
------

One upon a time, there were *models* and *modellers*, *solvers* and *kernels*:
 * models are the math, you write them a you wish
 * modellers wrap models according to a standard interface
   * to begin these will be explicit NLAs, but the abstractions will grow
 * solvers can solve a system of equations, they implement a numerical method
   * to begin with, these will just "evaluate", as that's all there is for an explicit NLA
 * kernels combine modellers and solvers

In the future there shall be *problems*... and much more.
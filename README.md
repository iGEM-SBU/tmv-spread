Stony Brook iGEM 2019
----------------------
Agent-based model for the spread of Tobacco Mosaic Virus (TMV)

##Requirements:
1. NetLogo 6.x
2. Python 3.7
3. NumPy 1.17.x
4. SciPy 1.3.x

##How to use:
###If you do not have Python, NumPy and SciPy installed:
  1. Open tmv_spread.nlogo with NetLogo.
  2. Go to the Interface tab.
  3. Select the number of initial infection sites with the slider.
  4. Click "Setup" and wait until the model loads.
  5. Click "Go" to run the model. The speed can be changed with the slider on the top.
  IMPORTANT: points.txt and links.txt must be in the same folder as tmv_spread.nlogo.

###If you do have Python, NumPy and SciPy installed:
  1. Run generate_points.py.
  2. Input the number of cells. This will randomly generate points.txt and links.txt.
  3. Follow the same procedures as above.

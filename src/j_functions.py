import matplotlib.pyplot
import numpy as np

def bargraph(Categories, expences):
        matplotlib.pyplot.bar(Categories, expences)
        matplotlib.pyplot.title('Expenses per categories')
        matplotlib.pyplot.xlabel('Catagories')
        matplotlib.pyplot.ylabel('Expences')
        matplotlib.pyplot.show()

def piegraph(InputCats,inputexpences):
        fig = matplotlib.pyplot.figure(figsize=(10, 8))
        matplotlib.pyplot.pie(inputexpences, labels=InputCats)

        # show plot
        matplotlib.pyplot.show()


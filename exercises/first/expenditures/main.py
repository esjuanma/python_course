import functions
import helpers

# Asks
data = functions.askForExpenditures()
functions.printData(data)

functions.save(helpers.getMonth())

# functions.read(helpers.getMonth())
from instance import Instance

#* Create example classes for testing
class DataModel(Instance): pass
class Workspace(Instance): pass
class Part(Instance): pass
class Model(Instance): pass

from represent import represent

game = DataModel()
workspace = Workspace(); workspace.Parent = game

#* Create a Model that contains 3 Parts
model1 = Model(); model1.Parent = workspace
for i in range(3): Part().Parent = model1

#* Create a Model that contains 6 Parts
model2 = Model(); model2.Parent = workspace
for i in range(6): Part().Parent = model2

#* Reparent model2 to model1
model2.Parent = model1

#* Print every Instances as a tree
represent(game)
# Find Degrees of Freedom of a Robot using Grϋbler's Formula
# dof - m * (N - 1 -J) + J ∑ (i=1) f(i)

# m   -   degrees of freedom of a rigid body (m = 3 for planar) and (m=6 for spatial)
# J   -   Number of Joints
# N   -   Links (including ground)
# fi  -   Number of freedom provided by Joint (i)

class GrublersFormula:
    def __init__(self):
        self.m :int = 0
        self.J :int = 0
        self.N :int = 0
        self.fi :int = 0

        self.sigma_list :list = []
        self.dof :int = 0


    # get user inputs
    def get_userInput(self):
        try:
            self.m = int(input("M: "))
            self.J = int(input("J: "))
            self.N = int(input("N: "))
            self.fi = int(input("fi: "))

        except ValueError:
            print("Please enter a valid number!")
            GrublersFormula.get_userInput(self)


    def find_DegreesOfFreedom(self):
        for i in range(self.J):
            self.sigma_list.append(self.fi)
            i+=1

        self.dof = self.m * (self.N - 1 - self.J) + sum(self.sigma_list)
        return self.dof


formula = GrublersFormula()
formula.get_userInput()
print(f"Degrees of Freedom: {formula.find_DegreesOfFreedom()}")
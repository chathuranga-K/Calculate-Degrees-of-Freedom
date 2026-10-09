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
        self.bodyType:str = ""
        self.jointType:str = ""

        self.dof: int = 0
        self.sigma_list :list = []
        self.jointTypes :dict = {}
        self.diagram_list :dict = {}



    # get user inputs
    def get_userInput(self):
        while True:
            try:
                #self.m = int(input("M: "))
                self.J = int(input("J: "))
                self.N = int(input("N: "))
                self.fi = int(input("fi: "))
                break

            except ValueError: print("Please enter a valid number!")
            continue # continue to the main loop

        while True:
            try:
                self.bodyType = str(input("Type of Rigid Body: ")).lower().strip()

                # Assign value of 'm' according to bodyType
                if self.bodyType in 'planar' and self.bodyType[0] == 'p':
                    self.m = 3
                elif self.bodyType in 'spatial' and self.bodyType[0] == 's':
                    self.m = 6
                else:
                    print("Please enter a valid bodyType!")
                    continue
            except ValueError,IndexError:
                print("Please enter a valid bodyType!")
                continue
            break # break the main loop


    def Diagram_DegreesOfFreedom(self):
        # Assign Joint Types
        self.jointTypes = {
            "R" :   "Revolute",
            "P" :   "Prismatic",
            "H" :   "Helical",
            "C" :   "Cylindrical",
            "U" :   "Universal",
            "S" :   "Spherical"
        }

        # Assign D
        self.diagram_list[self.jointTypes] = {
            "value_f"       : 0,
            "Planar_body"   : 0,
            "Spatial_body"  : 0
        }


    def find_DegreesOfFreedom(self):
        for i in range(self.J):
            self.sigma_list.append(self.fi)
            i+=1

        self.dof = self.m * (self.N - 1 - self.J) + sum(self.sigma_list)
        return self.dof


formula = GrublersFormula()
formula.get_userInput()
print(f"Degrees of Freedom: {formula.find_DegreesOfFreedom()}")
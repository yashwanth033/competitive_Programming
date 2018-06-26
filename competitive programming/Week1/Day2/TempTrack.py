class TempTrack:

    def __init__(self):
        self.temps = [0] * 111
        self.num_temps = 0
        self.min = 111
        self.max = -1
        self.total = 0
        self.mean = None
        self.max_freq = 0
        self.mode = []

    def insert(self, temp):
        if temp < 0 or temp > 110:
            raise Exception
        self.temps[temp] += 1
        self.num_temps += 1
        if temp < self.min:
            self.min = temp
        if temp > self.max:
            self.max = temp
        self.total += temp
        self.mean = self.total / float(self.num_temps)
        if self.temps[temp] > self.max_freq:
            self.max_freq = self.temps[temp]
            self.mode = [temp]
        elif self.temps[temp] == self.max_freq:
            self.mode.append(temp)

    def get_max(self):
        if self.max == -1:
            return None
        return self.max

    def get_min(self):
        if self.min == 111:
            return None
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

if __name__ == '__main__':

    newtemp = TempTrack()
    while(1):
        inpt = input()
        if(inpt=="exit"):
            break
        else:
            inpt = int(inpt)
            newtemp.insert(inpt)
            print("Max: "+ str(newtemp.get_max()) + "\n")
            print("Min: " + str(newtemp.get_min()) + "\n")
            print("Mean: " + str(newtemp.get_mean()) + "\n")
            print("Mode: " + str(newtemp.get_mode()) + "\n")
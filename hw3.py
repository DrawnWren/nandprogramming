""" Basic template file that you should fill in for Problem Set 3. Some util
functions are provided from the NAND notebooks online that implement some
of the NAND essentials. """
from util import EVAL
from util import TRUTH
from util import NANDProgram

# TODO: Implement this function and return a string representation of its NAND
# implementation. You don't have to use the class we supplied - you could use
# other methods of building up your NAND program from scratch.
def nandsquare(n):
    '''Takes in an integer n. Outputs the string representation of a NAND prog
    that takes in inputs x_0, ..., x_{n-1} and squares it mod 2^n. The output
    will be y_0, ..., y_{n-1}. The first digit will be the least significant
    digit (ex: 110001 --> 35)'''
    # creates a blank NAND program with n inputs and n outputs.
    prog = NANDProgram(n, n)
    # now add lines to your NAND program by calling python functions like
    # prog.NAND() or prog.OR() or other helper functions. For an example, take
    # a look at the stuff after if __name__ == '__main__':

    # "compiles" your completed program as a NAND program string.
    return str(prog)

def rightshift(n):
    '''Returns a program that takes [x_0,...x_n] as inputs and returns [0,...,x_n-1]  '''

# TODO: Do this for bonus points and the leaderboard.
def nandsquare256():
    '''Implement nandsquare for a specific input size, n=256. This result gets
    placed on the leaderboard for extra credit. If you get close to the top
    score on the leaderboard, you'll still recieve BONUS POINTS!!!'''
    raise NotImplementedError


def badadder(N):
    '''Should create a NAND adder that takes two n digits and outputs an n digit
    because it's bad'''
    return

# Examples of using the NANDProgram class to build NAND Programs. Please don't
# worry too much about the details of using this class - this is not a class
# about designing NAND programs.
def nandadder(N):
    '''Creates a NAND adder that takes in two n-digit binary numbers and gets
    the sum, returning a n+1-digit binary number. Returns the string repr. of
    the NAND program created.'''
    nand = NANDProgram(2 * N, N + 1, debug=False) #set debug=True to show debug lines
    nand.ONE("ONE")

    carry = nand.allocate()
    nand.ADD_3(nand.output_var(0), carry,
               nand.input_var(0), nand.input_var(N), nand.NAND("ZERO", "ONE", "ONE"), debug=True)

    last_carry = ""
    for i in range(1, N - 1):
        last_carry = carry
        carry = nand.allocate()
        nand.ADD_3(nand.output_var(i), carry,
                   nand.input_var(i), nand.input_var(N + i), last_carry, debug=True)

    nand.ADD_3(nand.output_var(N-1), nand.output_var(N),
               nand.input_var(N-1), nand.input_var(2 * N - 1), carry, debug=True)
    return str(nand)


if __name__ == '__main__':
    # Generate the string representation of a NAND prog. that adds numbers
    addfive = str(nandadder(10))
    # Input Number 1: 11110 --> 15
    # Input Number 2: 10110 --> 13   1111010110
    # Expected Output: 28 --> 001110


    #816 0000110011
    #877 1011011011
    #  10111001011
    print(EVAL(addfive,'00001100111011011011'))

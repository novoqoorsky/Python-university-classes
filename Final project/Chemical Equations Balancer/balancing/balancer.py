from computing.matrix_computer import MatrixComputer
from computing.matrix_creator import MatrixCreator
from chembal_logging.logger import Logger
from parsing.equation_parser import EquationParser


class Balancer:

    def __init__(self, logging=True):
        self.matrix_creator = MatrixCreator()
        self.matrix_computer = MatrixComputer()
        self.equation_parser = EquationParser()
        self.logging = logging
        if logging:
            self.logger = Logger()
        else:
            self.logger = Logger(active=False)

    def balance_equation(self, equation):
        left_side_molecules, right_side_molecules = self.__get_molecules(equation)
        self.logger.info("Parsing the equation...")
        equation_matrix = self.matrix_creator.create_equation_matrix(equation)
        self.logger.info("Creating the equation matrix...", args=equation_matrix)
        try:
            equation_coefficients = self.matrix_computer.compute_coefficients(equation_matrix)
        except ValueError as ex:
            self.logger.error("Coefficients computing error: ", ex)
            return False
        self.logger.info("Computed the coefficients:", args=equation_coefficients)
        self.__print_results(left_side_molecules, right_side_molecules, equation_coefficients)
        return True

    def __get_molecules(self, equation):
        try:
            sides = self.equation_parser.parse_equation_into_two_sides(equation)
            left_side_molecules = self.equation_parser.parse_side_to_molecules(sides[0])
            right_side_molecules = self.equation_parser.parse_side_to_molecules(sides[1])
            return left_side_molecules, right_side_molecules
        except SyntaxError as ex:
            self.logger.error("Equation parsing error: ", ex)

    @staticmethod
    def __print_results(left_side_molecules, right_side_molecules, coefficients):
        print("")
        left_side_coefficients = [-int(x) for x in coefficients if x < 0]
        right_side_coefficients = [int(x) for x in coefficients if x > 0]
        for i in range(len(left_side_molecules)):
            print(left_side_coefficients[i], left_side_molecules[i], " ", end="")
            if i != len(left_side_molecules) - 1:
                print("+ ", end="")
        print("-> ", end="")
        for i in range(len(right_side_molecules)):
            print(right_side_coefficients[i], right_side_molecules[i], " ", end="")
            if i != len(right_side_molecules) - 1:
                print("+ ", end="")
        print("")

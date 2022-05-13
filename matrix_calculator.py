import os
import sys
import time
from copy import deepcopy

def operating_system() -> str:
    clear= str()
    if os.name == "nt":
        clear = "cls"
    elif os.name == "posix":
        clear = "clear"
    else:
        clear = "clear"
        
    return clear


def welcome() -> None:
    print("\nWelcome to the matrix calculator!!!")
    print("\nDeveloped by:")
    text = "alequinterok"
    typing(text, 0.1)
    print("\n\n")

def show_menu_operation(clear:str) -> None:
    os.system(clear)
    print("""
\n
 _______________________________________________
|                                               |
|What do you want to do with your matrices?:    |
|                                               |
|                                               | 
|1) Add                                         |
|2) Subtract                                    |
|3) Multiply by number                          |
|4) Multiply matrices                           |
|5) Transpose                                   |
|6) Determinant                                 |
|0) Exit                                        |
|_______________________________________________|""")


def show_menu_modify_matrix(matrix1:list, matrix2:list, clear:str) -> None:
    print("""
\n+) Do you want to modify your matrices?:
1) Yes
2) No""")


def show_matrices(matrix1, matrix2) -> None:
    print("\n+) Your matrix 1 is: \n")
    print_matrix(matrix1)
    
    print("\n+) Your matrix 2 is: \n")
    print_matrix(matrix2)


def validate_option(min: int, max: int) -> int:
    option = int(input("""
\n+) Your answer: """))
    while not option in range(min, max+1):
        print("""
\n-) Invalid option. Try again.""")
        option = int(input("""
\n+) Your answer: """))
    return option


def print_matrix(matrix: list) -> None:
    for row in range(len(matrix)):
        print(matrix[row])


def define_matrix(clear:str) -> list():
    matrix = list()
    finished = False
    while not finished:
        rowS = int(input("+) Enter the number of rows: "))
        colS = int(input("+) Enter the number of columns: "))
        
        for row in range(rowS):
            matrix.append(list())
            for col in range(colS):
                matrix[row].append(int(input(f"+) Enter the value of the matrix [{row+1}][{col+1}]: ")))
        print("\n+) Your matrix is: \n")
        print_matrix(matrix)
        print("""
\n+) Your matrix is correct?: 
1) Yes
2) No""")
        answer = validate_option(1, 2)
        if answer == 1:
            os.system(clear)
            finished = True
        else:
            matrix = list()
            clear = operating_system()
            os.system(clear)
    return matrix


def select_matrix(matrix1: list, matrix2: list, clear:str) -> list:
    print("\n+) Your matrix 1 is: \n")
    print_matrix(matrix1)
    print("\n+) Your matrix 2 is: \n")
    print_matrix(matrix2)
    print ("""
\n+) Which matrix do you want to use?
1) Matrix 1
2) Matrix 2""")
    answer = validate_option(1, 2)
    if answer == 1:
        os.system(clear)
        return matrix1
    else:
        os.system(clear)
        return matrix2


def add_matrix(matrix1: list, matrix2: list) -> list:
    result = list()
    for i in range(len(matrix1)):
        result.append(list())
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] + matrix2[i][j])
   
    return result
            
            
def subtract_matrix(matrix1: list, matrix2: list) -> list:
    result = list()
    for i in range(len(matrix1)):
        result.append(list())
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] - matrix2[i][j])
   
    return result


def multiply_by_number(matrix: list) -> list:
    result = list()
    number = int(input("\n+) Enter the number: "))
    for i in range(len(matrix)):
        result.append(list())
        for j in range(len(matrix[0])):
            result[i].append(matrix[i][j] * number)
    
    return result


def transpose_matrix(matrix: list) -> list:
    result = list()
    for i in range(len(matrix[0])):
        result.append(list())
        for j in range(len(matrix)):
            result[i].append(matrix[j][i])
   
    return result


def multiply_matrices(matrix1: list, matrix2: list) -> list:
    result = list()
    matrix2_transposed = transpose_matrix(matrix2)
    
    for i in range(len(matrix1)):
        result.append(list())
    
    for i in range(len(matrix1)):
        for j in range(len(matrix2_transposed)):
            suma = 0
            for k in range(len(matrix1[0])):
                suma += matrix1[i][k] * matrix2_transposed[j][k]
            result[i].append(suma)
    
    return result


def smaller_matrix(matrix: list, row: int, col: int) -> list:
    new_matrix = deepcopy(matrix)
    new_matrix.remove(matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][col])
    
    return new_matrix


def determinant(matrix: list) -> int:
    rowS_number = len(matrix)
    for row in matrix:
        if len(row) != rowS_number:
            print("\n-) The matrix is not square.")
            return None
    
    if rowS_number == 1:
        determinant_1x1= matrix[0][0]
        return determinant_1x1
    
    elif rowS_number == 2:
        determinant_2x2 = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])
        return determinant_2x2
    
    else:
        result = 0
        colS_number = rowS_number
        for j in range(colS_number):
            cofactor = (-1)**(0+j) * matrix[0][j] * determinant(smaller_matrix(matrix, 0, j))
            result += cofactor
        return result


def typing(text:str, velocity:float) -> None:
    print("\n")
    splited = text.split()
    for word in splited:
        for letter in word:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(velocity)


def main():
    finished = False
    clear = operating_system()
    
    welcome()
    
    matrix1 = define_matrix(clear)
    matrix2 = define_matrix(clear)
    result = list()
    
    while not finished:
        show_matrices(matrix1, matrix2)


        show_menu_modify_matrix(matrix1, matrix2, clear)
        answer = validate_option(1, 2)
        if answer == 1:
            os.system(clear)
            matrix1 = define_matrix(clear)
            matrix2 = define_matrix(clear)
        
        
        show_menu_operation(clear)
        answer2 = validate_option(0, 6)
        if answer2 == 0:
            print("\n")
            typing('Closing...', 0.1)
            print("\n")
            os.system(clear)
            finished = True
        
        elif answer2 == 1:
            os.system(clear)
            result = add_matrix(matrix1, matrix2)
            print("\n The result of the addition is: \n")
            print_matrix(result)

        elif answer2 == 2:
            os.system(clear)
            result = subtract_matrix(matrix1, matrix2)
            print("\n The result of the subtraction is: \n")
            print_matrix(result)

        elif answer2 == 3:
            os.system(clear)
            matrix = select_matrix(matrix1, matrix2, clear)
            result = multiply_by_number(matrix)
            print("\n The result of the multiplication by a number is: \n")
            print_matrix(result)

        elif answer2 == 4:
            os.system(clear)
            result = multiply_matrices(matrix1, matrix2)
            print("\n The result of the multiplication between matrices is: \n")
            print_matrix(result)
        
        elif answer2 == 5:
            os.system(clear)
            matrix = select_matrix(matrix1, matrix2, clear)
            print("\n The result of the transpose is: \n")
            result = transpose_matrix(matrix)
            print_matrix(result)
            
            
        else:
            os.system(clear)
            matrix = select_matrix(matrix1, matrix2, clear)
            print("\n The result of the determinant is: \n")
            determinant_result = determinant(matrix)
            print(determinant_result)
    
    os.system(clear)

main()
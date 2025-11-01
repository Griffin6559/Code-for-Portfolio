import numpy as np

def main():
    # my_array = np.array([[12, 73, 68], [33, 25, 1], [54, 46, 92]])
    # print(f"The largest element in my_array is: { np.max(my_array) }")
    # print(f"The largest element in my_array is at index: { np.argmax(my_array) }")
    # print(f"The largest elements in each column are: { np.max(my_array,axis=1 )}")
    # new_array = np.array([[-18, 13, 83, 11], [28, 18, 12, -16]])
    # print(new_array)
    # print(new_array[-1])
    # print(np.sort(new_array[0]))
    # print(np.argwhere(new_array > 20))
    # print(np.nonzero(new_array))
    # print(np.where(new_array >0))
    # print(np.sort(new_array, axis=1))
    # customers = np.array([['Dave','4101'],['Gwendolyn','3222'],['Anne','2315']])
    # gwen_id_index = np.argwhere(customers[0]'Gwendolyn')
    # print(gwen_id_index)
    # my_array = [[[1]],[[2]],[[3]]] * np.ones((3,3,3))
    # print(my_array)
    # print(my_array[1][0][0])
    # print(my_array[1][0:8])
    # create a copy of my_array named new_array
    # my_array = [[[1]],[[2]],[[3]]] * np.ones((3,3,3))
    # print(my_array)
    # new_array = my_array

    #add 5 to every other element
    # new_array[::2,::2,::2] += 5
    # add 5 to the corner elements
    # new_array[ <YOUR ANSWER HERE> ] += 5
    # # add 5 to the center elements
    # print(new_array)
    # my_array = [ [ [1] ],[ [2] ],[ [3] ] ] * np.ones((3,3,3))
    # print(my_array[0].flatten())
    # x= np.array([1, 2, 3, 4, 5])
    # print(x)
    # print(x[x % 2 == 1])
    a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    b = a.reshape(4, 4)
    c = a.reshape(2, 2, 4)
    d = a.reshape(2, 2, 2, 2)
    print(d)







main()

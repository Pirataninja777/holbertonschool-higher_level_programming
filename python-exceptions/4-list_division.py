#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Retrieve elements from both lists if within range
            elem1 = my_list_1[i]
            elem2 = my_list_2[i]

            # Try to perform the division
            try:
                result.append(elem1 / elem2)
            except ZeroDivisionError:
                print("division by 0")
                result.append(0)
            except TypeError:
                print("wrong type")
                result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            # Append 0 if there's any other issue
            pass

    return result

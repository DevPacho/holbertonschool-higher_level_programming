#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    final_list = []

    for traverse in range(list_length):
        try:
            div = my_list_1[traverse] / my_list_2[traverse]
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0

        finally:
            final_list = final_list + [div]
    return final_list

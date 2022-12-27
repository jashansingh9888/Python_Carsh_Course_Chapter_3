if __name__ == '__main__':
    guest_list = ['gagan', 'sharan', 'Avtar', 'jashan']
    print("I would like to invite " + guest_list[0].title() + " to the dinner")
    print("I would like to invite " + guest_list[1].title() + " to the dinner")
    print("I would like to invite " + guest_list[2].title() + " to the dinner")
    print("I would like to invite " + guest_list[3].title() + " to the dinner")
    print("I have found a bigger dinner table.")

    guest_list.insert(0, 'Sidhu')
    guest_list.insert(2, 'Bindi')
    guest_list.append('lali')

    print("I would like to invite " + guest_list[0].title() + " to the dinner")
    print("I would like to invite " + guest_list[1].title() + " to the dinner")
    print("I would like to invite " + guest_list[2].title() + " to the dinner")
    print("I would like to invite " + guest_list[3].title() + " to the dinner")
    print("I would like to invite " + guest_list[4].title() + " to the dinner")
    print("I would like to invite " + guest_list[5].title() + " to the dinner")
    print("I would like to invite " + guest_list[6].title() + " to the dinner")

    print("I just found out the dinner table wont arrive in time for dinner.")

    removed_guest = guest_list.pop(0)
    print(" I am soory "+ removed_guest.title()+ " i can not invite to you the dinner.")

    removed_guest = guest_list.pop(2)
    print(" I am soory "+ removed_guest.title()+ " i can not invite to you the dinner.")

    removed_guest = guest_list.pop(3)
    print(" I am soory " + removed_guest.title() + " i can not invite to you the dinner.")

    removed_guest = guest_list.pop(1)
    print(" I am soory " + removed_guest.title() + " i can not invite to you the dinner.")

    removed_guest = guest_list.pop(2)
    print(" I am soory " + removed_guest.title() + " i can not invite to you the dinner.")

    print(guest_list)
    print("I would like to invite " + guest_list[0].title() + " to the dinner")
    print("I would like to invite " + guest_list[1].title() + " to the dinner")
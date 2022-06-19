"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active and touching_ghost:
        return True
    else:
        return False



def score(touching_power_pellet, touching_dot):
    if  touching_dot  or touching_power_pellet:
        return True
    else:
        return False



def lose(power_pellet_active, touching_ghost):
    if touching_ghost and not power_pellet_active:
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    has_lost=lose(power_pellet_active, touching_ghost)
    if not has_lost and has_eaten_all_dots:
        return True
    else:
        return False

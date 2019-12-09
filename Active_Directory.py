"""
Runtime : O(n)

Design:
1. Use recursive approach to get all the nested groups.

"""

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if group is None or user is None:
        return False

    # If the group has sub groups
    if group.get_groups() is not None:
        for g in group.get_groups():
            return is_user_in_group(user, g)

    # If the group has other users
    if group.get_users() is not None:
        users = group.get_users()
        if user in users:
            return True

    return False


print(is_user_in_group("sub_child_user", parent))  # Return True
print(is_user_in_group("sub_child_user", None))  # Return False
print(is_user_in_group(None, sub_child))  # Return False
print(is_user_in_group("unknown_user", parent))  # Return False

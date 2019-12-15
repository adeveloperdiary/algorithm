from collections import defaultdict


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self, path, handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for p in path:
            node = node.children[p]

        node.handler = handler

    def find(self, path):
        node = self.root
        match = True

        for p in path:
            if p in node.children:
                node = node.children[p]
            else:
                match = False

        if match:
            return node.handler
        else:
            return None


# Starting at the root, navigate the Trie to find a match for this path
# Return the handler for a match, or None for no match


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        self.children = defaultdict(RouteTrieNode)
        self.handler = None

    def insert(self, path):
        self.children[path] = RouteTrie()


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, error_handler):
        self.router = RouteTrie(root_handler)
        self.error_handler = error_handler

    # Create a new RouteTrie for holding our routes
    # You could also add a handler for 404 page not found responses as well!

    def add_handler(self, path, handler):
        self.router.insert(self.split_path(path), handler)

    # Add a handler for a path
    # You will need to split the path and pass the pass parts
    # as a list to the RouteTrie

    def lookup(self, path):

        if path == "/":
            return self.router.root.handler

        if path[-1] == "/":
            path = path[:-1]

        handler = self.router.find(self.split_path(path))
        if handler is None:
            return self.error_handler
        else:
            return handler

    # lookup path (by parts) and return the associated handler
    # you can return None if it's not found or
    # return the "not found" handler if you added one
    # bonus points if a path works with and without a trailing slash
    # e.g. /about and /about/ both return the /about handler

    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one

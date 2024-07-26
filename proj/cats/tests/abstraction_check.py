"""Infrastructure for detecting abstraction barrier violations."""

class AbstractionViolation(Exception):
    pass

def datatype(obj):
    return type(obj).__name__

# Generic abstract data type
class Abstract:
    def __add__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __radd__(self, other):
        raise AbstractionViolation("Can't add {} object to {}".format(datatype(self), datatype(other)))

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return other is self
        raise AbstractionViolation("Can't use == on {} object and {}".format(datatype(self), datatype(other)))

    def __ne__(self, other):
        if isinstance(other, type(self)):
            return other is not self
        raise AbstractionViolation("Can't use != on {} object and {}".format(datatype(self), datatype(other)))

    def __bool__(self):
        raise AbstractionViolation("Can't use {} object as a boolean".format(datatype(self)))

    def __getitem__(self, index):
        raise AbstractionViolation("Can't use [] notation on {} object".format(datatype(self)))

    def __contains__(self, other):
        raise AbstractionViolation("Can't use contains notation on {} object".format(datatype(self)))

    def __delitem__(self, other):
        raise AbstractionViolation("Can't use del notation on {} object".format(datatype(self)))

    def __iter__(self):
        raise AbstractionViolation("Can't iterate on {} object".format(datatype(self)))

    def __len__(self):
        raise AbstractionViolation("Can't use len notation on {} object".format(datatype(self)))

    def __setitem__(self, key, item):
        raise AbstractionViolation("Can't use setitem notation on {} object".format(datatype(self)))

    def __call__(self, *args, **kwargs):
        raise AbstractionViolation("Can't call {} object".format(datatype(self)))

    def __hash__(self):
        return id(self)

class Match(Abstract):
    def __init__(self, words, timestamps_per_player):
        self.a, self.b = words, timestamps_per_player
    def __repr__(self):
        return '<Match {} {}>'.format(self.a, self.b)

match = Match
get_word = lambda u, v: u.a[v]
get_all_words = lambda u: u.a
get_all_times = lambda u: u.b
time = lambda u, v, w: u.b[v][w]

old = {}

def swap_implementations(impl):
    # save other implementations
    old['match'] = impl.match, impl.get_word, impl.get_all_words, impl.get_all_times, impl.time

    # save our implementations
    new_match = match, get_word, get_all_words, get_all_times, time

    # replace impl's implementations with ours
    impl.match, impl.get_word, impl.get_all_words, impl.get_all_times, impl.time = match, get_word, get_all_words, get_all_times, time

def restore_implementations(impl):
    impl.match, impl.get_word, impl.get_all_words, impl.get_all_times, impl.time = old['match']
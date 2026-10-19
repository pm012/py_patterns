import string
import random
#import sys
import tracemalloc
import timeit

# 1. Basic class (without optimization)
class User:
    def __init__(self, name):
        self.name = name

# 2. Optimized class (Flyweight)
class User1:
    # Instead of list we can use dict to make search even faster  O(1)
    strings = {}  # { "string": index }
    strings_list = []  # for rapid recovery via __str__

    def __init__(self, name):        
        def add_or_get(s):
            if s in User1.strings:
                return User1.strings[s]
            else:
                idx = len(User1.strings_list)
                User1.strings[s] = idx
                User1.strings_list.append(s)
                return idx
        
        # Saving only integers (indeces) instead of heavy strings
        self.names = [add_or_get(s) for s in name.split(' ')]

    def __str__(self):
        return ' '.join(User1.strings_list[x] for x in self.names)


#===========================__slots__ best practice========================

class UserBestPractice:
    # 1. Flyweight compund (CLASS attributes)
    # Saved in one instance during while program is running
    strings = {}
    strings_list = []

    # 2. Object optimization (CLASS attribute)
    # Lower  __dict__  memory allocation for every created user, using only array for  'names'
    __slots__ = ('names',)

    def __init__(self, name):
        def add_or_get(s):
            if s in UserBestPractice.strings:
                return UserBestPractice.strings[s]
            else:
                idx = len(UserBestPractice.strings_list)
                UserBestPractice.strings[s] = idx
                UserBestPractice.strings_list.append(s)
                return idx
        
        # Record data to the single allowed slot
        self.names = [add_or_get(s) for s in name.split(' ')]

    def __str__(self):
        return ' '.join(UserBestPractice.strings_list[x] for x in self.names)



#=============================end best practice implementation=================
# ==================== Ultimate Memory optimisation ====================
class UserUltimate:
    strings = {}
    strings_list = []
    
    # Using __slots__ for eliminating __dict__
    __slots__ = ('names',)

    # Moving out auxilary method on the class level (to rid off __init__  creation)
    @classmethod
    def _add_or_get(cls, s):
        if s in cls.strings:
            return cls.strings[s]
        idx = len(cls.strings_list)
        cls.strings[s] = idx
        cls.strings_list.append(s)
        return idx

    def __init__(self, name):
        # Instead of list use tuple — more lightweight for memory
        self.names = tuple(UserUltimate._add_or_get(s) for s in name.split(' '))

    def __str__(self):
        return ' '.join(UserUltimate.strings_list[x] for x in self.names)
# ==================================================================


def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(8)])

if __name__ == "__main__":
    # Generating database of names
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]
    
    print(f"Generating Carthesian product: 100 * 100 = 10,000 users...\n")

    # --- TEST 1: basic User implementation ---
    tracemalloc.start()  # Allocating memory
    
    users_normal = []
    for first_name in first_names:
        for last_name in last_names:
            users_normal.append(User(f"{first_name} {last_name}"))
            
    current, peak_normal = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"[User] Memory track (peak): {peak_normal / 1024:.2f} KB")

    # Clear memory before the second test
    del users_normal
    
    # --- TEST 2: Optimized User1 (Flyweight) ---
    tracemalloc.start()
    
    users_flyweight = []
    for first_name in first_names:
        for last_name in last_names:
            users_flyweight.append(User1(f"{first_name} {last_name}"))
            
    current, peak_flyweight = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"[User1 - Flyweight] Memory track (peak): {peak_flyweight / 1024:.2f} KB")
    
    # Clear memory before the second test
    del users_flyweight

# --- TEST 3: Optimized User1 (Flyweight with slots) ---
    tracemalloc.start()
        
    users_slots = []
    for first_name in first_names:
        for last_name in last_names:
            users_slots.append(UserBestPractice(f"{first_name} {last_name}"))
                
    current, peak_flyweight_slot = tracemalloc.get_traced_memory()
    tracemalloc.stop()
        
    print(f"[User - Flyweight_slot] Memory track (peak): {peak_flyweight_slot / 1024:.2f} KB")
        
    # Clear memory before the second test
    del users_slots

 # --- TEST 4: Ultimate Optimization (Tuple + Slots + Classmethod) ---
    tracemalloc.start()
    users_ultimate = [UserUltimate(f"{f} {l}") for f in first_names for l in last_names]
    current, peak_ultimate = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"[User - Ultimate] Memory track (peak): {peak_ultimate / 1024:.2f} KB")
    
    # --- Result ---
    saved = peak_normal - peak_flyweight
    percent = (saved / peak_normal) * 100
    print(f"\nMemory saving due to Flyweight: {saved / 1024:.2f} KB ({percent:.1f}%)")

    # ---slots comparizon
    saved1 = peak_normal - peak_flyweight_slot
    percent1 = (saved1 / peak_normal) * 100
    print(f"\nMemory saving due to basic slot: {saved1 / 1024:.2f} KB ({percent1:.1f}%)")

    # ---slots optimized comarizon
    saved2 = peak_normal - peak_ultimate
    percent2 = (saved2 / peak_normal) * 100
    print(f"\nMemory saving due to basic slot: {saved2 / 1024:.2f} KB ({percent2:.1f}%)")

  
    # Check, that data can be recovered correctly
    print(f"\nCheck output for the first user: {users_ultimate[0]}")

    print('--------------------------------CPU bound ---------------------------------------------------')
def random_string():
    chars = string.ascii_lowercase
    return ''.join([random.choice(chars) for _ in range(8)])

first_names = [random_string() for _ in range(100)]
last_names = [random_string() for _ in range(100)]

def test_normal():
    users = []
    for f in first_names:
        for l in last_names:
            users.append(User(f"{f} {l}"))
    return users

def test_flyweight():
    User1.strings.clear()
    User1.strings_list.clear()
    users = []
    for f in first_names:
        for l in last_names:
            users.append(User1(f"{f} {l}"))
    return users

def test_slots():
    UserBestPractice.strings.clear()
    UserBestPractice.strings_list.clear()
    users = []
    for f in first_names:
        for l in last_names:
            users.append(UserBestPractice(f"{f} {l}"))
    return users

def test_ultimate():
    UserUltimate.strings.clear()
    UserUltimate.strings_list.clear()
    users = [UserUltimate(f"{f} {l}") for f in first_names for l in last_names]
    return users

t_normal = timeit.timeit(test_normal, number=10) / 10 * 1000
t_flyweight = timeit.timeit(test_flyweight, number=10) / 10 * 1000
t_slots = timeit.timeit(test_slots, number=10) / 10 * 1000
t_ultimate = timeit.timeit(test_ultimate, number=10) / 10 * 1000

print(f"Normal: {t_normal:.2f} ms")
print(f"Flyweight: {t_flyweight:.2f} ms")
print(f"Slots: {t_slots:.2f} ms")
print(f"Ultimate: {t_ultimate:.2f} ms")

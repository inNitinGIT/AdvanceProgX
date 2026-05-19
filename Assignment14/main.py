import sys
import gc


# =========================================================
# NODE CLASS
# =========================================================
class Node:
    def __init__(self, name):
        self.name = name
        self.link = None

    # This method is called when object is destroyed
    def __del__(self):
        print(f"{self.name} is being garbage collected")


# =========================================================
# ENABLE GARBAGE COLLECTOR DEBUGGING
# =========================================================
gc.set_debug(gc.DEBUG_SAVEALL)

print("===== Creating Nodes =====")

# Create two nodes
A = Node("Node A")
B = Node("Node B")


# =========================================================
# CREATE CIRCULAR REFERENCE
# A -> B
# B -> A
# =========================================================
A.link = B
B.link = A

print("\n===== Circular Reference Created =====")

# =========================================================
# CHECK REFERENCE COUNTS
# =========================================================
print("\nReference Count of A:", sys.getrefcount(A))
print("Reference Count of B:", sys.getrefcount(B))

# NOTE:
# getrefcount() adds 1 extra temporary reference internally


# =========================================================
# STORE IDS FOR INVESTIGATION
# =========================================================
a_id = id(A)
b_id = id(B)

print("\nMemory Address of A:", a_id)
print("Memory Address of B:", b_id)


# =========================================================
# DELETE EXTERNAL REFERENCES
# =========================================================
print("\n===== Deleting A and B =====")

del A
del B

print("Variables A and B deleted")


# =========================================================
# INVESTIGATION
# Objects still exist because of circular reference
# =========================================================
print("\n===== Investigating Garbage =====")

print("Objects currently saved by GC before collection:")
print(gc.garbage)

# Count tracked objects before cleanup
before = len(gc.get_objects())
print("\nTotal tracked objects before gc.collect():", before)


# =========================================================
# FORCE GARBAGE COLLECTION
# =========================================================
print("\n===== Running Garbage Collector =====")

collected = gc.collect()

print("\nUnreachable objects collected:", collected)


# =========================================================
# AFTER CLEANUP
# =========================================================
after = len(gc.get_objects())

print("\nTotal tracked objects after gc.collect():", after)

print("\nGarbage list after collection:")
print(gc.garbage)

print("\n===== Program Finished =====")
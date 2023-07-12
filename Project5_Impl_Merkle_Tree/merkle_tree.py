import math
import hashlib,json
import random
import string

def cons_merkle(Data):
    # Split data into blocks of 32
    blocks = [Data[i:i+32] for i in range(0, len(Data), 32)]
    
    # If the number of blocks is not a power of 2, append empty blocks
    while len(blocks) & (len(blocks) - 1) != 0:
        blocks.append('')
    
    # Calculate length and depth of the tree
    length = len(blocks)
    depth = math.ceil(math.log(length, 2)) + 1
    
    # Initialize merkle tree with empty lists for each depth level
    merkle_tree = [[] for _ in range(depth)]
   
    # Populate the leaf nodes
    for i in range(length):
        merkle_tree[0].append(hashlib.sha256(blocks[i].encode()).hexdigest())
    
    # Populate the rest of the tree
    for j in range(1, depth):
        for k in range(0, len(merkle_tree[j-1]), 2):
            merkle_tree[j].append(hashlib.sha256(
                (merkle_tree[j-1][k]+ merkle_tree[j-1][k+1]).encode()).hexdigest())
        
    root_value = merkle_tree[depth-1][0] if merkle_tree[depth-1] else None

    return merkle_tree, root_value

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choices(characters, k=length))
    return random_string

def verify(Data,root_value):
    blocks = [Data[i:i+32] for i in range(0, len(Data), 32)]

    while len(blocks) & (len(blocks) - 1) != 0:
        blocks.append('')
    length = len(blocks)
    depth = math.ceil(math.log(length, 2)) + 1

    merkle_tree = [[] for _ in range(depth)]
    for i in range(length):
        merkle_tree[0].append(hashlib.sha256(blocks[i].encode()).hexdigest())

    for j in range(1, depth):
        for k in range(0, len(merkle_tree[j-1]), 2):
            merkle_tree[j].append(hashlib.sha256(
                (merkle_tree[j-1][k]+ merkle_tree[j-1][k+1]).encode()).hexdigest())
        
    veri_root_value = merkle_tree[depth-1][0] if merkle_tree[depth-1] else None
    print("初始数据的校验值为",root_value)
    print("现在数据的校验值为",veri_root_value)
    if(veri_root_value==root_value):
        print("检验完成，数据完整")
    else:
        print("数据被篡改，不完整")
    return

data=generate_random_string(10000)
Merkle_tree,root_value=cons_merkle(data)
verify(data,root_value)


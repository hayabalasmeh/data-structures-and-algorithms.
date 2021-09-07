from data_structures_algorth.challenge_hashtable.hashtable import HashTable,Node


def add_values(hashmap, values_list):
    for bucket in hashmap.buckets:
        if bucket:
            current = bucket.head
            while current:
                values_list.append(current.value)
                current = current.next
    return values_list 


def left_join( first_hash, second_hash):
    joined_values = []
    add_values(first_hash, joined_values)
    if not joined_values:
       return joined_values
    for pairs in joined_values:
        if second_hash.contains(pairs[0]):
            value = second_hash.get(pairs[0])
            pairs.append(value)
        else:
            pairs.append('Null')
        
    return joined_values

if __name__ == "__main__":
    hash_1 = HashTable()
    hash_1.add('nice','good')
    hash_1.add('small','tiny')
    hash_1.add('beautiful','sweet')
    hash_2 = HashTable()
    hash_2.add('small','big')
    hash_2.add('nice','bad')
    hash_2.add('old','new')
    print(left_join(hash_1,hash_2))


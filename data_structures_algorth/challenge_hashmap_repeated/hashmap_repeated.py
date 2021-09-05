from data_structures_algorth.challenge_hashtable.hashtable import HashTable

def find_repeated(string):

        if not string:
            return string
        tester = HashTable()
        words = string.split(' ')
        for word in words:
            if tester.contains(word) or tester.contains(f'{word},'):
                return word
            else:
                tester.add(word.lower(),0)
                
        return ""
if __name__=="__main__":
    string = "It was the best of times, it was the worst of times, it was the age of wisdom,"
    print(find_repeated(string))
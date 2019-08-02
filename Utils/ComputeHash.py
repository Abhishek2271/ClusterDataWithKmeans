import hashlib
"""
    <Created Date> Nov 2, 2018 </CreatedDate>    
    <About>
        For the given string, compute SHA1 hash
    </About>
"""
def ComputeHash(string_element):
    computed_Hash = hashlib.sha1(string_element).hexdigest()
    return computed_Hash

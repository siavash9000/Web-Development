import hmac
from hashlib import md5

# Implement the hash_str function to use HMAC and our SECRET instead of md5
SECRET = 'imsosecret'

class hasher:
    
    def hash_str(self,s):
        return hmac.new(SECRET,s,md5).hexdigest()
    
    def make_secure_val(self,s):
        return "%s|%s" % (s, self.hash_str(s))
    
    def check_secure_val(self,h):
        val = h.split('|')[0]
        if h == self.make_secure_val(val):
            return val
    
    
def main():
    hasher_instance = hasher()
    print hasher_instance.hash_str("somestring")

if __name__ == "__main__":
    main()
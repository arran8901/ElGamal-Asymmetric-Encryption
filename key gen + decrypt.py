# ElGamal key generation and asymmetric decryption
# Run this first!

prime = input("Enter public prime (eg. 997): ")
base = input("Enter public base (eg. 2): ") % prime
privateKey = input("Enter private key (eg. 20): ")

print "The public key is: " + str((base ** privateKey) % prime)
print "Release your prime, base, and public key. Keep the private key a secret!\n"

while True:
  c1 = input("Enter ciphertext component c1: ")
  c2 = input("Enter ciphertext component c2: ")
  print "Original plaintext: " + str((pow(pow(c1, privateKey, prime), prime - 2, prime) * c2) % 997)
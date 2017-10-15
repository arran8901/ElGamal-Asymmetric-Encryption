# ElGamal asymmetric encryption
# Run this second - after running decrypt first to get public key

prime = input("Enter public prime (from distributor): ")
base = input("Enter public base (from distributor): ")
publicKey = input("Enter public key (from distributor): ")

while True:
  plaintext = input("\nEnter number to encrypt (< " + str(prime) + "): ")
  ephemeralKey = input("Enter ephemeral key (eg. 3): ") % prime
  print "Ciphertext component c1: " + str(pow(base, ephemeralKey))
  print "Ciphertext component c2: " + str((plaintext * pow(publicKey, ephemeralKey, prime)) % prime)
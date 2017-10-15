# ElGamal-Asymmetric-Encryption
For public key cryptosystems

# How to use:
Start by running the 'key gen + decrypt' file. Specify a prime number (the larger the better), a base, and a private key. The public key will be calculated. Release your public key (prime, base, publicKey) but keep the private key a secret.

Next, run the 'encrypt'file. Fill in the public details prime, base and publicKey. Then choose a number (n < prime) to encrypt. To send a message, convert the message to ASCII values and input the ASCII code. Next specify an ephemeral key, of arbitrary value. (For security, this should be different each message you send). You will then be provided with the ciphertext (c1, c2)

Return to the decrypt file and enter the ciphertext one at a time, beginning with c1. It will decrypt the message using the private key and (if all went well!) return you the original plaintext.

# About ElGamal public key cryptoraphy:
The ElGamal cryptosystem was among the first public key cryptosystems to be invented, and is still used today, albeit much less. It involves two public parameters, a (large) prime number p and a base g where 1 ≤ g < p. A private key x is chosen and a public key X is calculated by g^x (mod p). p, g, X are released to the public.

Anyone in the public is now able to encrypt their message m with the public key (p, g, X). They begin by generating an ephemeral key k where 1 ≤ k < p for each message they encrypt. Two ciphertext components (c1, c2) are calculated, where c1 = g^k (mod p), and c2 = m * X^k (mod p).

Now, with the private key, the plaintext can be deduced by m = invmod(c1^a) * c2 (mod p). This is because:

invmod(c1^a) * c2 = invmod((g^k)^a) * m * X^k = invmod((g^a)^k) * m((g^a)^k)

invmod((g^a)^k) * (g^a)^k cancel, leaving m.

# 
# Reference arithmetic coding
# Copyright (c) Project Nayuki
# 
# https://www.nayuki.io/page/reference-arithmetic-coding
# https://github.com/nayuki/Reference-arithmetic-coding
# 

import sys
import arithmeticcoding
python3 = sys.version_info.major >= 3


# Command line main application function.
def main(args):
	# Handle command line arguments
	if len(args) != 2:
		print("Usage: python arithmetic-decompress.py InputFile OutputFile")
		sys.exit(1)
	inputfile  = args[0]
	outputfile = args[1]
	
	bitin = arithmeticcoding.BitInputStream(open(inputfile, "rb"))
	out = open(outputfile, "wb")
	try:
		freqs = read_frequencies(bitin)
		decompress(freqs, bitin, out)
	finally:
		out.close()
		bitin.close()


def read_frequencies(bitin):
	freqs = []
	for i in range(256):
		freqs.append(read_int(bitin, 32))
	freqs.append(1)  # EOF symbol
	return arithmeticcoding.SimpleFrequencyTable(freqs)


def decompress(freqs, bitin, out):
	dec = arithmeticcoding.ArithmeticDecoder(bitin)
	while True:
		symbol = dec.read(freqs)
		if symbol == 256:  # EOF symbol
			break
		out.write(bytes((symbol,)) if python3 else chr(symbol))


# Reads an unsigned integer of the given bit width from the given stream.
def read_int(bitin, numbits):
	result = 0
	for i in range(numbits):
		result = (result << 1) | bitin.read_no_eof()  # Big endian
	return result


# Main launcher
if __name__ == "__main__":
	main(sys.argv[1 : ])
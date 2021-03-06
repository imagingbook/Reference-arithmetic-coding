import java.io.IOException;

/**
 * Encoder modeled after {@link ArithmeticEncoder}
 * @author WB
 *
 */
public class ArithmeticCharEncoder extends ArithmeticCoderBase {
	
	// Number of saved underflow bits. This value can grow without bound,
	// so a truly correct implementation would use a BigInteger.
	private int numUnderflow;

	public ArithmeticCharEncoder(int numBits) {
		super(numBits);
		// fill in
		numUnderflow = 0;
	}

	@Override
	protected void shift() throws IOException {
		int bit = (int)(low >>> (numStateBits - 1));
		//output.write(bit);
		
		// Write out the saved underflow bits
		for (; numUnderflow > 0; numUnderflow--) {
			//output.write(bit ^ 1);
		}
	}

	@Override
	protected void underflow() {
		if (numUnderflow == Integer.MAX_VALUE)
			throw new ArithmeticException("Maximum underflow reached");
		numUnderflow++;
	}
	
}

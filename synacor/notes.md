
## Notes

### Coins 

* red		: 2
* corroded	: triangle
* shiny		: pentagon
* concave	: 7
* blue		: 9

a + b * c^2 + d^3 - e = 399

* blue red shiny concave corroded
* 9 2 5 7 3
* 9 + 2 * 25 + 343 - 3
* 9 + 50 + 340
* 399

Implemented in `coins.py`

### Teleporter

Four instances of reading reg 7 (32775)

521: 7 32775 1093
	If r7 is non-zero, jump to 1093
	This prints "nonzero reg" and halts the program
5451: 8 32775 5605
	If r7 is zero, jump to 5605
5522: 1 32768 32775
	Set r0 to value of r7
6042: 1 32769 32775
	Set r1 to value of r7

* Solution plan
	* TODO
		* Method of saving state
			* Use pickle on Architecture object?
			* Issue is upon load, won't know the text of the prompt
	* Plan
		* Run program to teleporter availability
		* use teleporter and analyze commands called
		* Need to bypass 0-check for r7. Is this position 521?


### Strange book
The cover of this book subtly swirls with colors.  It is titled "A Brief Introduction to Interdimensional Physics".  It reads:

Recent advances in interdimensional physics have produced fascinating
predictions about the fundamentals of our universe!  For example,
interdimensional physics seems to predict that the universe is, at its root, a
purely mathematical construct, and that all events are caused by the
interactions between eight pockets of energy called "registers".
Furthermore, it seems that while the lower registers primarily control mundane
things like sound and light, the highest register (the so-called "eighth
register") is used to control interdimensional events such as teleportation.

A hypothetical such teleportation device would need to have have exactly two
destinations.  One destination would be used when the eighth register is at its
minimum energy level - this would be the default operation assuming the user
has no way to control the eighth register.  In this situation, the teleporter
should send the user to a preconfigured safe location as a default.

The second destination, however, is predicted to require a very specific
energy level in the eighth register.  The teleporter must take great care to
confirm that this energy level is exactly correct before teleporting its user!
If it is even slightly off, the user would (probably) arrive at the correct
location, but would briefly experience anomalies in the fabric of reality
itself - this is, of course, not recommended.  Any teleporter would need to test
the energy level in the eighth register and abort teleportation if it is not
exactly correct.

This required precision implies that the confirmation mechanism would be very
computationally expensive.  While this would likely not be an issue for large-
scale teleporters, a hypothetical hand-held teleporter would take billions of
years to compute the result and confirm that the eighth register is correct.

If you find yourself trapped in an alternate dimension with nothing but a
hand-held teleporter, you will need to extract the confirmation algorithm,
reimplement it on more powerful hardware, and optimize it.  This should, at the
very least, allow you to determine the value of the eighth register which would
have been accepted by the teleporter's confirmation mechanism.

Then, set the eighth register to this value, activate the teleporter, and
bypass the confirmation mechanism.  If the eighth register is set correctly, no
anomalies should be experienced, but beware - if it is set incorrectly, the
now-bypassed confirmation mechanism will not protect you!

Of course, since teleportation is impossible, this is all totally ridiculous.


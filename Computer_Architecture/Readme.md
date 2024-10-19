Digital Design & Comp Arch - Lecture 7: Von Neumann Model & Instruction Set Architectures

an architecture can be byte addressable or word addressable. In byte addressable, each byte has a unique address. In word addressable, each word has a unique address.  


MIPS is byte addressable.
X86 is byte addressable.
RISC-V is byte addressable.
ARM is byte addressable.
POWER PC is byte addressable.
other word addressable architectures are PDP-11, VAX, and IBM 360.

little endian: least significant byte is stored at the lowest address.
big endian: most significant byte is stored at the lowest address.

example of liitle endian: x86, ARM, MIPS
example of big endian: IBM 360, SPARC, POWER PC

comminication between big endian and little endian systems is done by converting the data to network byte order (big endian) and then converting it back to the target system's byte order.

two ways of accessing memory in a computer:
1. load/store architecture: data is loaded from memory to registers, operated on, and then stored back to memory.
2. memory-memory architecture: data is operated on directly in memory.

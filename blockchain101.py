import datetime as d
import hashlib as h

# Define the Block class to represent individual blocks in the blockchain.
class Block:
    def __init__(self, index, timestamp, data, prevhash):
        self.index = index               # Block ID
        self.timestamp = timestamp       # Timestamp when the block is created
        self.data = data                 # Data or transactions in the block
        self.prevhash = prevhash         # Hash of the previous block
        self.hash = self.hashblock()     # Compute the hash for this block

    # Method to calculate the hash for the block.
    def hashblock(self):
        block_encryption = h.sha256()    # Initialize a SHA-256 hash object
        block_encryption.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.prevhash)).encode('utf-8'))
        return block_encryption.hexdigest()  # Return the hexadecimal representation of the hash

    # Static method to create the genesis block (the first block in the blockchain).
    @staticmethod
    def genesisblock():
        return Block(0, d.datetime.now(), "Genesis Block Transaction", "0")  # "0" represents no previous block

    # Static method to create a new block, given the previous block.
    @staticmethod
    def newblock(lastblock):
        index = lastblock.index + 1          # Increment the block ID
        timestamp = d.datetime.now()         # Current timestamp
        hashblock = lastblock.hash           # Hash of the previous block
        data = "Transaction " + str(index)   # Data for the new block
        return Block(index, timestamp, data, hashblock)

# Initialize the blockchain with the genesis block.
blockchain = [Block.genesisblock()]

# Set the previous block to the genesis block initially.
prevblock = blockchain[0]

# Print information about the genesis block.
print("Block ID :{} ".format(prevblock.index))              #show block id
print("Timestamp:{}".format(prevblock.timestamp))           #show block timestamp
print("Hash of the block:{}".format(prevblock.hash))        #show block hash
print("Previous Block Hash:{}".format(prevblock.prevhash))  #show block previous hash
print("data:{}\n".format(prevblock.data))                   #show block data

# Generate and add five more blocks to the blockchain.
for i in range(0,5):                     #loop and print 
    addblock = Block.newblock(prevblock) #the block to be added to the block
    blockchain.append(addblock)          #adding the block to the chain of blocks
    prevblock = addblock                 #previous block becomes the last block

    print("Block ID #{} ".format(addblock.index))               #show block id
    print("Timestamp:{} ".format(addblock.timestamp))           #show block timestamp
    print("Hash of the block:{}".format(addblock.hash))         #show block hash
    print("Previous Block Hash:{}".format(addblock.prevhash))   #show block previous hash
    print("data:{}\n".format(addblock.data))                    #show block data

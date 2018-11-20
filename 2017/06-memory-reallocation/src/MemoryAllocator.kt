import java.io.File

fun main(arg: Array<String>) {

    val inputMemoryBanks = readFileAsLines("memory_banks_input")
    val distributedMemory = MemoryAllocator().distributeMemory(splitAndMapToInt(inputMemoryBanks[0]))
    println("Steps: ${distributedMemory.size}")

}

fun readFileAsLines(fileName: String): List<String>
        = File(fileName).readLines()

fun splitAndMapToInt(input: String): List<Int> {
    return input.split("\\s+".toRegex()).map { it.toInt() }
}


class MemoryAllocator {

    fun distributeMemory(memoryBanks: List<Int>): List<List<Int>> {

        var memoryAllocationHistory = ArrayList<List<Int>>()
        memoryAllocationHistory.add(memoryBanks)

        while (true) {
            val currentMemoryBanks = memoryAllocationHistory.last()
            val maxIndex = currentMemoryBanks.withIndex().maxBy { it.value }!!.index
            val nextMemoryBanks = doDistributeMemory(currentMemoryBanks, maxIndex)
            if (memoryAllocationHistory.contains(nextMemoryBanks)) {
                break
            }
            memoryAllocationHistory.add(nextMemoryBanks)
        }

        return memoryAllocationHistory
    }

    private fun doDistributeMemory(memoryBanks: List<Int>, maxValueIdx: Int): List<Int> {
        val newMemoryBanks = ArrayList<Int>()
        newMemoryBanks.addAll(memoryBanks)
        var remainingMemoryBlocks = memoryBanks[maxValueIdx]
        var idx = incAndWrapIndex(maxValueIdx, newMemoryBanks.size)
        newMemoryBanks[maxValueIdx] = 0
        while (remainingMemoryBlocks > 0) {
            newMemoryBanks[idx] += 1
            remainingMemoryBlocks--
            idx = incAndWrapIndex(idx, newMemoryBanks.size)
        }
        return newMemoryBanks
    }

    private fun incAndWrapIndex(idx: Int, size: Int): Int {
        return (idx + 1) % size
    }

}

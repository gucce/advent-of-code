import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class MemoryAllocatorTest {

    @Test
    fun distributeMemorySimple() {
        val testInput = splitAndMapToInt("0 2 7 0")
        val memorySteps = MemoryAllocator().distributeMemory(testInput)
        assertEquals(5, memorySteps.size)
    }

}

import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Test

internal class MemoryAllocatorTest {

    private val testInput = splitAndMapToInt("0 2 7 0")

    @Test
    fun testDistributeMemorySimple() {
        assertEquals(5, MemoryAllocator().getDistributeMemoryStepsCount(testInput))
    }

    @Test
    fun testGetDistributeMemoryCycleLength() {
        assertEquals(4, MemoryAllocator().getDistributeMemoryCycleLength(testInput))
    }

}

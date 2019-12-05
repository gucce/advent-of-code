import adventofcode.extractOpCodeParamModes
import adventofcode.processIter
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals

internal class ProgramAlarmExtendedTest {

    @Test
    fun testProcessIter() {
        val input = mutableListOf(1002, 4, 3, 4, 33)
        processIter(input)
        assertEquals(99, input[4])
    }

    @Test
    internal fun testExtractOpCodeParamList() {
        val modes = extractOpCodeParamModes(1002)
        assertEquals(listOf(2, 0, 1), modes)
    }
}

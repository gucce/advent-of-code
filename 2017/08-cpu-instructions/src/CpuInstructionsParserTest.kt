import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

internal class CpuInstructionsParserTest {

    private var parser: CpuInstructionsParser = CpuInstructionsParser()

    private val input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""

    @Test
    internal fun testRunInstructions() {
        parser.runInstructions(input.lines())
        assertEquals(1, parser.maxRegisterValue)
        assertEquals(10, parser.maxOverallRegisterValue)
    }

}

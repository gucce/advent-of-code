import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

internal class CpuInstructionsParserTest {

    private var parser: CpuInstructionsParser = CpuInstructionsParser()

    @Test
    internal fun testParseCondition() {
        assertEquals("a > 1", parser.parseCondition("b inc 5 if a > 1"))
        assertEquals("b < 5", parser.parseCondition("a inc 1 if b < 5"))
        assertEquals("a >= 1", parser.parseCondition("abc dec -10 if a >= 1"))
        assertEquals("c == 10", parser.parseCondition("c inc -20 if c == 10"))
    }

    @Test
    internal fun testRunInstruction() {
        parser.runInstruction("b inc 5 if a > 1")
        assertEquals(0, parser.getRegisterVal("b"))
        parser.runInstruction("a inc 1 if b < 5")
        assertEquals(1, parser.getRegisterVal("a"))
        parser.runInstruction("abc dec -10 if a >= 1")
        assertEquals(10, parser.getRegisterVal("abc"))
        parser.runInstruction("c inc -20 if c == 10")
        assertEquals(0, parser.getRegisterVal("c"))

    }

    @Test
    internal fun testCalcInstruction() {
        parser.execInstruction("b inc 5 if a > 1")
        assertEquals(5, parser.registers["b"])
    }

}

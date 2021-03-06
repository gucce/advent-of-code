import java.io.File

fun main(args: Array<String>) {
    val input = readFileAsLines("cpu_instructions_input")
    CpuInstructionsParser().apply {
        runInstructions(input)
        println("Max current register value: $maxRegisterValue")
        println("Max overall register value: $maxOverallRegisterValue")
    }

}

fun readFileAsLines(fileName: String): List<String> = File(fileName).readLines()


class CpuInstructionsParser {

    var registers: MutableMap<String, Int> = HashMap()
    var maxOverallRegisterValue: Int = 0
    val maxRegisterValue: Int? get() = registers.values.max()


    fun runInstructions(lines: List<String>) {
        lines.forEach { l -> runSingleInstruction(l) }
    }

    private fun runSingleInstruction(line: String) {
        if (evalCondition(line)) {
            runOpCode(line)
        }
    }

    private fun evalCondition(line: String): Boolean {
        val (reg, operator, value) = parseCondition(line).split(Regex("\\s+"))
        val regVal = registers[reg] ?: 0
        return when (operator) {
            "==" -> regVal == value.toInt()
            "!=" -> regVal != value.toInt()
            ">" -> regVal > value.toInt()
            "<" -> regVal < value.toInt()
            "<=" -> regVal <= value.toInt()
            ">=" -> regVal >= value.toInt()
            else -> throw IllegalArgumentException("Wrong operator $operator")
        }
    }

    private fun runOpCode(instruction: String) {
        val (reg, operator, value) = parseInstruction(instruction).split(Regex("\\s+"))
        val nextVal = when (operator.toLowerCase()) {
            "dec" -> getRegisterVal(reg) - value.toInt()
            "inc" -> getRegisterVal(reg) + value.toInt()
            else -> throw IllegalArgumentException("Wrong operator $operator")
        }
        maxOverallRegisterValue = maxOf(maxOverallRegisterValue, nextVal)
        registers[reg] = nextVal
    }

    private fun getRegisterVal(reg: String): Int {
        return registers.getOrPut(reg) { 0 }
    }

    private fun parseInstruction(line: String): String {
        return line.substringBefore(" if")
    }

    private fun parseCondition(instruction: String): String {
        return instruction.substringAfter("if ")
    }

}

import java.io.File

fun main(args: Array<String>) {
    val input = readFileAsLines("cpu_instructions_input")
    CpuInstructionsParser().apply {
        runInstructions(input)
        println(maxValFromRegisters())
    }

}

fun readFileAsLines(fileName: String): List<String> = File(fileName).readLines()


class CpuInstructionsParser {

    var registers: MutableMap<String, Int> = HashMap()

    fun runInstructions(lines: List<String>) {
        lines.forEach { l -> runSingleInstruction(l) }
    }

    fun runSingleInstruction(line: String) {
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

    fun runOpCode(instruction: String) {
        val (reg, operator, value) = parseInstruction(instruction).split(Regex("\\s+"))
        var valueInt = value.toInt()
        if (operator.toLowerCase() == "dec") {
            valueInt = -valueInt
        }
        val currentVal = getRegisterVal(reg)
        registers[reg] = currentVal + valueInt
    }

    fun maxValFromRegisters(): Int? {
        return registers.values.max()
    }

    fun getRegisterVal(reg: String): Int {
        return registers.getOrPut(reg) { 0 }
    }

    private fun parseInstruction(line: String): String {
        return line.substringBefore(" if")
    }

    fun parseCondition(instruction: String): String {
        return instruction.substringAfter("if ")
    }

}

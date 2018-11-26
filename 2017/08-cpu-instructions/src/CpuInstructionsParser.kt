import java.io.File

fun main(args: Array<String>) {
    val input = readFileAsLines("cpu_instructions_input")
    val parser = CpuInstructionsParser()
    parser.runInstructions(input)
    println(parser.getMaxFromRegisters())

}

fun readFileAsLines(fileName: String): List<String>
        = File(fileName).readLines()

class CpuInstructionsParser {

    var registers: MutableMap<String, Int> = HashMap()

    companion object {
        private val condFuncs = HashMap<String, (Int, Int) -> Boolean>()
        private val calcFuncs = HashMap<String, (Int, Int) -> Int>()

        init {
            condFuncs["=="] = { val1, val2 -> val1 == val2 }
            condFuncs["!="] = { val1, val2 -> val1 != val2 }
            condFuncs[">"] = { val1, val2 -> val1 > val2 }
            condFuncs["<"] = { val1, val2 -> val1 < val2 }
            condFuncs["<="] = { val1, val2 -> val1 <= val2 }
            condFuncs[">="] = { val1, val2 -> val1 >= val2 }

            calcFuncs["inc"] = { x, i -> x + i }
            calcFuncs["dec"] = { x, i -> x - i }
        }
    }

    fun evalCondition(line: String): Boolean {
        val (register, operator, value) = parseCondition(line).split(Regex("\\s+"))
        val registerValue = registers[register] ?: 0
        return condFuncs[operator]?.invoke(registerValue, value.toInt())
                ?: throw IllegalArgumentException("Wrong operator $operator")
    }

    fun getMaxFromRegisters(): Int? {
        return registers.values.max()
    }

    fun runInstructions(input: List<String>) {
        for (l in input) {
            runInstruction(l)
        }
    }

    fun runInstruction(line: String) {
        if (evalCondition(line)) {
            execInstruction(line)
        }
    }

    fun execInstruction(instruction: String) {
        val (register, operator, value) = parseInstruction(instruction).split(Regex("\\s+"))
        var valueInt = value.toInt()
        if (operator.toLowerCase() == "dec") {
            valueInt = -valueInt
        }
        val currentVal = registers.getOrPut(register) { 0 }
        registers[register] = currentVal + valueInt
    }

    fun getRegisterVal(register: String): Int {
        return registers.getOrPut(register) { 0 }
    }

    fun parseInstruction(line: String): String {
        return line.substringBefore(" if")
    }

    fun parseCondition(instruction: String): String {
        return instruction.substringAfter("if ")
    }

}

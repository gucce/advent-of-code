import java.io.File

fun main() {
    // test
    val test = listOf<Int>(1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50).toMutableList()
    processIter(test)

    val input = readLines("02/input")
    val instructions = input[0].split(',').map { it.toInt() }

    // part 1
    val mutableInstructions = instructions.toMutableList()
    preProcess(12, 2, mutableInstructions)
    processIter(mutableInstructions)
    println(mutableInstructions[0])

    // part 2
    for (noun in 1..99) {
        for (verb in 1..99) {
            val currentInstructions = instructions.toMutableList()
            preProcess(noun, verb, currentInstructions)
            processIter(currentInstructions)
            if (currentInstructions[0] == 19690720) {
                println("noun: $noun, verb: $verb")
                val solution = 100 * noun + verb
                println("Part 2 solution: $solution")
                break
            }
        }
    }

}

fun preProcess(noun: Int, verb: Int, instructions: MutableList<Int>) {
    instructions[1] = noun
    instructions[2] = verb
}

fun processIter(instructions: MutableList<Int>) {
    var opCode = 0
    var pos = 0
    while (opCode != 99) {
        val instr = instructions.slice(pos..pos + 3)
        opCode = instr[0]
        val firstOpIdx = instr[1]
        val secondOpIdx = instr[2]
        val outputIdx = instr[3]
        when (opCode) {
            1 -> instructions[outputIdx] = instructions[firstOpIdx] + instructions[secondOpIdx]
            2 -> instructions[outputIdx] = instructions[firstOpIdx] * instructions[secondOpIdx]
        }
        pos += 4
    }
}

fun readLines(filename: String) = File(filename).useLines { it.toList() }

package adventofcode

import java.io.File
import java.lang.IllegalArgumentException

fun main() {
    val input = readLines("05-kotlin/input")
    val instructions = input[0].split(',').map { it.toInt() }.toMutableList()
    processIter(instructions) // part 1
}

fun processIter(instructions: MutableList<Int>) {
    var opCode = 0
    var pos = 0
    while (opCode != 99) {
        val paramModes = extractOpCodeParamModes(instructions[pos])
        opCode = paramModes[0]

        val lastPos = when (opCode) {
            1, 2 -> pos + 3
            3, 4 -> pos + 1
            99 -> pos
            else -> throw IllegalArgumentException("Illegal opcode: $opCode")
        }
        val instrSet = instructions.slice(pos..lastPos)

        when (opCode) {
            1 -> instructions[instrSet.last()] = paramValue(paramModes, 1, instrSet, instructions) + paramValue(paramModes, 2, instrSet, instructions)
            2 -> instructions[instrSet.last()] = paramValue(paramModes, 1, instrSet, instructions) * paramValue(paramModes, 2, instrSet, instructions)
            3 -> instructions[instrSet.last()] = 1
            4 -> println(instructions[instrSet.last()])
        }
        pos = lastPos + 1
    }
}

private fun paramValue(paramModes: MutableList<Int>, paramNumber: Int, currentInstr: List<Int>, instructions: MutableList<Int>): Int =
        if (paramModes.getOrElse(paramNumber) { _ -> 0 } == 0) instructions[currentInstr[paramNumber]] else currentInstr[paramNumber]


fun extractOpCodeParamModes(instruction: Int): MutableList<Int> {
    return if (instruction < 10) {
        mutableListOf(instruction)
    } else {
        val instrStr = instruction.toString()
        val opCodeParamModes = mutableListOf(instrStr.takeLast(2).toInt())
        opCodeParamModes.addAll(instrStr.take(instrStr.length - 2).chunked(1).map { it.toInt() }.reversed())
        opCodeParamModes
    }
}

fun readLines(filename: String) = File(filename).useLines { it.toList() }

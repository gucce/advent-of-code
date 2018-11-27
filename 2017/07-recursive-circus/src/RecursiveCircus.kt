import java.io.File

fun main(args: Array<String>) {
    val input = readFileAsLines("recursive_cirucs_input")
    GraphAnalyzer(input).apply {
        println("The root program is: ${rootProgram()}")
    }

}

fun readFileAsLines(fileName: String): List<String> = File(fileName).readLines()

class GraphAnalyzer(private val input: List<String>) {

    fun rootProgram(): String {
        val programs = parseProgramList(input)
        return findRoot(programs.first().program, programs).name
    }

    private fun findParent(program: Program, programList: List<ProgramEntry>): Program? {
        return programList.find { pe -> pe.successors.contains(program.name) }?.program
    }

    private fun findRoot(program: Program, programList: List<ProgramEntry>): Program {
        val parent = findParent(program, programList)
        return if (parent == null) {
            program
        } else {
            findRoot(parent, programList)
        }
    }

    private fun parseProgramList(programLines: List<String>): List<ProgramEntry> {
        val basicProgramList = mutableListOf<ProgramEntry>()
        for (l in programLines) {

            val split = l.split(" -> ")
            var programStr: String
            var successors = ""
            when (split.size) {
                1 -> programStr = split[0]
                2 -> {
                    programStr = split[0]
                    successors = split[1]
                }
                else -> throw IllegalArgumentException("Line not formatted correctly: $l")
            }


            val (name, weight) = programStr.split(" ")
            val successorList = successors.trim().split(", ")
            val program = Program(name, weight.replace(Regex("(\\(|\\))"), "").toInt())
            basicProgramList.add(ProgramEntry(program, successorList))
        }
        return basicProgramList
    }

    data class Program(val name: String, val weight: Int)

    data class ProgramEntry(val program: Program, val successors: List<String>)

}

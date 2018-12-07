import java.io.File
import java.nio.charset.CharacterCodingException

fun readFileAsLines(fileName: String): List<String> = File(fileName).readLines()

fun main(args: Array<String>) {
    val testInput = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""

    val sumOfParts = SumOfParts()
    println(sumOfParts.findOrder(testInput.lines()))

    val input = readFileAsLines("input")
    println(sumOfParts.findOrder(input))
}

typealias DependencyMap = Map<String, List<String>>

class SumOfParts {

    private fun generateDependencyMap(inputList: List<String>): DependencyMap {
        val depPairs = inputList.map { Character.toString(it[36]) to Character.toString(it[5]) }
        val depMap = depPairs.asSequence()
                .groupBy { it.first }
                .mapValues { me -> me.value.map { p -> p.second }.sorted() }
                .toMutableMap()

        val letters = mutableSetOf<String>()
        depPairs.map {
            letters.add(it.first)
            letters.add(it.second)
        }

        // add empty lists for letters which do not have a dependency
        letters.filter { !depMap.containsKey(it) }
                .map { depMap.put(it, listOf()) }

        return depMap
    }

    internal fun findOrder(inputList: List<String>): String {
        val done = mutableListOf<String>()

        val depMap = generateDependencyMap(inputList)
        var mutDepMap = depMap
                .mapValues { me -> me.value.toMutableList() }
                .toMutableMap()

        while (!done.containsAll(mutDepMap.keys)) {
            val next = mutDepMap.asSequence()
                    .filter { it.key !in done } // not yet processed
                    .filter { it.value.isEmpty() } // no dependencies
                    .map { entry -> entry.key }
                    .sorted()
                    .first()
            done.add(next)
            mutDepMap.mapValues { it.value.remove(next) }
        }
        return done.joinToString(separator = "")
    }

}

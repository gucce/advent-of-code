import java.io.File
import kotlin.math.abs
import kotlin.test.assertEquals

val START = Pos(0, 0)

data class Pos(val x: Int, val y: Int)

fun main() {
    testPart1()
    testPart2()

    val input = readLines("03/input")

    val (firstWireInstructions, secondWireInstructions) = mapInput(input)

    // part 1
    println(part1(firstWireInstructions, secondWireInstructions))

    // part 2
    println(part2(firstWireInstructions, secondWireInstructions))
}

private fun part1(firstWireInstructions: List<String>, secondWireInstructions: List<String>): Int {
    val firstPath = path(firstWireInstructions)
    val secondPath = path(secondWireInstructions)
    val intersections = firstPath.intersect(secondPath).filter { it != START }
    return shortestDistance(START, intersections)
}

private fun part2(firstWireInstructions: List<String>, secondWireInstructions: List<String>): Int {
    val firstPath = path(firstWireInstructions)
    val secondPath = path(secondWireInstructions)
    return firstPath.intersect(secondPath)
            .filter { it != START }
            .map { fpos -> firstPath.indexOf(fpos) + secondPath.indexOf(fpos) }
            .min()!!
}

private fun mapInput(input: List<String>) = Pair(input[0].split(","), input[1].split(","))

private fun path(instructions: List<String>): List<Pos> {
    var current = START
    val path = mutableListOf<Pos>()
    for (i in instructions) {
        val line = line(i, current)
        current = line.last()
        path.addAll(line)
    }
    return path.distinct()
}

private fun readLines(filename: String) = File(filename).useLines { it.toList() }

private fun manhattanDist(posA: Pos, posB: Pos) = abs(posA.x - posB.x) + abs(posA.y - posB.y)

private fun shortestDistance(start: Pos, positions: Collection<Pos>): Int = positions.map { manhattanDist(start, it) }.min()!!

private fun line(instr: String, start: Pos): List<Pos> {
    val direction = instr[0].toString()
    val steps = instr.substring(1).toInt()

    return when (direction) {
        "R" -> (start.y..start.y + steps).map { Pos(start.x, it) }
        "U" -> (start.x..start.x + steps).map { Pos(it, start.y) }
        "L" -> (start.y downTo start.y - steps).map { Pos(start.x, it) }
        "D" -> (start.x downTo start.x - steps).map { Pos(it, start.y) }
        else -> throw IllegalArgumentException("Direction '$direction' cannot be mapped.")
    }
}

private fun testPart1() {
    println("Test Part 1")

    val test1Input = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    val (test1First, test1Second) = mapInput(test1Input.lines())
    assertEquals(159, part1(test1First, test1Second))

    val testInput2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    val (test2First, test2Second) = mapInput(testInput2.lines())
    assertEquals(135, part1(test2First, test2Second))
}

private fun testPart2() {
    println("Test Part 2")
    val test1Input = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
    val (test1First, test1Second) = mapInput(test1Input.lines())
    assertEquals(610, part2(test1First, test1Second))

    val testInput2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
    val (test2First, test2Second) = mapInput(testInput2.lines())
    assertEquals(410, part2(test2First, test2Second))
}

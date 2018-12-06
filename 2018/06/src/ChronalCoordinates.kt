import java.io.File

data class Coord(val x: Int, val y: Int)
data class Grid(val min: Coord, val max: Coord)

fun readFileAsLines(fileName: String): List<String> = File(fileName).readLines()

fun main(args: Array<String>) {
    val input = readFileAsLines("input.txt")
    val chronalCoordinates = ChronalCoordinates()
    val coordinates = chronalCoordinates.parseCoordinates(input)
    val distGrid = chronalCoordinates.shortestDistanceGrid(coordinates)
    val (coordIndex, area) = chronalCoordinates.biggestArea(distGrid, coordinates)
    println("Biggest area is $area for coordinates ${coordinates[coordIndex]}")

}

class ChronalCoordinates {

    fun biggestArea(distGrid: Map<Coord, Int>, coordinates: List<Coord>): Pair<Int, Int> {
        val maxGrid = maxGrid(coordinates)

        val edgeIds = distGrid.asSequence()
                .filter { isOnEdge(it.key, maxGrid) }
                .map { it.value }
                .toList()

        val mostNeighbors = distGrid.asSequence()
                .filter { it.value !in edgeIds }
                .groupBy { it.value }
                .maxBy { it.value.size }

        val area = mostNeighbors?.value?.size ?: throw IllegalStateException("No maximum found")
        val coordIndex = mostNeighbors.key

        return Pair(coordIndex, area)
    }

    private fun isOnEdge(coord: Coord, maxGrid: Grid) =
            coord.x in arrayOf(maxGrid.max.x, maxGrid.min.x)
                    || coord.y in arrayOf(maxGrid.max.y, maxGrid.min.y)


    fun shortestDistanceGrid(coordinates: List<Coord>): Map<Coord, Int> {
        val maxGrid = maxGrid(coordinates)
        val distGrid = mutableMapOf<Coord, Int>()

        // for every coordinate in the maximum grid
        for (x in maxGrid.min.x..maxGrid.max.x) {
            for (y in maxGrid.min.y..maxGrid.max.y) {
                val currentCoord = Coord(x, y)
                val nearestCoord = coordinates.asSequence()
                        .map { Pair(distance(currentCoord, it), it) }
                        .sortedBy { it.first } // distance
                        .toList()

                if (nearestCoord[0].first == nearestCoord[1].first) {
                    // more than one nearest coordinate
                    distGrid[currentCoord] = -1
                } else {
                    // add index within the coordinates list as reference
                    distGrid[currentCoord] = coordinates.indexOf(nearestCoord[0].second)
                }
            }
        }
        return distGrid
    }

    fun parseCoordinates(input: List<String>): List<Coord> =
            input.asSequence()
                    .map {
                        var coord = it.split(", ")
                        Coord(coord[0].toInt(), coord[1].toInt())
                    }
                    .toList()

    private fun distance(origin: Coord, dest: Coord): Int =
            Math.abs(origin.x - dest.x) + Math.abs(origin.y - dest.y)

    private fun maxGrid(coordinates: List<Coord>): Grid {
        val maxX = coordinates.maxBy { it.x }?.x
                ?: throw IllegalStateException("No maxX found in coordinate list: $coordinates")
        val maxY = coordinates.maxBy { it.y }?.y
                ?: throw IllegalStateException("No maxY found in coordinate list: $coordinates")
        val minX = coordinates.minBy { it.x }?.x
                ?: throw IllegalStateException("No minX found in coordinate list: $coordinates")
        val minY = coordinates.minBy { it.y }?.y
                ?: throw IllegalStateException("No minY found in coordinate list: $coordinates")
        return Grid(min = Coord(minX, minY), max = Coord(maxX, maxY))
    }
}

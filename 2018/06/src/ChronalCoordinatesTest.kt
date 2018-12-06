import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

internal class ChronalCoordinatesTest {

    @Test
    fun testBiggestArea() {
        val testInput = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

        val chronalCoordinates = ChronalCoordinates()
        val coordinates = chronalCoordinates.parseCoordinates(testInput.lines())
        val distGrid = chronalCoordinates.shortestDistanceGrid(coordinates)
        assertEquals(Pair(4, 17), ChronalCoordinates().biggestArea(distGrid, coordinates))
    }

}


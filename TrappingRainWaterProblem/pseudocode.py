function trapWater(height):

    totalWater = 0

    for each index i in height:

        leftMax = tallest bar from index 0 to i

        rightMax = tallest bar from index i to last index

        waterLevel = minimum(leftMax, rightMax)

        waterAtCurrentIndex = waterLevel - height[i]

        if waterAtCurrentIndex > 0:
            totalWater = totalWater + waterAtCurrentIndex

    return totalWater

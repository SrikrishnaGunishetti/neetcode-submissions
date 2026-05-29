class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        maxjloc = 0
        for i in range(len(height)):
            if i < maxjloc:
                continue
            maxj = 0
            for j in range(i + 1, len(height)):
                if height[j] >= height[i]:
                    maxj = height[j]
                    maxjloc = j
                    break 
                if height[j] > maxj:
                    maxj = height[j]
                    maxjloc = j
            if maxjloc > i:
                water_level = min(height[i], height[maxjloc])
                basin_area = 0
                for k in range(i + 1, maxjloc):
                    basin_area += water_level - height[k]
                total_water += basin_area
        return total_water
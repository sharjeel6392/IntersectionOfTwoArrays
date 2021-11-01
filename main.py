class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)
        intersection = []
        if len1 < len2:
            for i in range(len1):
                for j in range(len2):
                    if nums1[i] == nums2[j] and nums1[i] >= 0:
                        intersection.append(nums1[i])
                        nums1[i] = -1
                        nums2[j] = -1
            return intersection
        else:
            for i in range(len2):
                for j in range(len1):
                    if nums2[i] == nums1[j] and nums1[j] >= 0:
                        intersection.append(nums1[j])
                        nums1[j] = -1
                        nums2[i] = -1
            print(intersection)
            return intersection
        

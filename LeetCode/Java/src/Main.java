import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        // test here
    }
}

class Solution {
    public String addBinary(String a, String b) {
        if (a.length() == 1) {
            if (Integer.parseInt(a) == 0) {
                return b;
            }
        }
        if (b.length() == 1) {
            if (Integer.parseInt(b) == 0) {
                return a;
            }
        }

        int[] aArr = new int[a.toCharArray().length];
        int[] bArr = new int[b.toCharArray().length];
        int temp = 0;

        int i = aArr.length - 1;
        int j = bArr.length - 1;

        while (i >= 0 && j >= 0) {
            if (aArr.length > bArr.length) {
                aArr[i] = Character.getNumericValue(a.charAt(i)) +
                        Character.getNumericValue(b.charAt(j)) + temp;
                if (aArr[i] > 1) {
                    aArr[i] = aArr[i] - 2;
                    temp = 1;
                } else {
                    temp = 0;
                }
            } else {
                bArr[j] = Character.getNumericValue(a.charAt(i)) +
                        Character.getNumericValue(b.charAt(j)) + temp;
                if (bArr[j] > 1) {
                    bArr[j] = bArr[j] - 2;
                    temp = 1;
                } else {
                    temp = 0;
                }
            }
            i--;
            j--;
        }
        while (i >= 0) {
            aArr[i] = Character.getNumericValue(a.charAt(i)) + temp;
            if (aArr[i] == 2) {
                aArr[i] = 0;
                temp = 1;
            } else {
                temp = 0;
            }
            i--;
        }
        while (j >= 0) {
            bArr[j] = Character.getNumericValue(b.charAt(j)) + temp;
            if (bArr[j] == 2) {
                bArr[j] = 0;
                temp = 1;
            } else {
                temp = 0;
            }
            j--;
        }

        char[] res;
        if (temp == 1) {
            if (aArr.length > bArr.length) {
                res = new char[aArr.length + 1];
                res[0] = 1 + '0';
                for (int x = 1; x < res.length; x++) {
                    res[x] = (char) (aArr[x - 1] + '0');
                }
            } else {
                res = new char[bArr.length + 1];
                res[0] = 1 + '0';
                for (int x = 1; x < res.length; x++) {
                    res[x] = (char) (bArr[x - 1] + '0');
                }
            }
            return String.valueOf(res);
        }

        if (aArr.length > bArr.length) {
            res = new char[aArr.length];
            for (int x = 0; x < aArr.length; x++) {
                res[x] = (char) (aArr[x] + '0');
            }
        } else {
            res = new char[bArr.length];
            for (int x = 0; x < bArr.length; x++) {
                res[x] = (char) (bArr[x] + '0');
            }
        }

        return String.valueOf(res);
    }

    public boolean canJump(int[] nums) {
        int canReach = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > canReach) {
                return false;
            }
            canReach = Math.max(canReach, i + nums[i]);
        }
        return true;
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int j = 0;
        while (j < n) {
            nums1[m + j] = nums2[j];
            j++;
        }
        Arrays.sort(nums1);
    }

    public int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;

        while (left <= right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public String countAndSay(int n) {
        String res = "1";
        int i = 1;
        while (i < n) {
            String temp = "";
            int j = 0;
            while (j < res.length()) {
                int count = 1;
                while (j + 1 < res.length() && res.toCharArray()[j] == res.toCharArray()[j + 1]) {
                    count += 1;
                    j += 1;
                }
                temp += count + "" + res.toCharArray()[j];
                if (j + 1 == res.length()) {
                    break;
                }
                j += 1;
            }
            res = temp;
            i += 1;
        }
        return res;
    }

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode res = new ListNode();
        ListNode tail = res;
        while (head.next != null) {
            if (head.val != head.next.val) {
                tail.val = head.val;
                tail.next = new ListNode();
                tail = tail.next;
            }
            head = head.next;
        }
        tail.val = head.val;
        return res;
    }

    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            }

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }

    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i] += 1;
            if (digits[i] == 10) {
                digits[i] = 0;
            } else {
                return digits;
            }
        }
        int[] res = new int[digits.length + 1];
        res[0] = 1;
        return res;
    }

    public int strStr(String haystack, String needle) {
        char[] str1 = haystack.toCharArray();
        char[] str2 = needle.toCharArray();

        for (int i = 0; i <= str1.length - str2.length; i++) {
            if (str1[i] == str2[0]) {
                for (int j = 0; j < str2.length; j++) {
                    if (str1[i + j] != str2[j]) {
                        break;
                    } else {
                        if (j == str2.length - 1) {
                            return i;
                        }
                    }
                }
            }
        }
        return -1;
    }

    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (flowerbed.length == 1) {
            if (flowerbed[0] == 0) {
                flowerbed[0] = 1;
                n -= 1;
            }
        } else {
            if (flowerbed[0] == 0 && flowerbed[1] == 0) {
                flowerbed[0] = 1;
                n -= 1;
            }
            for (int i = 1; i < flowerbed.length - 2; i++) {
                if (flowerbed[i] == 0) {
                    if (flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        n -= 1;
                    }
                }
            }
            if (flowerbed[flowerbed.length - 1] == 0 && flowerbed[flowerbed.length - 2] == 0) {
                flowerbed[flowerbed.length - 1] = 1;
                n -= 1;
            }
        }
        return n <= 0;
    }

    public boolean search1(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return true;
            }

            if ((nums[left] == nums[mid]) && (nums[right] == nums[mid])) {
                left++;
                right--;
            } else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return false;
    }

    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length - k];
    }

    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i - 1] == nums[i]) {
                return true;
            }
        }
        return false;
    }

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        char[] arr = s.toCharArray();
        List<Character> newArr = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            if (Character.isDigit(arr[i]) || Character.isLetter(arr[i])) {
                newArr.add(arr[i]);
            }
        }
        for (int i = 0; i < newArr.size() / 2; i++) {
            if (newArr.get(i) != newArr.get(newArr.size() - 1 - i)) {
                return false;
            }
        }
        return true;
    }

    public boolean isAnagram(String s, String t) {
        char arr[] = s.toCharArray();

        Arrays.sort(arr);
        s = new String(arr);

        arr = t.toCharArray();
        Arrays.sort(arr);
        t = new String(arr);

        return s.equals(t);
    }

    public int maxProfit(int[] prices) {
        int best = 0;
        int minPrice = prices[0];
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            if (prices[i] - minPrice > best) {
                best = prices[i] - minPrice;
            }
        }
        return best;
    }

    public boolean isPalindrome(int x) {
        char[] ch = Integer.toString(x).toCharArray();
        int len = ch.length;
        for (int i = 0; i < len / 2; i++) {
            if (ch[i] != ch[len - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}

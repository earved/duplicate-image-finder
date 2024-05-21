# Duplicate Image Finder

Simple python script to search for similar or identical images using cross-correlation. All possible rotations of the images are considerd.

Examplary Results:
<pre>
19 files: starting process...
1 checked / 0 duplicates
2 checked / 0 duplicates
3 checked / 0 duplicates
4 checked / 0 duplicates
5 checked / 0 duplicates
-->20221113_125339246_iOS - Kopie.jpg AND 20221113_125339246_iOS.jpg--> correlation: 0.9994604354609619
6 checked / 1 duplicates
7 checked / 1 duplicates
8 checked / 1 duplicates
9 checked / 1 duplicates
10 checked / 1 duplicates
11 checked / 1 duplicates
12 checked / 1 duplicates
13 checked / 1 duplicates
14 checked / 1 duplicates
15 checked / 1 duplicates
16 checked / 1 duplicates
17 checked / 1 duplicates
18 checked / 1 duplicates
19 checked / 1 duplicates
summary: 19 files checked / 1 files duplicates
=== highest corrcoeff values ===
corrcoeff: 0.999 -->20221113_125339246_iOS - Kopie.jpg AND 20221113_125339246_iOS.jpg
corrcoeff: 0.781 -->20221113_132559913_iOS.jpg AND 20221113_132604071_iOS.jpg
corrcoeff: 0.725 -->DSC03225.JPG AND DSC03226.JPG
corrcoeff: 0.642 -->20221112_161256152_iOS.jpg AND 20221112_161304207_iOS.jpg
corrcoeff: 0.548 -->DSC03224.JPG AND DSC03229.JPG
corrcoeff: 0.541 -->DSC03224.JPG AND DSC03228.JPG
corrcoeff: 0.541 -->DSC03233.JPG AND DSC03236.JPG
corrcoeff: 0.529 -->20221112_153913071_iOS.jpg AND 20221113_125339246_iOS.jpg
corrcoeff: 0.527 -->20221112_153913071_iOS.jpg AND 20221113_125339246_iOS - Kopie.jpg
20221113_125339246_iOS - Kopie.jpg  can potentially be deleted
Runtime: 38.8032 seconds
-->process finished
</pre>
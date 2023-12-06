# Part 1

Soil    Seed    Total
50      98      2
52      50      48
Calculate Soil for Seed 79

First Range = [ 98, 99 ], total = 2
79 doesnt fall in this range, skip

Second Range = ( Soil Start = 52 ) [ 50, 97 ], total = 48
79 falls in this category

so soil for seed 79 = 52 + 79 - 50
( SoilStart + SeedValue - SeedStart ) <= FORMULA

Calculate Fertilizer for Soil 14

Fert    Soil    Total
0       15      37
37      52      2
39      0       15
First Range = [ 15, 15 + 37 - 1 ] => [ 15, 51 ]
Second Range = [ 52, 53 ]
Third Range = [ 0, 14 ]


52 50 48
52 + 48 = 99 ( 52 included ) Soil
50 + 48 = 97 ( 50 included ) Seed

so seed 50 => 52
51 => 53
52 => 54
53 => 55

First Value in the Mapping is the value the previous one is mapping to

# Part 2

To Debug

Range 1 =  [ 41218238,   462709950  ]
Range 2 =  [ 1255413673, 1605944579 ]
Range 3 =  [ 944138913,  1195243719 ]
Range 4 =  [ 481818804,  715390783  ]
Range 5 =  [ 2906248740, 3172696372 ]
Range 6 =  [ 3454130719, 3504775048 ]
Range 7 =  [ 1920342932, 2048122653 ]
Range 8 =  [ 2109326496, 2648036258 ]
Range 9 =  [ 3579244700, 3846478050 ]
Range 10 = [ 4173137165, 4233317049 ]
So ranking is based on the count                                                  Ranking
Lets take this hand: AAAAA => Count of A = 5 therefore its a Five of a kind       7
AA8AA => Count of A = 4 therefore its Four of a kind                              6
23332 => Count of 3 = 3 and 2 = 2 therefore its a full house                      5
TTT98 => Count of T = 3 therefore Three of a kind                                 4
23432 => Count of 2 = 2 and Count of 3 = 2 therefore its Two Pair                 3
22134 => Count of 2 = 2 and thats its, thereofre its One Pair                     2
23456 => No dupes, therefore its High Card                                        1
The weakest hand will be ranked first and so on

If the count is equal to 5, therefore its five of a kind always
maxCount = 5 and totalLength = 1
Like this hand => AAAAA => Count( 'A' ) = 5. There can be no other hand with count = 5

For four of a kind
MaxCount = 4 and totalLength of the counter should be 2
For this hand => AA8AA, maxCount = Count(A) = 4 and totalLength of the counter is 2 => { A:4, 8:1 }

For a full house,
maxCount = 3, totalLength = 2
Like for this hand => 23332 => Counter => { 3:3, 2:2 } Length is 2, and the counter of both the elements is 3 and 2

For three of a kind => maxCount = 3 and totalLength = 3

For Two Pair => maxCount = 2 and values with maxCount == 2 and totalLength = 3

For One Pair => maxCount = 2 and totalLength = 4

For High Card, maxCount = 1 and totalLength = 1
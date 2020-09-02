pd_to_dict

This simple package is result of my continus fight in converting many-layered pandas DataFrames into
readable dict format (and passing that dict into JSON). In my opinion build-in function in pandas 
library are quite insuffcient for mutliindexed DataFrames, resulting in an object which is totally
unusable for human eye (if we does not know the context on what each value represnts). Furthermore
all index names are usually lost in the translation.

As we all know "Readability Counts", and belive me debbuging some calculation, where the only
clue is some numbers-packed JSON file can be a pain in the as.

Installation:

1) download repo
2) use pip install pd_to_dict inside downloaded folder
3) done

#### Parsing Algorithm

1. The given worksheets contains many bounding boxes. In some cases, it can be aligned very well
And other times, the boxes are scattered
2. From the look of the worksheet, it feels like bounding boxes create an island and ----> this can be solved with 
dfs - find all components algorithm
3. Thats what I have applied here, with a special logic for finding a border.
4. The openpyxl library helps in identifying the border style for a cell in worksheet --> which helps in making logic for border or not 
for a bounding box
5. Coupled with isBorder and dfs_find_components, the code to extract data from worksheet works pretty well, and I was able to parse all the data 


The outline of sheet looks like this 


|            |
|            |
|------------|
|            |
|------------|
                                                    |            |                            |            |
                                                    |            |
                                                    |------------|
                                                    |            |
                                                    |------------|
                                                    |            |
                                                    |------------|
                                                    |------------|
                    
        |            |
        |            |
        |------------|
        |            |
        |------------|
        |            |
        |------------|

Looking at the sheet like this makes it clear to solve parsing via dfs-find-components. And that works like a charm on the given data.


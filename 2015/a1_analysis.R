x <- read.table("a1_input.txt", header = F) %>% .[1,1]

cx <- x %>% strsplit(., "") %>% table

cx[1] - cx[2]

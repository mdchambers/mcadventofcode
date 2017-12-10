
require(readr)
require(magrittr)

# Part 1

dat <- read_file("day_01_input.txt")

vec_1 <- dat %>% strsplit(split = "") %>% unlist
vec_2 <- c(
  vec_1[2:length(vec_1)], 
  vec_1[1]
)

pair <- function(a,b){
  if(a == b){
    return(as.numeric(a))
  } else{
    return(0)
  }
}

total <- mapply(pair, vec_1, vec_2) %>% sum
print(total)

# Part 2

dat <- read_file("day_01_input.txt")

vec_1 <- dat %>% strsplit(split = "") %>% unlist
vec_3 <- c(
  vec_1[(length(vec_1) / 2 + 1):length(vec_1)],
  vec_1[1:(length(vec_1) / 2)]
)

total <- mapply(pair, vec_1, vec_3) %>% sum
print(total)

## Day 17

Algorithm:

* On water addition (W) @ pos (P): (initial state: settled)
  1. If area below P is clear:
     1. Add water @ P + [0,1]
     2. Set state to unsettled
     3. Propagate unsettled state backwards
  2. If area below P is blocked (clay or settled water):
     1. Search left and right for walls w/o drops
        1. If both true, add water left and right (settled)
        2. If either false, ad water left and right (unsettled)



function addWater(position)
  if area below is clear:
    addWater( position + [0,1] )
  if area below is solid or settled water:
    Add waters to right and left
    Check each new water for paths down
    If path down found:
      Set this row of waters to be unsettled
      addWater @ path down
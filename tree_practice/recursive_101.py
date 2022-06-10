# ......................................
# elementary recursion repetition

def rec_seq_up( N ):
    if N <= 0:
        return
    print( N, end = ' ' )
    rec_seq_up( N-1 )

def rec_seq_down( N ):
    if N <= 0:
        print("start returning from recursion,", end = ' ')
        return
    rec_seq_down( N -1  )
    print( N, end = ' ' )


# ......................................
# recursion repetition with branching

def rec_binary_in( N ):
    if N < 0:
        return
    rec_binary_in( N-1 )
    print( N, end = ' ' )
    rec_binary_in( N-1 )


def rec_binary_tree( N, depth ):
    if N < 0:
        return
    rec_binary_tree( N-1, depth+1 )
    print( " "*3*depth,  N )
    rec_binary_tree( N-1, depth+1 )


def rec_binary_tree2( currDepth, maxDepth ):
    if currDepth > maxDepth:
        return
    rec_binary_tree2( currDepth+1, maxDepth )
    print( " "*3*currDepth,  currDepth )
    rec_binary_tree2( currDepth+1, maxDepth)


# ----------------------------------------------------------------------------
#                M A I N   P R O G R A M
# ----------------------------------------------------------------------------


# ......................................
# elementary recursion repetition

rec_seq_up( 13 )
print()

#same without recursion
for i in range( 13, 0, -1 ):
    print( i, sep= '  ', end = ' ')

print('\n--------------------')

rec_seq_down( 13 )
print()


# ......................................
# recursion repetition with branching

rec_binary_tree( 4, 0 )
print()


rec_binary_in( 4 )
print()
print()


rec_binary_tree2( 0, 4 )
print()




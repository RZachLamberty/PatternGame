import scipy
import itertools


def sureOverlaps( numList, N ):
    """
    Given a list of numbers and size of the puzzle, determine if there
    are any squares which are certainly overlapping
    """
    
    numList = scipy.array( numList )
    L = len( numList )
    
    for (i,el) in enumerate( numList ):
        leftMostRightEnd = scipy.sum( numList[:i] ) + i + el
        rightMostLeftEnd = N - ( scipy.sum( numList[ i: ] ) + ( L - i - 1 ) ) + 1
        if rightMostLeftEnd <= leftMostRightEnd:
            print '{:>2} is between {:>2} and {:>2}'.format( el, rightMostLeftEnd, leftMostRightEnd )
    

    bins = [Bin(w)]

        # iterate through all items in original array
        for item in a:
            # Iterate through all bins. Breaks when item is inserted.
            for bin in bins:
                if (item <= bin.capacity()):
                    bin.insert(item)
                    break
            # Iterates through all bins and cannot find a fit.  Create new bin.
            else:
                bins.append(Bin(w, item))
        
        return bins
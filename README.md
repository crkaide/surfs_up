# Surfs Up

## Overview and background
Initial analysis was intended to secure investor backing from W. Avy and his board of directors for a Surf n' Shake shop on the island of Oahu, Hawaii.  Although the investor is enthusiastic about the opportunity, his involvement is contingent upon the site of the business, to be determined by weather analytics reporting precipitation and temperature from multiple weather reporting stations.  Datasets for analysis were provided by the investor.

Following initial analysis of a year's worth of data from August to August, the investor requested summary statistics of all available observations for the months of June and December, to inform the operational schedule.  Requested analysis is provided below.

## Results
_*Temperatures for June*_

![temps_june.png](https://github.com/crkaide/surfs_up/blob/main/temps_june.png?raw=true)

_*Temperatures for December*_

![temps_dec.png](https://github.com/crkaide/surfs_up/blob/main/temps_dec.png?raw=true)

## Summary
_*Code snip*_

The queries written to extract June and December data avoid importing datetime, and instead rely on the central element of the string date provided (that is, the -mm- from yyyy-mm-dd) to identify the necessary records (see snip below).  The resulting output does not need to be converted to a list, eliminating that step, if desired, from the challenge's required procedure.

![code_snip.png](https://github.com/crkaide/surfs_up/blob/main/code_snip.png?raw=true)

1.  While there are more observations available for the month of June, both series of information are robust (approx. 1,500 and 1,700 records for June and December respectively).  Although there is a dip in mean temperature from 74.9 (June) to 71.0 (December), this is a) as expected and b) not dramatic in a real-world sense.  Standard deviations for June and December are 3.26 and 3.75; average temperatures are therefore relatively stable in both months, and roughly equivalently stable as well.
2.  The contrast between minimum temperatures between both months is more dramatic than mean at 9 degrees (64 in June and 56 in December).  While the standard deviation and mean indicate that both months are likely favorable for year-round business, and both months are stable relative to each other as well as in general, downturns in December are likely to be more significant due to isolated temperature dips than they are in June.  That is--when it gets "cold" for June, business isn't likely to be hit that hard; when it gets "cold" in December, the steeper dip in temperature is likely to have a greater (negative) impact on sales than it would in June.
3.  The 1st quartile of observations accounts for the greatest dissimilarity between the two datasets (that is, differences in the 2nd and 3rd quartiles are 3 degrees each between June and December, while the difference in the 1st is 4 degrees).  This further supports the observation made in #2 above:  while June and December may be somewhat similarly warm as well as relatively stable, the volatility in December's temperatures is seen at the low end of the temperature spectrum.  Based on this analysis, Surf n' Shake would be well-advised to "brace for" the lowest temperature days in December, even as it remains open for business.

## Add'l analysis

1. two recommendations for further analysis / two add'l queries to gather more weather data for June and Dec
2. 
3.  If possible, additional analysis might supplement a temperature report with revenue as well as cost of operations data.  While the weather on Oahu is unlikely to be volatile enough even in December to justify any lengthy closures, Surf n' Shake might consider reducing its hours of operation for limited stretches of time in the winter months when the temperatures are expected to be lowest.







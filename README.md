logsample
=========

This algorithm lets you pick a random sample from a list of unknown size
and completes in O(n) time. The original assignment was to take a random 
sample of x lines from a (streaming) webserver log with at least x lines, 
without knowing it's length in advance. You MUST take exactly x samples 
and the likelihood of each line being picked MUST be equal. 


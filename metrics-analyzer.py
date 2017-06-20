import sys
import os

if len(sys.argv) < 1:
    print """Metrics analyzer
Usage: python metrics-analyzer.py file-with-metrics

Output: metrics_count metrics_len_avg metrics_len_max balast_count balast_len_avg balast_len_max
"""

min_len = os.environ.get('DISPLAY_METRICS_LEN_GREATER_THEN')
if min_len:
    min_len = int(min_len)

f = open(sys.argv[1], 'r')
metrics_count = 0
metrics_len = 0
metrics_max = 0
balast_count = 0
balast_len = 0
balast_max = 0
for l in f:
    if l == '' or l.startswith('# '):
        balast_count += 1
        balast_len += len(l)
        balast_max = max(balast_max, len(l))
    else:
        metrics_count += 1
        metrics_len += len(l)
        metrics_max = max(metrics_max, len(l))
        if min_len and len(l) > min_len:
            print l

print(" {} {} {} {} {} {}".format(metrics_count, metrics_len / metrics_count, metrics_max, balast_count, balast_len / balast_count, balast_max))

1- Datasource URL:
2- Merged 8 files: (3119345, 85)
3- Dropna + duplicates: 290162 rows removed, now 2829183 rows
4- Dropped 8 constant cols: [' Bwd PSH Flags', ' Bwd URG Flags', 'Fwd Avg Bytes/Bulk', ' Fwd Avg Packets/Bulk', ' Fwd Avg Bulk Rate', ' Bwd Avg Bytes/Bulk', ' Bwd Avg Packets/Bulk', 'Bwd Avg Bulk Rate']
5- Dropped 3 IP/Timestamp cols
6- Low variance removed: 9 cols
7- High correlation removed: 17 cols
8- Optimized numeric cols: 466.14MB → 263.58MB (↓43.5%)

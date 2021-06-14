
### Scripts

- `compute.py`: computes the avg. time of iterations.
- `times.yaml`: execution time of the analyzed epoch/iterations.
- `graphs.py`: plotting script.

### VMs Configuration

|  | vCPUs | Architecture | Memory (GiB) | Network performance | USD/hr (Linux) |
| --------- | - | ------ | ------ | --------- | ----- |
| c4.large  | 2 | x86_64 |  3.75  | Moderate  | 0.1   |
| c5.xlarge | 4 | x86_64 | 8      | -         | 0.17  |
| m4.large  | 2 | x86_64 | 8      | Moderate  | 0.1   |
| m5.xlarge | 4 | x86_64 | 16     | -         | 0.192 |

### Results

Output of `python3 compute.py`:

```console
Time is measured in seconds.
c4.large
  - avg step 02 - 11. rank=0: 1.0230
  - avg step 02 - 11. rank=1: 1.0234
  - avg step 01 - 02. rank=0: 1.2307
  - avg step 01 - 02. rank=1: 1.2341
  - Epoch rank=0:  1787.5243
  - Epoch rank=1:  1787.5243
c5.xlarge
  - avg step 02 - 11. rank=0: 0.3717
  - avg step 02 - 11. rank=1: 0.3716
  - avg step 01 - 02. rank=0: 1.8906
  - avg step 01 - 02. rank=1: 2.0166
  - Epoch rank=0:  657.2162
  - Epoch rank=1:  657.2162
m4.large
  - avg step 02 - 11. rank=0: 1.1457
  - avg step 02 - 11. rank=1: 1.1457
  - avg step 01 - 02. rank=0: 3.0730
  - avg step 01 - 02. rank=1: 3.1441
  - Epoch rank=0:  2000.5012
  - Epoch rank=1:  2000.5012
m5.xlarge
  - avg step 02 - 11. rank=0: 0.4138
  - avg step 02 - 11. rank=1: 0.4137
  - avg step 01 - 02. rank=0: 2.4336
  - avg step 01 - 02. rank=1: 2.4348
  - Epoch rank=0:  756.626457
  - Epoch rank=1:  756.626457
```

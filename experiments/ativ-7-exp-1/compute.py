import yaml


def T_MS_avg(T_mx, T_my):
    # Estimate for step 2 - 11
    rank0_avg = sum(T_mx[1:10])/10
    rank1_avg = sum(T_my[1:10])/10

    # Estimate for step 1 - 2
    rank0_s12 = (T_mx[0] + T_mx[1])/2
    rank1_s12 = (T_my[0] + T_my[1])/2

    return rank0_avg, rank1_avg, rank0_s12, rank1_s12


def Main():
    with open('times.yaml') as sq:
        t = yaml.safe_load(sq)

    M = ['c4.large', 'c5.xlarge', 'm4.large', 'm5.xlarge']
    print('Time is measured in seconds.')
    for i in range(4):
        x0,x1,y0,y1 = T_MS_avg(t[i][M[i]][0]['rank_0'][0]['it'],
                               t[i][M[i]][1]['rank_1'][0]['it'])

        epoch_t_r0 = t[i][M[i]][0]['rank_0'][1]['epoch']
        epoch_t_r1 = t[i][M[i]][0]['rank_0'][1]['epoch']

        print(M[i])
        print('  - avg step 02 - 11. rank=0: {:5.4f}'.format(x0))
        print('  - avg step 02 - 11. rank=1: {:5.4f}'.format(x1))
        print('  - avg step 01 - 02. rank=0: {:5.4f}'.format(y0))
        print('  - avg step 01 - 02. rank=1: {:5.4f}'.format(y1))
        print('  - Epoch rank=0: ', epoch_t_r0[0])
        print('  - Epoch rank=1: ', epoch_t_r1[0])

if __name__ == '__main__':
    Main()

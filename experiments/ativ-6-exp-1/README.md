## Atividade 6

### Step 01: Creating an image base to run the experiments.

We created a Virtual Machine (VM) on Amazon AWS 
following the stpes **3.3.2** from the tutorial: [Introdução à Computação de Alto Desempeno 
na Nuvem Computacional](http://wscad.sbc.org.br/2018/anais/wscad-2018-minicursos.pdf).

The choosen configurations of the VM are the following:
- Ubuntu Server 20.04 LTS (HVM), SSD Volume Type.
- m5.large 2 (vCPUs) 8 Memory (GiB).
- Size (GiB) 16 General Purpose SSD (gp2).

After launch the VM and connect via SSH. We run the following commands:

#### #01: Installing Docker

```console
sudo apt-get update
sudo apt-get install apt-transport-https \
    ca-certificates \
    curl gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

#### #02: Building the Application

Clone the repository [Deep Convolution Generative Adversarial Networks](https://github.com/eborin/Distributed-DCGAN):

```console
git clone https://github.com/eborin/Distributed-DCGAN
```

and follow the README for the installation.

#### #03: RSA key Configuration

```console
ssh-keygen
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

After this, we close the terminal and follow the steps **3.3.4.4** and **3.3.4.5** from the
tutorial we reference in Step 01 to create an base image (AMI). We terminate the instance
after that.

## Step 02: Creating Instances

In this step we follow the tutorial from **3.3.4.6** and launch 2 instances based on 
the AMI previously created. The instances have the following configuration:

- m5.large 2 (vCPUs) 8 Memory (GiB).
- Size (GiB) 16 General Purpose SSD (gp2).

After create the instances and selected the the same security group we run the application

## Step 03: Running the Application

We launch and connect via SSH in both instances with user `ubuntu` 
instead of `root`, and run the following commands:

- Terminal 01:
```console
cd Distributed-DCGAN
sudo docker run --env OMP_NUM_THREADS=2 --rm --network=host -v=$(pwd):/root dist_dcgan:latest python -m torch.distributed.launch --nproc_per_node=1 --nnodes=2 --node_rank=0 --master_addr="172.31.22.51" --master_port=1234 dist_dcgan.py --dataset cifar10 --dataroot ./cifar10 --num_epochs 1 --batch_size 16 --max_workers 2
```

- Terminal 02:
```console
cd Distributed-DCGAN
sudo docker run --env OMP_NUM_THREADS=2 --rm --network=host -v=$(pwd):/root dist_dcgan:latest python -m torch.distributed.launch --nproc_per_node=1 --nnodes=2 --node_rank=1 --master_addr="172.31.22.51" --master_port=1234 dist_dcgan.py --dataset cifar10 --dataroot ./cifar10 --num_epochs 1 --batch_size 16 --max_workers 2
```

where `--master_addr="172.31.22.51"` is the private IPv4 IP address of the master machine (node_rank=0).

## Report

We report the following in the executed experiments:

[epoch: 0/1][iteration: 1562/1563][rank: 0] Loss_D: 0.2744, Loss_G: 5.5915, D(x): 0.9900, D(G(z)): 0.2249 / 0.0048, iteration time: 0.4708s
[rank: 0] Epoch 0 took: 1203.6375 seconds

[epoch: 0/1][iteration: 1562/1563][rank: 1] Loss_D: 0.3023, Loss_G: 5.5915, D(x): 0.9633, D(G(z)): 0.2249 / 0.0048, iteration time: 0.4696s
[rank: 1] Epoch 0 took: 1203.6388 seconds

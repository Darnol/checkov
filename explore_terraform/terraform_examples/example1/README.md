This example1 contains a very simple example which explores the usage of foreach and count to specify multiple resources at once.
The subnets are created by specifying foreach or count. The instances a and b are hardcoded.

Expected output
5 Resources
- vpc
- subnet1
- subnet2
- instance_a
- instance_b

4 Edges
- subnet1 -> vpc
- subnet2 -> vpc
- instance_a -> subnet1
- instance_b -> subnet2

There are 3 variants how to specify this cound of subnet 1 and 2
- foreach and locals is manually hardcoded (see file ex1_tf_graph_foreach_manual.dot)
- foreach and locals uses a loop (see file ex1_tf_graph_foreach_loop.dot)
- count = 2 in subnets (see file ex1_tf_graph_count.dot)

The 3 mentioned dot files were created by actually running terraform init, apply and graph.

### Checkov
Of course, the goal is to use checkov and not having to apply terraform.
What does checkov say about the 3 variants:

#### count = 2 in subnets
Misses the edges of instance -> subnet

#### foreach and locals is manually hardcoded
This is the only variant that works, subnets are references by string name "subnet1" and "subnet2"

#### foreach and locals uses a loop
Does not work at all, cannot parse the loop structure
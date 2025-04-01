provider "aws" {
  region = "us-east-2"
}
resource "aws_vpc" "vpc" {
  cidr_block = "10.30.0.0/16"
  tags = {
    Name = "vpc"
  }
}

/* hardcoded locals
locals {
  subnets = {
    subnet1 = "10.30.1.0/24"
    subnet2 = "10.30.2.0/24"
  }
}
*/

// loop for locals, avoid using count
locals {
  subnet_count = 2
  subnet_base  = "10.30"

  subnets = {
    for i in range(local.subnet_count) : 
    "subnet${i + 1}" => "${local.subnet_base}.${i + 1}.0/24"
  }
}

resource "aws_subnet" "subnet" {
  for_each   = local.subnets
  vpc_id     = aws_vpc.vpc.id
  cidr_block = each.value
  tags = {
    Name = each.key
  }
}
resource "aws_instance" "instance_a" {
  ami           = "ami-08be1e3e6c338b037"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet["subnet1"].id
  tags = {
    Name = "instance A"
  }
}
resource "aws_instance" "instance_b" {
  ami           = "ami-08be1e3e6c338b037"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.subnet["subnet2"].id
  tags = {
    Name = "instance B"
  }
}

provider "aws" {
    region = "us-east-2"
}    
resource "aws_vpc" "vpc" {
    cidr_block = "10.30.0.0/16"
    tags = {
        name = "vpc"
    }
}
resource "aws_subnet" "subnet" {
    count = 2
    vpc_id = aws_vpc.vpc.id
    cidr_block = element(
        ["10.30.1.0/24","10.30.2.0/24"],
        count.index
    )
    tags = {
        name = "subnet-${count.index+1}"
    }
}
resource "aws_instance" "instance_a" {
    ami            = "ami-08be1e3e6c338b037"
    instance_type  = "t2.micro"
    subnet_id      = aws_subnet.subnet[0].id
    tags = {
        name = "instance_a"
    }
}
resource "aws_instance" "instance_b" {
    ami            = "ami-08be1e3e6c338b037"
    instance_type  = "t2.micro"
    subnet_id      = aws_subnet.subnet[1].id
    tags = {
        name = "instance_b"
    }
}

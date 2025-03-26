provider "aws" {
    region = "us-east-2"
}    
resource "aws_vpc" "vpc" {
    cidr_block = "10.30.0.0/16"
    tags = {
        Name = "vpc"
    }
}
resource "aws_subnet" "subnet" {
    vpc_id     = aws_vpc.vpc.id
    cidr_block = "10.30.1.0/24"
    tags = {
        Name = "subnet-0"
    }
}
resource "aws_instance" "instance_a" {
    ami            = "ami-08be1e3e6c338b037"
    instance_type  = "t2.micro"
    subnet_id      = aws_subnet.subnet.id
    tags = {
        Name = "instance A"
    }
}
resource "aws_instance" "instance_b" {
    ami            = "ami-08be1e3e6c338b037"
    instance_type  = "t2.micro"
    subnet_id      = aws_subnet.subnet.id
    tags = {
        Name = "instance B"
    }
}
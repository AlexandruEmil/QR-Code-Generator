provider "aws" {
  region = "us-east-1"
  acces_key=""
  secret_key=""
}

resource "aws_instance" "qr_code_generator" {
  ami           = "ami-0c55b159cbfafe1f0"  # Ubuntu 18.04 LTS
  instance_type = "t2.micro"

  tags = {
    Name = "QRCodeGenerator"
  }

  # Asigură-te că instanța are acces la internet
  vpc_security_group_ids = [aws_security_group.qr_code_sg.id]
}

resource "aws_security_group" "qr_code_sg" {
  name_prefix = "qr_code_sg"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "public_ip" {
  value = aws_instance.qr_code_generator.public_ip
}
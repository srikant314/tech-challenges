output "lb_dns_name" {
  description = "The DNS name of the load balancer"
  value       = aws_lb.ext-elb.dns_name
}

# Python Infrastructure Health Monitor

A lightweight Python script designed to actively monitor network health. It uses the native `socket` library to perform TCP connectivity tests on critical infrastructure IPs and ports, identifying potential outages or firewall blocks.

## Features
- TCP Port scanning and validation
- Configurable timeout and sleep intervals
- Plain text alerting for open/closed ports
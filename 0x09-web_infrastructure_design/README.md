# 0x09. Web Infrastructure Design

## Introduction
This project focuses on designing web infrastructures with a DevOps and SysAdmin perspective. The tasks involve creating diagrams, explaining components, and addressing specific requirements related to web server design, load balancing, security, and monitoring.

## Team Members
- Akram Boutzouga

## Tasks Overview

### 0. Simple Web Stack
- **Design:** Single-server web infrastructure with LAMP stack.
- **Key Components:**
  - 1 server, 1 Nginx web server, 1 application server, 1 MySQL database.
  - Domain: www.foobar.com
- **Issues:**
  - Single Point of Failure (SPOF).
  - Downtime during maintenance.
  - Limited scalability.

![Screenshot](https://imgur.com/a/H3vcRkH)

### 1. Distributed Web Infrastructure
- **Design:** Three-server web infrastructure with load balancer (HAProxy).
- **Additional Elements:**
  - 2 servers, 1 HAProxy load balancer, 1 MySQL database.
- **Load Balancer:**
  - Configured with Round Robin algorithm for even distribution.
  - Active-Active setup for load balancing.
- **Database:**
  - Primary-Replica (Master-Slave) cluster.
- **Issues:**
  - SPOF, Security issues (no firewall, no HTTPS), No monitoring.

![Screenshot](https://imgur.com/a/tIC64Fv)

### 2. Secured and Monitored Web Infrastructure
- **Design:** Three-server web infrastructure with security measures and monitoring.
- **Additional Elements:**
  - 3 firewalls, 1 SSL certificate, 3 monitoring clients.
- **Security Measures:**
  - Firewalls for traffic filtering.
  - SSL certificate for encrypted traffic.
- **Monitoring:**
  - Sumo Logic for data collection.
- **Issues:**
  - SSL termination at the load balancer level.
  - Single MySQL server for writes.
  - Servers with identical components.

![Screenshot](https://imgur.com/a/44ju6kE)

### 3. Scale Up (Advanced)
- **Readme:** Explanation of application server vs web server.
- **Additional Elements:**
  - 1 server, 1 HAProxy load balancer configured as a cluster.
  - Components split across different servers.
- **Explanation:**
  - Details added for each additional element.
- **Issues:**
  - (Not specified in the task, but can be discussed during review).

![Screenshot](https://imgur.com/a/OLXhSAu)



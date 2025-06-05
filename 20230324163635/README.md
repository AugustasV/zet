# Fault Domains and Fault Levels: AWS vs. Azure

**What’s a Fault Domain?**  
A fault domain is a part of a data center (like a rack of servers or a whole room) where, if something breaks (like power or network), only that section is affected. The main idea: failures don’t “spill over” and mess up everything else[1].

**What’s a Fault Level?**  
A fault level is just a group of fault domains. Think of it as a bigger box containing smaller boxes (fault domains).

---

### How AWS and Azure Do It Differently

| Cloud        | Fault Level (Big Group)         | Fault Domain (Small Group)                  | Extra Concepts      |
|--------------|---------------------------------|---------------------------------------------|--------------------|
| **AWS**      | Region (e.g., us-east-1)        | Availability Zone (e.g., us-east-1a)        | —                  |
| **Azure**    | Region (e.g., East US)          | Availability Zone or Fault Domain           | Update Domain      |

- **AWS:**  
  - A Region is the big area (fault level), made up of multiple Availability Zones (fault domains).  
  - If one zone fails, others keep working[1].

- **Azure:**  
  - Uses both Availability Zones (like AWS) and Fault Domains (inside an Availability Set).  
  - Fault Domains are racks or groups of servers with shared power/network.  
  - Azure also has *Update Domains*—these are for planned maintenance, so not all your servers reboot at once[2][3][5][6].

---

**In short:**  
- Both AWS and Azure split their data centers to limit failures.
- AWS calls the big group a Region, small group an Availability Zone.
- Azure uses Regions too, but also has Fault Domains (hardware groups) and Update Domains (for updates), so failures and maintenance don’t take everything down at once.

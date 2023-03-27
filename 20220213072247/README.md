# Dependencies scanning
Dependencies check for software is very important thing to catch vulnerabilities
as fast as possible.
Vulnerabilities are introduced through plugins, libraries etc.
---
Most popular ones in industry is Snyk and Dependabot(GitHub)
Snyk Scans:
* containers
* dependencies
* Terraform code
* Auto fixes
Dependabot do only dependencies check. It's by default on GitHub, and only
available on GitHub.

Also, popular alternative is to use AquaSecurity open source tool: Trivy
Have GitHub Actions, good integration with GitHub Security section.

* https://www.aquasec.com/products/trivy/
* https://snyk.io/plans/
*

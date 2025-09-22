# 🌐 AI-CloudSec-System
*A collaborative learning project to build a cloud-based security system with AI, Snowflake, and AWS.*

---

## 📖 Overview
Our goal is to design and implement a **cloud-based security platform** that integrates:
- AI models for **spam detection** and **threat detection**
- **Honeypots** for intrusion research
- **Firewalls, IDS, and IPS** for network security
- **Cloud monitoring tools** (AWS CloudTrail, GuardDuty, Snowflake analytics)
- **Threat modeling frameworks** like **STRIDE, DREAD, and MITRE ATT&CK**

The project combines **theory** (cybersecurity frameworks) and **practice** (cloud engineering + AI).

---

## 🎯 Objectives
- Build **cloud-native security practices** (AWS, Snowflake).
- Develope **AI-based threat detection** (ML models for spam, anomaly detection).
- Deploy and monitor **honeypots** to study attacks.
- Implement and configure **firewalls, IDS, IPS**.
- Apply **threat modeling** frameworks: STRIDE, DREAD, MITRE.
- Develop collaboratively using **GitHub workflows, issues, and pull requests**.

---

## 🏗️ Project Structure

```
/docs         → Design docs, threat models (STRIDE/DREAD), MITRE mappings
/models       → AI/ML models for spam & anomaly detection
/honeypot     → Honeypot configs and scripts
/ids_ips      → IDS/IPS setup and configurations
/firewall     → AWS Security Groups, firewall rules
/monitoring   → CloudTrail, GuardDuty, and logging configs
/snowflake    → SQL scripts, pipelines, dashboards
```

---

## Getting Started

### 1. Ensure git lfs is installed
```bash
git lfs install
```
If not installed, please review the document for [Installing Git Large File Storage](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage) before cloning the repository.

### 2. Clone the repo
```bash
git clone https://github.com/<your-org>/CloudSec-AI-Lab.git
cd CloudSec-AI-Lab
```

### 3. Set up environment
- Install Python 3.10+
- Create a virtual environment:
  ```bash
  python -m venv .venv
  source .venv/bin/activate   # Mac/Linux
  .venv\Scripts\activate      # Windows
  ```
- Install dependencies (to be listed in `requirements.txt`).

### 4. Cloud Setup
- AWS Free Tier account (for CloudTrail, GuardDuty, EC2 honeypots).
- Snowflake free trial account (for analytics + queries).

---

## 📚 Learning Tasks for Students

- [ ] Deploy **CloudTrail** and **GuardDuty** on AWS.
- [ ] Implement a simple **honeypot** (e.g., Cowrie SSH honeypot).
- [ ] Train a **spam detection model** (Naive Bayes, Logistic Regression).
- [ ] Connect **Snowflake** to store & query logs.
- [ ] Document threats using **STRIDE/DREAD**.
- [ ] Map scenarios to **MITRE ATT&CK tactics**.

---

## Contribution Guidelines

1. **Fork** the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/my-feature
   ```
3. Commit changes with clear messages.
4. Submit a **Pull Request** for review.
5. Add/update documentation in `/docs`.

---

## Roles
- **AI Team** → Develop ML models for spam & anomaly detection.
- **Cloud Team** → Manage AWS, Snowflake, and infrastructure security.
- **Threat Modeling Team** → Apply STRIDE, DREAD, and MITRE ATT&CK.
- **Monitoring Team** → Deploy honeypots, IDS/IPS, and logging systems.

---

## Security Note
This repository is under continuous development, so please do not deploy insecure configurations in production environments.

---

## References
- [AWS CloudTrail Docs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS GuardDuty Docs](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Snowflake Tutorials](https://docs.snowflake.com/en/user-guide)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)

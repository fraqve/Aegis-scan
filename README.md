Aegis-Scan

A Python-based CLI security scanner for network reconnaissance and threat intelligence enrichment.


Overview
Aegis-Scan is a modular command-line security tool built for blue team workflows. It combines active network scanning with threat intelligence APIs to help analysts quickly assess hosts, identify open services, and enrich findings with reputation data — all from a single interface.
Built as part of a hands-on cybersecurity portfolio, Aegis-Scan is designed with real-world DFIR and threat hunting use cases in mind.

Features

Network scanning — Host discovery and service detection via Nmap (-sV)
Threat intelligence enrichment — IP and file reputation lookups via VirusTotal and AbuseIPDB
AI-assisted analysis — Automated finding summarization via Google Gemini API
Structured reporting — Clean, readable output saved to report files
Modular architecture — Separate modules for scanning, analysis, and reporting


Installation
Requirements

Python 3.8+
Nmap installed on your system
API keys for VirusTotal, AbuseIPDB, and Google Gemini

Steps

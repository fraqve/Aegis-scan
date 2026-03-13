import json
import requests
from google import genai

GEMINI_PROMPT = """
You are a senior cybersecurity analyst reviewing automated scan results. 
You do not greet, explain yourself, or add preamble. You analyze the data and report directly.

Given the following scan data, produce a structured security assessment with these sections:
You will also receive VirusTotal and AbuseIPDB reputation scores for the target IP. Factor these into your risk assessment.
RISK LEVEL: [CRITICAL / HIGH / MEDIUM / LOW / INFORMATIONAL]

VULNERABILITIES IDENTIFIED:
- List each finding with CVE if applicable, service/port affected, and a one-line technical description.

TECHNICAL ANALYSIS:
- Explain what the findings mean in context. What is exposed? What could an attacker do with this?

RECOMMENDATIONS:
- Concrete, prioritized remediation steps. Be specific (e.g. "Disable SSLv3 on Apache via SSLProtocol directive" not "update your SSL").

ANALYST NOTES:
- Anything anomalous, worth investigating further, or that changes the risk picture.

Rules:
- No filler phrases ("Great question", "Certainly", "As an AI").
- No markdown formatting beyond the section headers above.
- If data is insufficient to assess a finding, say so plainly and state what additional data is needed.
- Treat every open port, banner, and header as potential attack surface.
"""


def load_config(config_file:str):
    with open(config_file) as file:
        config = json.load(file)
    return config



def check_virustotal(ip:str,api:str):
    data = {
        "malicious": 0,
        "suspicious": 0,
        "harmless": 0,
        "undetected": 0,
        "error": None
    }

    try:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"

        headers = {
            "accept": "application/json",
            "x-apikey":api
        }


        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            raw_stats = response.json()
            target_stats = raw_stats["data"]["attributes"]["last_analysis_stats"]

            for key in target_stats:
                if key != "timeout":
                    data[key] = target_stats[key]
            return data
        

        else:
            data["error"] = f"Error:{response.status_code}"
            return data


    except requests.ConnectionError:
        data["error"] = "Error: No internet connexion"
        return data

    except Exception as e:
        data["error"] = f"An error has occured: {e}"
        return data





def check_abuseipdb(ip:str,api:str):
    data = {
        "abuseConfidenceScore": 0,
        "error": None
    }

    try:
        url = f"https://api.abuseipdb.com/api/v2/check"
        query_params = {
            "ipAddress":ip,
            "maxAgeInDays": "90"
        }

        query_headers = {
            'Accept': 'application/json',
            'Key': api
        }

        response = requests.get(url,headers=query_headers,params=query_params)

        if response.status_code == 200:
            raw_data = response.json()
            data["abuseConfidenceScore"] = raw_data["data"]["abuseConfidenceScore"]
            return data
        
        else:
            data["error"] = f"Error:{response.status_code}"
            return data

    except requests.ConnectionError:
        data["error"] = "Error: no internet connexion"
        return data

    except Exception as e:
        data["error"] = f"An error has occured: {e}"
        return data




def ask_gemini(report:str,api:str):
    try:
        client = genai.Client(api_key=api)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{GEMINI_PROMPT}\n {report}",
        )

        if response.text != None:
            return response.text
        else:
            return "Gemini generated nothing."

    except Exception as e:
        return f"Error: {e}"



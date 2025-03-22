# Resume Builder

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Overview

Resume Builder is a Streamlit-based web application that allows users to create professional resumes easily. The application guides users through a step-by-step process to input their information, and then generates a well-formatted PDF resume.

## Features

- User-friendly interface with a step-by-step form
- Sections for personal information, education, work experience, and skills
- Ability to add multiple education entries
- Skills input with comma-separated values, formatted as bullet points in the final PDF
- PDF generation with a clean, professional layout
- Responsive design using Streamlit components

## Requirements

- Python 3.7+
- Streamlit
- ReportLab
- streamlit-antd-components

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/resume-builder.git
   cd resume-builder
   ```

2. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:

   ```
   streamlit run main.py
   ```

2. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

3. Follow the step-by-step process to input your information:

   - Basic Information
   - Education
   - Work Experience
   - Skills

4. In the final step, click "Generate Resume PDF" to create and download your resume.

## Project Structure

```
resume-builder/
├── .streamlit
├    └── config.toml
├── views
├    ├── app.py
├    └── welcome.py
├── main.py              # Main Streamlit application
├── requirements.txt     # List of Python dependencies
└── README.md            # Project documentation (you are here)

```

## Customization

You can customize the resume layout and styling by modifying the `generate_pdf` function in `app.py`. The function uses ReportLab to create the PDF, so you can adjust fonts, colors, spacing, and more to match your preferences.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![](https://mermaid.ink/img/pako:eNp1lNuO2yAQhl8FceWVEuU-F62S2Dl0c7CcXalbuxesPXGobLAAdxNFefcO5ISSlAsLM9_8_DDAgeayANqnpWLNlryFmSDYdPt5GnjXoMhMGFAsN1yKU9i2Qepi700lWaFJArqt4bcXJ93uNzIMHBUzbUCTH_KThKBzxRsr9nKjh44eHWIlc9AXue_HEwGiyMSds5FUQM44F-VNaoRS5ANns4phGjOl4dFe6MJRGu2MXRoZtlUFhsSSC6M9LnLc-Mq9wv5LqsJHxg6ZpCMFzACZzxfWV90Yj5k4ZpqucSnnKDHSsh40ddA8TSAH_tea_lLcGBD_dXfu3S1-KZ3QK5rmvom5G16kIddNxfZkzWteMZwCuzlu5wO6TK-lRztRwQ3utEctHbU6jFtltljmBDZcQA3CXCpn28ovyMR3u_LdPpR6kPYy-uSQkSAOx71wNfr5ktHe2U5oYb_WSO0XrSNlvvPIyJJPy06CBErY9ZK2Au1ljP2MywEgAfaGUfJGukTzuqnQJ2saJVm-9XInNvfhZJBgpXjJBavODjr3d6NzncgTm1qxxyNEgsGMDOIZOtlIdXLDcyyrl3r5ZmZpRZ7UtU8GeQ6N6SXwB3Ch67YsQVsv2srQDq1B1YwX-FocrFxGseg1ZLSP3QI2rK1MRjNxRJS1Rq73Iqd9o1roUCXbckv7G1Zp_GubAvcj5Ayvcn0dbZj4JeXtH9CXVIvT--SeqeM_sB5taQ?type=png)](https://mermaid.live/edit#pako:eNp1lNuO2yAQhl8FceWVEuU-F62S2Dl0c7CcXalbuxesPXGobLAAdxNFefcO5ISSlAsLM9_8_DDAgeayANqnpWLNlryFmSDYdPt5GnjXoMhMGFAsN1yKU9i2Qepi700lWaFJArqt4bcXJ93uNzIMHBUzbUCTH_KThKBzxRsr9nKjh44eHWIlc9AXue_HEwGiyMSds5FUQM44F-VNaoRS5ANns4phGjOl4dFe6MJRGu2MXRoZtlUFhsSSC6M9LnLc-Mq9wv5LqsJHxg6ZpCMFzACZzxfWV90Yj5k4ZpqucSnnKDHSsh40ddA8TSAH_tea_lLcGBD_dXfu3S1-KZ3QK5rmvom5G16kIddNxfZkzWteMZwCuzlu5wO6TK-lRztRwQ3utEctHbU6jFtltljmBDZcQA3CXCpn28ovyMR3u_LdPpR6kPYy-uSQkSAOx71wNfr5ktHe2U5oYb_WSO0XrSNlvvPIyJJPy06CBErY9ZK2Au1ljP2MywEgAfaGUfJGukTzuqnQJ2saJVm-9XInNvfhZJBgpXjJBavODjr3d6NzncgTm1qxxyNEgsGMDOIZOtlIdXLDcyyrl3r5ZmZpRZ7UtU8GeQ6N6SXwB3Ch67YsQVsv2srQDq1B1YwX-FocrFxGseg1ZLSP3QI2rK1MRjNxRJS1Rq73Iqd9o1roUCXbckv7G1Zp_GubAvcj5Ayvcn0dbZj4JeXtH9CXVIvT--SeqeM_sB5taQ)

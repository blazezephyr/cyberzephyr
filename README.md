# Blaze Zephyr

A highly customizable phishing tool for educational purposes only. Blaze Zephyr contains a comprehensive collection of phishing email templates for popular social media platforms and services.

## ⚠️ Educational Purpose Only

This tool is intended strictly for educational and testing purposes. Users are responsible for ensuring compliance with applicable laws and regulations. The developers are not responsible for any misuse of this software.

## 🚀 Features

- **Multiple Platform Support**: Instagram, Facebook, Gmail, Twitter, Snapchat, Steam, and more
- **Customizable Templates**: Fully customizable phishing email templates
- **Device & Browser Emulation**: Support for various device and browser combinations
- **IP Location Options**: Custom IP addresses or pre-generated location options
- **Redirect Bypass**: Built-in redirect page creation capabilities
- **Enhanced Error Handling**: Comprehensive error handling and logging
- **User-Friendly Interface**: Intuitive command-line interface with color support

## 📋 Supported Platforms

### Social Media
- Instagram
- Facebook
- Gmail (Standard & Simple)
- Twitter
- Snapchat (Standard & Simple)
- Discord
- Spotify
- LinkedIn

### Gaming & Entertainment
- Steam
- Playstation
- Riot Games
- Rockstar Games
- AskFM

### Financial & Business
- PayPal
- Blockchain

### Web Services
- Dropbox
- 000Webhost
- Gamehag
- Mega

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository:**
   ```bash
   https://github.com/blazezephyr/cyberzephyr.git
   cd cyberzephyr
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python3 CyberPhish.py
   ```

### Manual Dependency Installation
If requirements.txt installation fails, install manually:
```bash
pip install colorama rgbprint
```

## 📖 Usage

1. **Launch the application:**
   ```bash
   python3 CyberPhish.py
   ```

2. **Select a phishing template** from the main menu by entering the corresponding number

3. **Enter target information** when prompted:
   - Target name
   - Target email
   - Phishing URL
   - Additional platform-specific details

4. **Choose device and browser** options for enhanced realism

5. **Select IP location** (custom or pre-generated)

6. **Save the generated HTML file** to your desired location

## 🎯 Advanced Features

### Custom Device Selection
- Choose from predefined device/browser combinations
- Enter custom device and browser specifications
- Optimize templates for specific targets

### IP Location Options
- Use custom IP addresses with location details
- Select from pre-generated IPs with country/city information
- Enhance credibility with geographically relevant data

### Redirect Bypass
- Create redirect pages for phishing campaigns
- Customizable redirect timing and destinations
- Built-in template generation

## 🔧 Configuration

### Logging
All errors and exceptions are logged to `blaze_zephyr.log` for debugging purposes.

### Customization
- Modify templates in `Core/eletter.py`
- Add new platforms by following existing function patterns
- Customize colors and styling in `Core/helper/color.py`

## 🐛 Error Handling

Blaze Zephyr includes comprehensive error handling:

- **Input Validation**: Validates all user inputs for proper format
- **Exception Handling**: Graceful handling of system errors and exceptions
- **Logging**: Detailed error logging for troubleshooting
- **User Feedback**: Clear error messages and recovery options

## 📁 Project Structure

```
Blaze-Zephyr/
├── CyberPhish.py              # Main application entry point
├── Core/
│   ├── pre.py                 # Core utilities and banner
│   ├── eletter.py             # Email template functions
│   ├── devicemenu.py          # Device selection menu
│   ├── ipmenu.py              # IP selection menu
│   └── helper/
│       ├── color.py           # Color utilities
│       ├── date.py            # Date utilities
│       ├── Banners.py         # Banner displays
│       └── RedirectBypass.py  # Redirect bypass functionality
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For support and questions:
- Check the error logs in `blaze_zephyr.log`
- Review the troubleshooting section below
- Create an issue on GitHub for bugs or feature requests

## 🔍 Troubleshooting

### Common Issues

**Module Import Errors:**
```bash
# Install missing dependencies
pip install colorama rgbprint
```

**Permission Errors:**
- Run the application with appropriate permissions
- Check file write permissions for output directory

**Display Issues:**
- Ensure terminal supports ANSI color codes
- Try running without rgbprint if display issues persist

### Debug Mode
Enable verbose logging by setting environment variable:
```bash
export BLAZE_ZEPHYR_DEBUG=1
python3 CyberPhish.py
```

## ⚡ Performance Tips

- Use SSD storage for faster file operations
- Ensure sufficient RAM for large template operations
- Close unnecessary applications while running

## 🔐 Security Notes

- Never share generated phishing files with unauthorized individuals
- Store templates securely when not in use
- Regularly update dependencies for security patches
- Use in isolated environments when possible

## 📄 License

This project is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Original CyberPhish project contributors
- Python security community
- Educational cybersecurity community

## 📊 Version History

### Version 2.2 (Blaze Zephyr)
- Enhanced error handling throughout
- Improved user interface
- Additional platform support
- Better logging and debugging capabilities

---

**⚠️ Disclaimer**: This tool is for educational purposes only. Users must comply with all applicable laws and regulations. The developers are not responsible for any misuse of this software.

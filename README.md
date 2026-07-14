# Account Auth - Django OTP Authentication

A comprehensive Django-based implementation demonstrating how One-Time Passwords (OTP) are created, stored, and used for secure website login authentication.

## 📋 Overview

This project showcases a complete OTP authentication system built with Django. It covers the entire lifecycle of OTP-based authentication including:
- OTP generation and validation
- Secure storage of OTP credentials
- User registration and login flows
- Session management with OTP verification

## 🎯 Features

- **OTP Generation**: Secure one-time password generation using industry-standard algorithms
- **User Authentication**: Complete user registration and login system
- **OTP Validation**: Time-based and counter-based OTP verification
- **Session Management**: Secure session handling after OTP verification
- **Responsive UI**: HTML templates for seamless user experience
- **Django Integration**: Built with Django best practices and conventions

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS
- **Database**: Django ORM (configurable)
- **Authentication**: OTP-based security

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/lazyskiddie/account_auth.git
   cd account_auth
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings**
   - Update `settings.py` with your database configuration
   - Set up secret keys and allowed hosts

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` in your browser to access the application.

## 🔐 How OTP Authentication Works

### User Registration
1. User provides email and password
2. System generates a secret key for OTP generation
3. Secret is stored securely in the database

### OTP Generation
1. User requests OTP during login
2. System generates a time-based or counter-based OTP
3. OTP is displayed or sent to user (depending on configuration)

### Login Flow
1. User enters credentials
2. User receives/retrieves OTP
3. User enters OTP for verification
4. System validates OTP against stored secret
5. Session is created upon successful verification

## 📁 Project Structure

```
account_auth/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── account_auth/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── auth/                  # Authentication app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│       ├── login.html
│       ├── register.html
│       └── otp_verify.html
└── static/
    ├── css/
    └── js/
```

## 🚀 Usage

### Register a New User

1. Navigate to the registration page
2. Enter your email and password
3. System generates and displays your OTP secret
4. Save your secret in an authenticator app (Google Authenticator, Authy, etc.)

### Login with OTP

1. Go to login page
2. Enter your email and password
3. When prompted, enter the 6-digit OTP from your authenticator app
4. Upon successful verification, you'll be logged in

## 🔑 Security Considerations

- **Secret Storage**: OTP secrets are encrypted and securely stored
- **Time Window**: OTP validation includes time windows to account for clock skew
- **Rate Limiting**: Failed OTP attempts are rate-limited
- **Session Tokens**: Session tokens expire after a configurable duration
- **HTTPS**: Always use HTTPS in production

## 📚 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | GET, POST | User login |
| `/verify-otp/` | POST | Verify OTP |
| `/logout/` | GET | User logout |
| `/dashboard/` | GET | Protected user dashboard |

## 🧪 Testing

Run tests with:
```bash
python manage.py test
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

For issues, questions, or suggestions:
- Open an issue on [GitHub Issues](https://github.com/laskylazyddie/account_auth/issues)
- Check existing documentation and examples

## 📚 References

- [Django OTP Documentation](https://django-otp-official.readthedocs.io/)
- [RFC 6238 - TOTP](https://tools.ietf.org/html/rfc6238)
- [Django Security](https://docs.djangoproject.com/en/stable/topics/security/)

---

Built with ❤️ using Django

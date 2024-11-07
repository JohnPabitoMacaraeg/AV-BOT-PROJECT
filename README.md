
# Django Appointment Booking System

This project is a web-based appointment booking system developed using Django. It provides users with the ability to browse services, book appointments, and complete purchases either online or on-site. Registered and unregistered users can view available slots and book appointments by filling in the required details. The system also includes email verification and various payment options.

## Features

1. **User Registration and Login**
   - Users can register to create an account and log in.
   - Password recovery and update options are available for registered users.

2. **Appointment Booking**
   - Both registered and unregistered users can book appointments.
   - Users can view available time slots and select a preferred date and time for their appointments.

3. **Cart Management**
   - Registered users can add items to a cart for easy checkout later.
   - The system saves the cart for logged-in users.

4. **Checkout and Payment Options**
   - Users can proceed to checkout directly from the cart.
   - Options for on-site or delivery-based appointments are available.
   - Payment options include cash (on-site) and online payment for deliveries.

5. **Verification Process**
   - The system requires email verification to confirm bookings.
   - Failed email verifications prompt a manual verification step by staff.
   
6. **Admin and Staff Functions**
   - Staff can manually book and cancel appointments.
   - Cancellations and successful bookings update the database in real time.

## Project Structure

- **`views.py`**: Contains view logic for managing pages like registration, login, appointment booking, and checkout.
- **`models.py`**: Defines the database structure for storing user, appointment, and transaction details.
- **`forms.py`**: Contains Django forms for user registration, login, and booking forms.
- **`urls.py`**: Maps URLs to their corresponding views.
- **`templates/`**: Holds HTML files for frontend pages.
- **`static/`**: Contains CSS, JavaScript, and image assets for the UI.

## Installation

### Prerequisites
- Python 3.x
- Django
- SQLite (default) or PostgreSQL (for production)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd django-appointment-booking
   ```

2. **Set Up Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - By default, the project uses SQLite. You can switch to PostgreSQL or another database by editing `settings.py`.

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and go to `http://127.0.0.1:8000`.

## Usage

1. **Homepage**: Users can view services and available slots.
2. **Registration/Login**: Allows users to create accounts and log in.
3. **Booking**:
   - Select preferred date and time.
   - Input necessary details and confirm.
   - Email verification is required for successful booking.
4. **Payment Options**:
   - For on-site bookings, users can choose cash payment.
   - For delivery bookings, online payment is available.
5. **Admin Features**: Admin or staff can manually book and cancel appointments, as well as update user details.

## Database Structure

- **User Information**: Stores registered user details and login credentials.
- **Appointments**: Manages bookings, time slots, and user-specific appointment data.
- **Transactions**: Logs payment and order information.
- **Verification Logs**: Tracks email and manual verifications.

## Workflow

1. **User Registration and Login**: The user can register or log in to access the booking feature.
2. **Appointment Selection**: Choose a date and time, add details, and add to the cart.
3. **Checkout Process**:
   - On-site or delivery options are available.
   - Payment choices depend on the booking type.
4. **Verification and Completion**:
   - Users verify bookings via email.
   - Manual verification by staff is available in case of verification failure.

## Built With

- **Django** - The web framework used
- **SQLite** - Default database for development
- **PostgreSQL** (Optional) - For production deployment
- **HTML/CSS** - Frontend styling and layout
- **JavaScript** - For interactive components and validation

## License

This project is licensed under the MIT License. See `LICENSE` for more information.


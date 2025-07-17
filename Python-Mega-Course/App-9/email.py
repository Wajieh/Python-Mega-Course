import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import filetype  # pip install filetype

password = "nkky yphf dlqb wvoo"
sender = "wajiehbadr@gmail.com"
receiver= "wajiehbadr@gmail.com"

def send_email(image_path):
    print('Preparing email...')
    
    # Create message container
    msg = MIMEMultipart()
    msg['Subject'] = 'New Customer'
    msg['From'] = sender
    msg['To'] = receiver
    
    # Add text body
    msg.attach(MIMEText('New customer has arrived', 'plain'))
    
    # Add image attachment
    with open(image_path, 'rb') as f:
        img_data = f.read()
        
        # Determine image type
        kind = filetype.guess(img_data)
        if kind is None:
            print("Warning: Could not determine image type, defaulting to png")
            img = MIMEImage(img_data, _subtype='png')
            img.add_header('Content-Disposition', 'attachment', filename='customer.png')
        else:
            img = MIMEImage(img_data, _subtype=kind.extension)
            img.add_header('Content-Disposition', 'attachment', filename=f'customer.{kind.extension}')
        
        msg.attach(img)

    # Send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {str(e)}')

if __name__ == '__main__':
    send_email('images/1.png')
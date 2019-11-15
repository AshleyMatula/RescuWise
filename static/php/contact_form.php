<?php
/*
* Booking form mail
*/
?>

<?php

    if (isset($_POST['submit_reservation'])) {
        $to = 'support@themeslr.com';
        $form_user_name = $_POST['contactName'];
        $form_user_email = $_POST['contactEmail'];
        $form_user_phone = $_POST['contactPhone'];
        $form_user_subject = $_POST['contactSubject'];

        $message = '';
        $message .= "Reservation for: " .  $form_user_name . "\r\n";
        $message .= "Email: " . $form_user_email . "\r\n";
        $message .= "Phone: " . $form_user_phone . "\r\n";
        $message .= "Time: " . $form_user_time . "\r\n";
        $message .= "Subject: " . $form_user_subject;
        $message .= "\r\n" . "\r\n";

        $headers = 'From: ' . $form_user_name . '<'. $form_user_email . '>';
        if( mail( $to, $form_user_subject, $message, $headers ) ) {
            #echo "<p>Your email has been sent! Thank you</p>";
        }
    }

?>
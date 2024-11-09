Biometric Device Integration v18 This module integrates Odoo attendance with biometric device attendance.

Features Integrates biometric device(Face+Thumb) with HR attendance. Managing attendance automatically Keeps zk machine history in Odoo Option to configure multiple zk devices Option to clear all zk history from both device and Odoo API feature for integrating with other systems Technical Notes Used Libraries:

zklib you can install zklib library using "sudo pip install zklib" API Documentation The API feature allows you to integrate this module with other systems. The API endpoint is /api/zk_device and it accepts the following methods:

GET: Retrieves a list of all configured zk devices POST: Creates a new zk device configuration PUT: Updates an existing zk device configuration DELETE: Deletes a zk device configuration Compatible Devices This module support with the following machines :

Testing Status This module is currently under testing for different models. It may work with some models but not others. Please report any issues or successes to the author.

Author Dr. Sabry Youssef https://www.vetbrains.com Credits Developer: Dr. Sabry Youssef, sabry.youssef@vetbrains.com

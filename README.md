# Network-Based-Malicious-Activity-Detection

Design and implement a network-based security monitoring system for a local area network (LAN). The system consists of a server and multiple clients. The server monitors client activity, including the titles of active browser windows and clipboard contents, and cross-references this data with a predefined list of malicious URLs and programs stored in a CSV file. If the server detects any potentially malicious activity, it takes appropriate action, such as terminating the offending program or blocking access to the malicious URL. The system aims to enhance network security by proactively identifying and addressing suspicious behavior on client computers within the LAN.  




**Project Overview:**

1. **Client-Server Architecture:** 🕊️ This project features a classic client-server setup, where two distinct programs communicate over a network (in this case, a local area network or LAN).

2. **Network Communication:** 🌐 The client and server chat using sockets, virtual conduits for network chatter. Sockets enable data exchange between these two entities, facilitating their digital dialogue.

3. **Server-Side Functionality:**
   - The server 🏰 catches incoming data from the client and does some serious thinking.
   - Armed with a list of possibly suspicious URLs and programs, stored in a CSV file 📋, the server plays detective.
   - It investigates the incoming data against this sneaky list to catch any malevolent mischief.
   - If the server sniffs out trouble, it's ready to jump into action (in this demo, just some printed alerts).

4. **Client-Side Functionality:**
   - The client 👤 perpetually keeps an eye out for certain activities on its own turf.
   - It's particularly interested in the title of the browser window 🌐 and the secrets stashed in the clipboard 📋.
   - Whenever these activities change, the client swiftly dispatches these updates to the server for a verdict.

5. **Security and Monitoring:** 🔒🔍 The project serves as a mini watchdog. It's like a digital guardian angel, identifying potential bad deeds—like venturing into harmful websites or fiddling with iffy software.

**Key Learning Points:**

- **Network Communication:** 🌐 You master the art of establishing a connection between two parties over a network, employing the mystical power of sockets. 🧙‍♂️

- **CSV Data Handling:** 📋 The project showcases a skill essential for data enthusiasts—reading data from CSV files, a kind of digital spreadsheet.

- **Platform Independence:** 💼 The server script flaunts its adaptability, capable of functioning across diverse platforms like Windows 🪟 and Unix-like systems 🐧.

- **Basic Monitoring:** 🔎 The client script lays the groundwork for more sophisticated monitoring systems. It's like dipping your toes into the vast ocean of monitoring possibilities.

**Project Scope and Enhancements:**

- Building more advanced monitoring techniques and security checks is like leveling up your skills in a video game 🎮. You're the hero of your own code adventure!

- Dressing up the client with a stylish user interface 🖥️ for easy interaction and dazzling reports.

- Adding extra pizzazz by implementing actions like shutting down pesky programs, blocking naughty websites, or sending out dramatic alarms 🔥🚨.

- Bolstering security measures to lock down the communication between the client and server is like constructing an unbreachable fortress.

- Scaling up the system to handle multiple clients at once is like hosting a mega party, ensuring everyone gets their turn to chat.

- Transforming the system into a historical data archive for security audits is like preserving a digital history book 📜 for future generations to explore.


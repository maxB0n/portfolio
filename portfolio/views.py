from django.shortcuts import render


def index(request):
    experience = [
        {
            'title': 'Electronics Lead',
            'org': 'NYU Rogue Aerospace',
            'location': 'Brooklyn, NY',
            'date': 'Sept 2025 – Present',
            'bullets': [
                'Direct the electronics subteam by managing multiple concurrent projects and personnel, ensuring all systems are fully functional and rigorously tested prior to strict competition deadlines.',
                'Mentor and onboard incoming members, providing technical guidance to help them seamlessly adjust to the team\'s workflow and collaborative culture.',
                'Develop and integrate the rocket\'s flight computer, payload system, and live telemetry to ensure precise launch control and data collection for New York\'s second-ever hybrid propulsion rocket.',
                'Build and maintain ground station support equipment (GSE) for launching and remotely controlling the rocket.',
            ],
        },
        {
            'title': 'Volunteer',
            'org': 'Bread of Life Food Pantry',
            'location': 'Long Island City, NY',
            'date': 'Summers 2024 & 2025',
            'bullets': [
                'Provided respectful and efficient service in the distribution of food to 100+ families weekly.',
                'Trained new volunteers on outstanding customer service and pantry procedures.',
                'Resolved supply shortages by finding alternative solutions and organized inventory.',
            ],
        },
        {
            'title': 'Lead – Semester Long Design Project',
            'org': 'NYU Tandon',
            'location': 'Brooklyn, NY',
            'date': 'Sept 2023 – Dec 2023',
            'bullets': [
                'Led the development of a wearable safety device capable of tracking and sharing user locations.',
                'Implemented and soldered hardware components for device assembly and operation.',
                'Ensured project deadlines were met while maintaining high-quality standards.',
            ],
        },
    ]

    projects = [
        {
            'title': 'Rocket Ground Station Equipment (GSE)',
            'date': 'Feb 2026 – Present',
            'bullets': [
                'Designed a two-way communication architecture using XBee radio modules for reliable wireless telemetry.',
                'Engineered a secure ground station interface to transmit critical launch and abort commands.',
                'Developed data parsing and logging protocols for live system health monitoring and post-flight analysis.',
            ],
            'tags': ['XBee', 'Wireless', 'Telemetry', 'Python', 'Radio'],
        },
        {
            'title': 'Automated Payload Ejection System',
            'date': 'Nov 2026 – Present',
            'bullets': [
                'Programmed an Arduino flight computer to autonomously synchronize a stepper motor and servo-actuated valve for precise, simultaneous fluid ejection.',
                'Integrated a custom rack-and-pinion linkage with electronics to safely expel the water payload mid-flight.',
                'Conducted bench testing to calibrate motor torque, synchronize servo-valve actuation, and validate control logic timing under simulated loads.',
            ],
            'tags': ['Arduino', 'C++', 'Servo', 'Stepper Motor', 'Motor Driver'],
        },
        {
            'title': 'Full-Stack Django E-Commerce Engine',
            'date': 'April 2025',
            'bullets': [
                'Developed a dynamic web application using the MVT (Model-View-Template) architecture to manage product inventories, shopping carts, and customer orders.',
                'Engineered a session-based shopping cart system to manage persistent state across user sessions without requiring immediate database writes.',
                'Designed a relational database schema using Django ORM and SQLite to handle complex relationships between products, categories, and customer order records.',
                'Implemented a responsive, mobile-first frontend using Bootstrap 5, focusing on UI/UX principles for intuitive navigation and distraction-free checkout flows.',
                'Managed the development lifecycle through Git/GitHub, utilizing systematic branching and committing to maintain code integrity and version history.',
            ],
            'tags': ['Python', 'Django', 'SQLite', 'Bootstrap 5', 'Git'],
        },
        {
            'title': 'Full-Stack Airline Reservation System',
            'date': 'Fall 2025',
            'bullets': [
                'Designed and developed a comprehensive airline reservation web application using Python, Flask, and MySQL for the NYU Tandon Intro to Databases course.',
                'Engineered a robust relational database schema to manage airports, flights, airplanes, and ticketing, utilizing complex SQL JOINs and subqueries for dynamic seat availability and sales analytics.',
                'Integrated secure MD5 password hashing, session management, and role-based access control to support distinct, secure portals for both customers and airline administrators.',
            ],
            'tags': ['Python', 'Flask', 'MySQL', 'Relational Databases', 'Web Dev'],
        },
        {
            'title': 'Portable Safety Device',
            'date': 'Sept 2023 – Dec 2023',
            'bullets': [
                'Programmed in C++ for real-time location updates and user distress signaling.',
                'Conducted debugging and testing to ensure hardware and software functionality under various conditions.',
            ],
            'tags': ['C++', 'Arduino', 'KiCAD'],
        },
    ]

    skills = {
        'Programming & Software': ['C++', 'Python', 'Verilog', 'SQL', 'SQLite', 'phpmyadmin', 'Git', 'Django', 'Arduino IDE', 'OOP', 'Databases'],
        'Hardware & Prototyping': ['Altium', 'KiCAD', 'PCB Design', 'Schematic Capture', 'Circuit Design', 'Soldering'],
        'Testing & Analysis': ['Oscilloscopes', 'Multimeters', 'Signal Analysis', 'Data Structures & Algorithms'],
        'Soft Skills': ['Problem Solving', 'Cross-Functional Collaboration', 'Technical Communication', 'Project Leadership', 'Time Management'],
    }

    coursework = [
        'Electronics', 'Computer Architecture', 'Object-Oriented Programming', 'Databases',
        'Data Structures & Algorithms', 'Probability & Statistics', 'Discrete Mathematics',
        'Calculus III', 'Linear Algebra', 'Differential Equations',
    ]

    context = {
        'experience': experience,
        'projects': projects,
        'skills': skills,
        'coursework': coursework,
    }
    return render(request, 'portfolio/index.html', context)

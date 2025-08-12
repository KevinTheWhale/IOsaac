IOsaac – Interactive Online Solution Archive for Calculus

IOsaac is a Django-based web application that provides a searchable, structured archive of worked solutions for Calculus: Early Transcendentals (7th ed.) by James Stewart.

The platform is designed to make solution lookup simple, fast, and organized — allowing users to navigate by chapter, section, and problem number.
It also supports multiple solutions per problem, resource reference pages (e.g., tables of integrals), and a moderation system for community uploads.

Key Features
	•	Structured Navigation: Browse problems by chapter, section, and problem number.
	•	Multiple Solutions per Problem: Displays all approved solution images in one view.
	•	Admin-Editable Content: Home, About, and Resource pages are fully manageable via the Django admin panel.
	•	Upload & Moderation System: Users can submit solutions, which are stored for admin/moderator approval before publication.
	•	Resource Pages: Includes supplemental learning resources like tables of integrals and series tests.
	•	Search & Sorting: Sort problems and sections logically (e.g., 6.7 before 7.1).
	•	Spam-Protected Feedback System: Allows up to three feedback submissions per day per user, with a live word counter.
	•	Security Features: Upload filtering, SQL injection protection, and Django’s built-in XSS/CSRF defenses.

Technology Stack
	•	Backend: Django (Python)
	•	Frontend: HTML, CSS (custom styling for consistent UI across all pages)
	•	Database: SQLite (dev) / Compatible with PostgreSQL (prod)
	•	Other Tools: Pillow (image handling), MathJax (optional LaTeX rendering), Django Admin customization

Planned Enhancements
	•	Subject expansion (e.g., Probability Theory solutions)
	•	User accounts for tracking submitted solutions
	•	Improved search/filter functionality
	•	Secure file serving for downloadable resources

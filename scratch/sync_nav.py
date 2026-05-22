import os

def sync_nav():
    workspace_dir = "/Users/biancaremster/Desktop/Scrubb ATX/scrubb"
    
    for root, dirs, files in os.walk(workspace_dir):
        for file in files:
            if not file.endswith(".html"):
                continue
            
            # Skip referral.html since it is already correct
            if file == "referral.html":
                continue
                
            file_path = os.path.join(root, file)
            is_subpage = "areas" in root
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            # If the referrals page is already linked in this file, skip it
            if "referral.html" in content:
                print(f"Skipping {file} (already synced)")
                continue
                
            original_content = content
            
            if is_subpage:
                # Desktop Navigation update for subpages
                content = content.replace(
                    '<li><a href="../index.html#contact" class="nav-link">Contact</a></li>',
                    '<li><a href="../referral.html" class="nav-link">Referrals</a></li>\n                    <li><a href="../index.html#contact" class="nav-link">Contact</a></li>'
                )
                # Mobile Navigation update for subpages
                content = content.replace(
                    '<li><a href="../index.html#contact" class="mobile-nav-link">Contact</a></li>',
                    '<li><a href="../referral.html" class="mobile-nav-link">Referrals</a></li>\n            <li><a href="../index.html#contact" class="mobile-nav-link">Contact</a></li>'
                )
                # Footer Company column update for subpages
                content = content.replace(
                    '<li><a href="../index.html#service-areas">Service Areas</a></li>',
                    '<li><a href="../index.html#service-areas">Service Areas</a></li>\n                            <li><a href="../referral.html">Referral Program</a></li>'
                )
            else:
                # Desktop Navigation update for root pages
                content = content.replace(
                    '<li><a href="#contact" class="nav-link">Contact</a></li>',
                    '<li><a href="referral.html" class="nav-link">Referrals</a></li>\n                    <li><a href="#contact" class="nav-link">Contact</a></li>'
                )
                content = content.replace(
                    '<li><a href="index.html#contact" class="nav-link">Contact</a></li>',
                    '<li><a href="referral.html" class="nav-link">Referrals</a></li>\n                    <li><a href="index.html#contact" class="nav-link">Contact</a></li>'
                )
                # Mobile Navigation update for root pages
                content = content.replace(
                    '<li><a href="#contact" class="mobile-nav-link">Contact</a></li>',
                    '<li><a href="referral.html" class="mobile-nav-link">Referrals</a></li>\n            <li><a href="#contact" class="mobile-nav-link">Contact</a></li>'
                )
                content = content.replace(
                    '<li><a href="index.html#contact" class="mobile-nav-link">Contact</a></li>',
                    '<li><a href="referral.html" class="mobile-nav-link">Referrals</a></li>\n            <li><a href="index.html#contact" class="mobile-nav-link">Contact</a></li>'
                )
                # Footer Company column update for root pages
                content = content.replace(
                    '<li><a href="#service-areas">Service Areas</a></li>',
                    '<li><a href="#service-areas">Service Areas</a></li>\n                            <li><a href="referral.html">Referral Program</a></li>'
                )
                content = content.replace(
                    '<li><a href="index.html#service-areas">Service Areas</a></li>',
                    '<li><a href="index.html#service-areas">Service Areas</a></li>\n                            <li><a href="referral.html">Referral Program</a></li>'
                )
                
            if content != original_content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Successfully synced: {file}")
            else:
                print(f"Failed to match sync patterns for: {file}")

if __name__ == "__main__":
    sync_nav()

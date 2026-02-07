# Needed for "base" packages
SUSEConnect -p sle-module-desktop-applications/15.3/x86_64

SUSEConnect --product sle-module-development-tools/15.3/x86_64

SUSEConnect --product sle-module-python2/15.3/x86_64

SUSEConnect --product sle-module-public-cloud/15.3/x86_64

SUSEConnect --product sle-module-legacy/15.3/x86_64

# Needed for X11/Desktop packages
SUSEConnect --product sle-we/15.3/x86_64 -r ADDITIONAL REGCODE

SUSEConnect --product PackageHub/15.3/x86_64

SUSEConnect --product sle-ha/15.3/x86_64 -r ADDITIONAL REGCODE



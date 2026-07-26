%global source0_hash 1997a00b6d82d189b65f6fd2a856a34992abc99e50d9ec463bbf1afb750d1765

Name:    sc
Version: 7.16
Release: 29%{?dist}
Summary: Spreadsheet Calculator

License: LicenseRef-Fedora-Public-Domain
URL:     http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/!INDEX.html
Source0: http://www.ibiblio.org/pub/Linux/apps/financial/spreadsheet/sc-%{version}.tar.gz

# These patches are from Debian, see:
# http://anonscm.debian.org/cgit/collab-maint/sc.git/tree/debian/patches?id=8d75b0ec9f761b5d5245290a79a20b409c442d52
Patch0:  Upstream-changes-from-old-versions.patch
Patch1:  function_definitions.patch
Patch2:  call_function_not_take_its_address.patch

# Patch for http://fedoraproject.org/wiki/Changes/FormatSecurity
Patch3:  format_security_fixes.patch

# https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1400274.html
Patch4:  nonotimeout-ncurses6.patch

BuildRequires: make
BuildRequires: gcc
BuildRequires: bison
BuildRequires: ncurses-devel

%description
Spreadsheet Calculator is a free curses-based spreadsheet program that uses key
bindings similar to vi and less.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%global build_type_safety_c 0
make all sc.1 psc.1 %{?_smp_mflags} CFLAGS="%{optflags} -DSYSV3 -std=gnu89"

%install
# The "install" target of upstream's makefile does not work, so install manually

# Binaries
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 sc %{buildroot}%{_bindir}
install -m 0755 psc %{buildroot}%{_bindir}

# Man pages
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -m 0644 sc.1 %{buildroot}%{_mandir}/man1
install -m 0644 psc.1 %{buildroot}%{_mandir}/man1

# Data
install -d -m 0755 %{buildroot}%{_datadir}/sc
install -m 0644 tutorial.sc %{buildroot}%{_datadir}/sc

%files
%doc CHANGES README SC.MACROS TODO
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/sc

%changelog
%autochangelog

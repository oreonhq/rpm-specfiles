%global source0_hash 83633d0e8a4f35810456d9d52261c8ae0beb9148276847cae8963505240fb2d5

Summary:        Utility to test Pluggable Authentication Modules (PAM)
Name:           pamtester
Version:        0.1.2
Release:        30%{?dist}
License:        BSD-3-Clause
URL:            https://pamtester.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         pamtester-configure-c99.patch
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pam-devel

%description
Pamtester is a tiny program to test the Pluggable Authentication Modules
(PAM) facility, which is a de facto standard of unified authentication
management mechanism in many Unixes and similar OSes including Solaris,
HP-UX, *BSD, MacOSX and Linux. While specifically designed to help PAM
module authors to test their modules, that might also be handy for system
administrators interested in building a centralised authentication system
using common standards such as NIS, SASL and LDAP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog

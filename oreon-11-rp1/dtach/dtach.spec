%global source0_hash 32e9fd6923c553c443fab4ec9c1f95d83fa47b771e6e1dafb018c567291492f3

Name: dtach
Version: 0.9
Release: %autorelease
Summary: A simple program that emulates the detach feature of screen

License: GPL-2.0-or-later
URL: http://dtach.sourceforge.net
Source: http://prdownloads.sourceforge.net/dtach/dtach-%{version}.tar.gz

# Fix build with GCC 15
# https://github.com/crigler/dtach/pull/21.patch
Patch: 21.patch

BuildRequires: gcc
BuildRequires: make

%description
dtach is a program that emulates the detach feature of screen, with
less overhead. It is designed to be transparent and un-intrusive; it
avoids interpreting the input and output between attached terminals
and the program under its control. Consequently, it works best with
full-screen applications such as emacs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 dtach %{buildroot}%{_bindir}/dtach
install -m 644 dtach.1 %{buildroot}%{_mandir}/man1/dtach.1

%files
%doc README
%license COPYING
%{_bindir}/dtach
%{_mandir}/*/dtach.*

%changelog
%autochangelog

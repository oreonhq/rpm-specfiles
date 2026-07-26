%global source0_hash 0d5c86656efbb6c2efdeed730cff8e5109bd075139ce55542072cbda0ad2f7b9

Name: regionset
Version: 0.2
Release: 28%{?dist}
Summary: Reads/sets the region code of DVD drives
URL: http://linvdr.org/projects/regionset/
Source: http://linvdr.org/download/regionset/%{name}-%{version}.tar.gz
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

BuildRequires: make
BuildRequires:  gcc
%description
regionset will show you the current region code of the drive, how often it
has been changed and how many changes are left. If there are any changes
left, it asks for the new region code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%{__make} CC="gcc $RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 $RPM_BUILD_ROOT%{_sbindir}
install -p -m755 %{name} $RPM_BUILD_ROOT%{_sbindir}

%files
%doc debian/changelog COPYING README
%attr(755,root,root) %{_sbindir}/%{name}

%changelog
%autochangelog

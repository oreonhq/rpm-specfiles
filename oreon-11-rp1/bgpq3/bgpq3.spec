%global source0_hash c2ae430fe95ca56ebcb0bf049719f3f04504cc5c13a1daf610dcb5a61aa95445

Name:           bgpq3
Version:        0.1.38
Release:        3%{?dist}
Summary:        Automate BGP filter generation based on routing database information

License:        BSD-2-Clause
URL:            http://snar.spb.ru/prog/bgpq3/
Source0:        https://github.com/snar/bgpq3/archive/refs/tags/v%{version}.zip
#Patch to fix:
# -destdir
# remove -s so that it does not strip debugging
Patch0:         bgpq3-fix-makefile-v2.patch

BuildRequires: gcc
BuildRequires: make
%description
You are running BGP in your network and want to automate 
filter generation for your routers? Well, with BGPQ3 it's easy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%install
%make_install

%check

%files
%doc CHANGES
%license COPYRIGHT
%{_bindir}/bgpq3
%{_mandir}/man8/bgpq3.8*

%changelog
%autochangelog

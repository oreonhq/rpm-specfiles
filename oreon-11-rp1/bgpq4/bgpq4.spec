%global source0_hash c228e44bb62141851e7213563b5800b9b7b56d183f71563d5f0fe1ecdf57709e

Summary:        Automate BGP filter generation based on routing database information
Name:           bgpq4
Version:        1.16
Release:        1%{?dist}
# bgpq4 itself is BSD-2-Clause but uses other source codes, breakdown:
# BSD-3-Clause: include/sys/queue.h
# ISC: compat/strlcpy.c
# LicenseRef-Fedora-Public-Domain: include/{string,sys/{_null,types}}.h
License:        BSD-2-Clause AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/bgp/bgpq4
Source0:        https://github.com/bgp/bgpq4/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make

%description
The bgpq4 utility can be used to generate BGP filter configurations
such as prefix lists, (extended) access lists, policy statement terms
and AS path lists based on routing database information and supports
output formats for BIRD, Cisco, Huawei, Juniper, MikroTik, Nokia and
OpenBGPD routers as well as generic JSON.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf --install

%build
%configure
%make_build

%install
%make_install

%check
make check

%files
%license COPYRIGHT
%doc README.md CHANGES
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
%autochangelog

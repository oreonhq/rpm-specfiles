%global source0_hash f99010aad2f6b9d78f13deebee006441755e5501efcc1680174316d4bb0ab509
Name:           tvlsim
Version:        1.01.12
Release:        1%{?dist}
Summary:        Travel Market Simulator
License:        LGPL-2.1-or-later
URL:            https://github.com/airsim/%{name}
Source0:        https://github.com/airsim/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  pkgconfig(airinv)
BuildRequires:  pkgconfig(airrac)
BuildRequires:  pkgconfig(airtsp)
BuildRequires:  pkgconfig(cppzmq)
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(rmol)
BuildRequires:  pkgconfig(sevmgr)
BuildRequires:  pkgconfig(simcrs)
BuildRequires:  pkgconfig(simfqt)
BuildRequires:  pkgconfig(stdair)
BuildRequires:  pkgconfig(trademgen)
BuildRequires:  pkgconfig(travelccm)
BuildRequires:  soci-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-postgresql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  stdair-data
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
# /oreon:deps
%description
The Travel Market Simulator project aims at providing reference implementation,
mainly in C++, of a travel market simulator, focusing on revenue management (RM)
for airlines. It is intended to be used for applied research activities only:
it is by no way intended to be used by production systems. It is a new breed of
software and aims to become the new generation PODS (https://podsresearch.com/),
which was instrumental in the inception of the Travel Market Simulator project.

Over a dozen components have been implemented and are fully functional,
encompassing for instance (but not limited to) traveler demand generation
(booking requests), travel distribution (GDS/CRS), low fare search (LFS),
price calculation and inventory availability calculation), customer choice
modeling (CCM), revenue management (RM), schedule and inventory management,
revenue accounting (RA).

The Travel Market Simulator can be used in either batch or hosted mode.
It is the main component of the Travel Market Simulator:
https://www.travel-market-simulator.com

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) libraries are used.

The %{name} component itself aims at providing a clean API and a simple
implementation, as a C++ library, of a full travel market simulator,
focusing on revenue management (RM) for airlines. That library uses
the Standard Airline IT C++ object model (https://github.com/airsim/stdair).

Install the %{name} package if you need a library of basic C++ objects
for airline-related travel market simulation.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex)
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  texlive-epstopdf
%description    doc
This package contains HTML pages, as well as a PDF reference manual,
for %{name}. All that documentation is generated thanks to Doxygen
(https://doxygen.org). The content is the same as what can be browsed
online (https://%{name}.org).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_bindir}/simulate %{buildroot}%{_bindir}/%{name}_simulate
mv %{buildroot}%{_mandir}/man1/simulate.1 %{buildroot}%{_mandir}/man1/%{name}_simulate.1
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n tvlsim-devel -f %{oreon_filedir}/tvlsim-devel.list
%files -n tvlsim-doc -f %{oreon_filedir}/tvlsim-doc.list

%changelog

%autochangelog

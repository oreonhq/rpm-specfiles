%global source0_hash 3d4fe340d236d43e7f036272388b1bcc9eb5e10710698f33f9541b724f3a34b2
Name:           simcrs
Version:        1.01.14
Release:        1%{?dist}
Summary:        C++ Simulated Travel-Oriented Distribution System library
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
BuildRequires:  pkgconfig(simfqt)
BuildRequires:  pkgconfig(stdair)
BuildRequires:  soci-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-postgresql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  stdair-data
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
# /oreon:deps
%description
%{name} aims at providing a clean API and a simple implementation,
as a C++ library, of a Travel-oriented Distribution System. It
corresponds to the simulated version of the real-world Computerized
Reservation Systems (CRS). That library uses the Standard Airline IT
C++ object model (https://www.stdair.org).

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for airline-related booking distribution system, mainly for simulation purpose.

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
BuildRequires:  texlive-epstopdf
BuildRequires:  doxygen
BuildRequires:  ghostscript
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
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n simcrs-devel -f %{oreon_filedir}/simcrs-devel.list
%files -n simcrs-doc -f %{oreon_filedir}/simcrs-doc.list

%changelog

%autochangelog

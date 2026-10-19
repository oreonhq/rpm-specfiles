%global source0_hash ff2da35677ad15024ecde1c085d450e9e93a70961895acfd4a662a5981f26f0a
Name:           airrac
Version:        1.00.15
Release:        1%{?dist}
Summary:        C++ Simulated Revenue Accounting (RAC) System Library
License:        LGPL-2.1-or-later
URL:            https://github.com/airsim/%{name}
Source0:        https://github.com/airsim/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(stdair)
BuildRequires:  soci-devel
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-postgresql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
# /oreon:deps
%description
%{name} is a C++ library of airline revenue accounting classes and
functions, mainly targeting simulation purposes.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Airline Revenue Accounting, mainly for simulation purpose.

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
online (https://github.com/airsim/%{name}).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_docdir}/%{name}/html/installdox
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}
%oreon_autofiles airrac-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles airrac-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n airrac-devel -f %{oreon_filedir}/airrac-devel.list
%files -n airrac-doc -f %{oreon_filedir}/airrac-doc.list

%changelog

%autochangelog

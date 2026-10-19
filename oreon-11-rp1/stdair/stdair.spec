%global source0_hash 193cd0f5659d707bb028bc73c797dbd680abb3ea2259da6a134aa54277693b37
Name:           stdair
Version:        1.00.26
Release:        1%{?dist}
Summary:        C++ Standard Airline IT Object Library
License:        LGPL-2.1-or-later
URL:            https://github.com/airsim/%{name}
Source0:        https://github.com/airsim/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libpq-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  pkgconfig(readline)
BuildRequires:  soci-mysql-devel
BuildRequires:  soci-postgresql-devel
BuildRequires:  soci-sqlite3-devel
BuildRequires:  sqlite-devel
BuildRequires:  tex(latex)
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-epstopdf
BuildRequires:  texlive-hanging
BuildRequires:  texlive-ltablex
BuildRequires:  texlive-multirow
BuildRequires:  texlive-newunicodechar
BuildRequires:  texlive-ninecolors
BuildRequires:  texlive-stackengine
BuildRequires:  texlive-tabularray
BuildRequires:  texlive-ulem
BuildRequires:  texlive-wasysym
BuildRequires:  texlive-xltabular
# /oreon:deps
%description
%{name} aims at providing a clean API, and the corresponding C++
implementation, for the basis of Airline IT and travel distribution
Business Object Model (BOM), that is, to be used by several other open
source projects, such as AirRAC, RMOL, AirInv, AvlCal, AirSched, SimFQT,
SimLFS, SimCRS, TravelCCM, SEvMgr, TraDemGen, DSim, OpenTREP, etc.

Install the %{name} package if you need a library of basic C++ objects
for Airline IT (e.g., schedule management, inventory, revenue management,
revenue accounting), travel distribution, demand generation and customer choice
modeling, mainly for simulation purpose.

%package        devel
Summary:        Header files, libraries and development helper tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%description    devel
This package contains the header files, shared libraries and
development helper tools for %{name}. If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        data
Summary:        Sample data sets for the Airline/Travel Market simulator (AirSim/TvlSim)
%description    data
This package contains sample data sets for the components of
the Airline/Travel Market simulator (AirSim/TvlSim):
https://github.com/airsim/.
Most of those data sets may be browsed online as well:
https://github.com/airsim/stdair/tree/main/samples/

%package        doc
Summary:        HTML documentation for the %{name} library
BuildArch:      noarch
BuildRequires:  tex(latex)
BuildRequires:  doxygen
BuildRequires:  ghostscript
BuildRequires:  texlive-epstopdf texlive-ltablex texlive-xltabular
BuildRequires:  texlive-tabularray texlive-multirow texlive-hanging
BuildRequires:  texlive-adjustbox texlive-stackengine texlive-ulem
BuildRequires:  texlive-wasysym texlive-newunicodechar texlive-ninecolors
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
find %{buildroot}%{_libexecdir}/%{name} -type f -name '*.sh' -exec chmod +x {} \;
rm -f %{buildroot}/%{_docdir}/%{name}/html/installdox
rm -f %{buildroot}%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n stdair-devel -f %{oreon_filedir}/stdair-devel.list
%files -n stdair-data -f %{oreon_filedir}/stdair-data.list
%files -n stdair-doc -f %{oreon_filedir}/stdair-doc.list

%changelog

%autochangelog

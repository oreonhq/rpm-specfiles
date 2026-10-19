%global source0_hash daed30a934b4b9694338e92bd8a5271c7d9f3bdaa016ae8db6ff2270a4d5ca3f
Name:           travelccm
Version:        1.00.14
Release:        1%{?dist}
Summary:        C++ Travel Customer Choice Model (CCM) Library
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
BuildRequires:  stdair-data
BuildRequires:  tex(latex)
BuildRequires:  texlive-epstopdf
# /oreon:deps
%description
%{name} aims at providing a clean API, and the corresponding
C++ implementation, for choosing one item among a set of travel
solutions, given demand-related characteristics (e.g.,
Willingness-To-Pay, preferred airline, preferred cabin, etc.).

The %{name} C++ library implements some simple Customer Choice Models
(CCM), as referenced in the literature (PhD dissertations at MIT, for
instance: https://dspace.mit.edu).

The %{name} C++ library exposes a simple, clean and object-oriented,
API. For instance, the choose() method takes, as input, both a
structure representing the travel request (e.g., "from Washington, DC,
US, to Beijing, China, on the 25th of May") and a list of travel
solutions (as provided by the Airline Travel Solution Provider (AirTSP)
project: https://github.com/airsim/airtsp), and yields, as output, the
chosen item.

The output can then be used by other systems, for instance to book the
corresponding travel or to visualize it on a map and calendar and to
share it with others.

%{name} makes an extensive use of existing open-source libraries for
increased functionality, speed and accuracy. In particular the
Boost (C++ Standard Extensions: https://www.boost.org) library is used.

Install the %{name} package if you need a library of basic C++ objects
for Customer-Choice Modeling (CCM), mainly for simulation purpose.

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
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/html/installdox
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/{NEWS,README.md,AUTHORS}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n travelccm-devel -f %{oreon_filedir}/travelccm-devel.list
%files -n travelccm-doc -f %{oreon_filedir}/travelccm-doc.list

%changelog

%autochangelog

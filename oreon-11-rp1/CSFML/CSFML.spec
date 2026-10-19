%global source0_hash 903cd4a782fb0b233f732dc5b37861b552998e93ae8f268c40bd4ce50b2e88ca
Name:           CSFML
Summary:        C Interface for the Simple and Fast Multimedia Library
License:        Zlib
Version:        3.0.0
Release:        1%{?dist}
URL:            https://www.sfml-dev.org/download/csfml/
Source0:        https://github.com/SFML/CSFML/archive/%{version}/CSFML-%{version}.tar.gz
Patch0:         CSFML-2.6.1-Use_GNUInstallDirs.patch
# oreon:deps
BuildRequires:  SFML-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
CSFML is the official C interface for the SFML library (written in C++),
allowing to develop applications using C instead of C++.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains developer documentation (in HTML format) for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCSFML_BUILD_DOC=TRUE
%cmake_build
%install
%cmake_install
install -m 755 -d %{buildroot}%{_datadir}/doc
mv \
	%{buildroot}%{_datadir}/%{name}/doc \
	%{buildroot}%{_datadir}/doc/%{name}
rm %{buildroot}%{_datadir}/%{name}/license.md
rm %{buildroot}%{_datadir}/%{name}/readme.md
%ldconfig_scriptlets
%oreon_autofiles CSFML-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles CSFML-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n CSFML-devel -f %{oreon_filedir}/CSFML-devel.list
%files -n CSFML-doc -f %{oreon_filedir}/CSFML-doc.list

%changelog

%autochangelog

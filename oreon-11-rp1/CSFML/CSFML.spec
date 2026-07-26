%global source0_hash f3f3980f6b5cad85b40e3130c10a2ffaaa9e36de5f756afd4aacaed98a7a9b7b

Name:           CSFML
Summary:        C Interface for the Simple and Fast Multimedia Library
License:        Zlib

Version:        2.6.1
Release:        7%{?dist}

URL:            https://www.sfml-dev.org/download/csfml/
Source0:        https://github.com/SFML/CSFML/archive/%{version}/CSFML-%{version}.tar.gz

# Use install paths from GNUInstallDirs
# Cherr-picked from: https://github.com/SFML/CSFML/pull/398.patch
Patch0:         CSFML-2.6.1-Use_GNUInstallDirs.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SFML-devel

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

%autosetup -p1

%build
%cmake -DCSFML_BUILD_DOC=TRUE
%cmake_build

%install
%cmake_install

# Fix documentation being installed in wrong directory
install -m 755 -d %{buildroot}%{_datadir}/doc
mv \
	%{buildroot}%{_datadir}/%{name}/doc \
	%{buildroot}%{_datadir}/doc/%{name}

# Remove license.txt and readme.txt - rely on %%license and %%doc macros
rm %{buildroot}%{_datadir}/%{name}/license.md
rm %{buildroot}%{_datadir}/%{name}/readme.md

%ldconfig_scriptlets

%files
%license license.md
%doc readme.md
%{_libdir}/libcsfml-*.so.2*

%files devel
%{_includedir}/SFML/
%{_libdir}/libcsfml-*.so
%{_libdir}/pkgconfig/csfml*.pc

%files doc
%license license.md
%doc %{_datadir}/doc/%{name}/

%changelog
%autochangelog

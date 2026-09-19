%global source0_hash d445667e145f755f0bc34ac89b63a6bfdce1eea943f87ee7a3f23dc0dcede8b1

Name:      libgta
Version:   1.2.1
%global so_version 1
Release:   17%{?dist}
Summary:   Library that implements the Generic Tagged Arrays file format
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:   LicenseRef-Callaway-LGPLv2+
URL:       https://marlam.de/gta/
Source0:   https://marlam.de/gta/releases/%{name}-%{version}.tar.xz
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: doxygen

%description
Libgta is a portable library that implements the GTA (Generic Tagged Arrays)
file format. It provides interfaces for C and C++.

%package devel
Summary:  Development Libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:  API documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
The %{name}-doc package contains HTML API documentation and
examples for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake -D GTA_BUILD_STATIC_LIB:BOOL=FALSE
%cmake_build

%install
%cmake_install

# Remove documentation; will install it with doc macro
rm -rf %{buildroot}%{_docdir}

%check
%ctest

%ldconfig_scriptlets

%files 
%doc COPYING AUTHORS README
%{_libdir}/%{name}.so.%{so_version}
%{_libdir}/%{name}.so.%{so_version}.*

%files devel
%{_libdir}/cmake/GTA-%{version}
%{_libdir}/pkgconfig/gta.pc
%{_includedir}/gta
%{_libdir}/%{name}.so

%files doc
%doc doc/example*

%changelog
%autochangelog

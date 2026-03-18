Name:           libmodman
Version:        2.0.1
Release:        36%{?dist}
Summary:        A simple library for managing C++ modules (plug-ins)

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://code.google.com/p/libmodman/
Source0:        http://libmodman.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel

%description
libmodman is a simple library for managing C++ modules (plug-ins).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS
%{_libdir}/libmodman.so.*

%files devel
%{_includedir}/libmodman/
%{_libdir}/libmodman.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/Findlibmodman.cmake

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.1-36
- Prepare for Oreon 11 (RP1)

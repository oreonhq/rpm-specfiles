%bcond_without mingw

Name:     inih
Version:  62
Release:  2%{?dist}
Summary:  Simple INI file parser library

License:  BSD-3-Clause
URL:      https://github.com/benhoyt/inih
Source0:        https://github.com/benhoyt/inih/archive/r62/inih-r62.tar.gz
# oreon url source checksums begin
%global source0_sha256 9c15fa751bb8093d042dae1b9f125eb45198c32c6704cd5481ccde460d4f8151
%global source0_file inih-r62.tar.gz
# oreon url source checksums end

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: meson

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
%endif


%description
The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.

%package cpp
Summary: INIReader C++ library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cpp
This package contains the INIReader C++ library which provides a C++ interface
for inih.

%package devel
Summary:  Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

The inih package provides simple INI file parser which is only a couple of
pages of code, and it was designed to be small and simple, so it's good for
embedded systems.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif


%{?mingw_debug_package}


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/inih-r62.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9c15fa751bb8093d042dae1b9f125eb45198c32c6704cd5481ccde460d4f8151" || { echo "oreon: Source0 SHA256 mismatch for inih-r62.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n %{name}-r%{version}


%build
%meson
%meson_build

%if %{with mingw}
%mingw_meson
%mingw_ninja
%endif


%install
%meson_install
%if %{with mingw}
%mingw_ninja_install
%endif

%{?mingw_debug_install_post}


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/lib%{name}.so.0

%files cpp
%{_libdir}/libINIReader.so.0


%files devel
%{_includedir}/ini.h
%{_includedir}/INIReader.h
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/pkgconfig/INIReader.pc
%{_libdir}/lib%{name}.so
%{_libdir}/libINIReader.so

%if %{with mingw}
%files -n mingw32-%{name}
%{mingw32_bindir}/lib%{name}-0.dll
%{mingw32_bindir}/libINIReader-0.dll
%{mingw32_includedir}/ini.h
%{mingw32_includedir}/INIReader.h
%{mingw32_libdir}/lib%{name}.dll.a
%{mingw32_libdir}/libINIReader.dll.a
%{mingw32_libdir}/pkgconfig/inih.pc
%{mingw32_libdir}/pkgconfig/INIReader.pc

%files -n mingw64-%{name}
%{mingw64_bindir}/lib%{name}-0.dll
%{mingw64_bindir}/libINIReader-0.dll
%{mingw64_includedir}/ini.h
%{mingw64_includedir}/INIReader.h
%{mingw64_libdir}/lib%{name}.dll.a
%{mingw64_libdir}/libINIReader.dll.a
%{mingw64_libdir}/pkgconfig/inih.pc
%{mingw64_libdir}/pkgconfig/INIReader.pc
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 62-2
- Prepare for Oreon 11 (RP1)

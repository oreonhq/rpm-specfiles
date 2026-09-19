%global source0_hash c49deac9e0933bcb7044f08516861a2d560988540b23de2ac1ad443b219afdb6

%{?mingw_package_header}

%global pkgname jsoncpp

%global jsondir json

%global common_desc \
%{pkgname} is an implementation of a JSON (http://json.org) reader and writer in \
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format. \
It is easy for humans to read and write. It is easy for machines to parse and \
generate. \
%{nil}

Name:           mingw-%{pkgname}
Version:        1.8.4
Release:        21%{?dist}
Summary:        JSON library implemented in C++

# Automatically converted from old format: Public Domain or MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain OR LicenseRef-Callaway-MIT
URL:            https://github.com/open-source-parsers/%{pkgname}
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake >= 3.1

# Win32 BRs
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers

# Win64 BRs
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers

%description %{common_desc}

# Win32
%package -n mingw32-%{pkgname}
Summary:        JSON library implemented in C++ for Win32 target

%description -n mingw32-%{pkgname} %{common_desc}
This package provides the library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:        JSON library implemented in C++ for Win64 target

%description -n mingw64-%{pkgname} %{common_desc}
This package provides the library for the Win64 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pkgname}-%{version} -p1

%build
%mingw_cmake -DBUILD_STATIC_LIBS=OFF                \
             -DJSONCPP_WITH_WARNING_AS_ERROR=OFF    \
             -DJSONCPP_WITH_PKGCONFIG_SUPPORT=ON    \
             -DJSONCPP_WITH_CMAKE_PACKAGE=ON        \
             -DJSONCPP_WITH_POST_BUILD_UNITTEST=OFF \
             .

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

%files -n mingw32-%{pkgname}
%license AUTHORS LICENSE
%doc README.md
%{mingw32_bindir}/lib%{pkgname}*.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_includedir}/%{jsondir}
%{mingw32_libdir}/cmake/*
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc

%files -n mingw64-%{pkgname}
%license AUTHORS LICENSE
%doc README.md
%{mingw64_bindir}/lib%{pkgname}*.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_includedir}/%{jsondir}
%{mingw64_libdir}/cmake/*
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc

%changelog
%autochangelog

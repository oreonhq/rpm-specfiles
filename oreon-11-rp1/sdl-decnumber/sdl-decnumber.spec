%global source0_hash 83501b58117e55d737e48fa1490f1ace2812aff7f77b8cd863d542ad9f58767d
%global srcname decNumber
%global date 20250324
%global commit 995184583107625015bb450228a5f3fb781d9502
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%if 0%{?el8}
%undefine __cmake_in_source_build
%endif
%global _vpath_builddir %{_builddir}/%{srcname}%{__isa_bits}.Release
%global debug_package %{nil}
%global common_description %{expand:
The decNumber library implements the General Decimal Arithmetic Specification
in ANSI C. This specification defines a decimal arithmetic which meets the
requirements of commercial, financial, and human-oriented applications. It
also matches the decimal arithmetic in the IEEE 754 Standard for Floating
Point Arithmetic.
The library fully implements the specification, and hence supports integer,
fixed-point, and floating-point decimal numbers directly, including infinite,
NaN (Not a Number), and subnormal values. Both arbitrary-precision and
fixed-size representations are supported.
This version is a fork by SoftDevLabs (SDL) to support the SDL-Hercules-390
emulator.}
Name:           sdl-decnumber
Version:        3.68.0^%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        ANSI C General Decimal Arithmetic Library (SDL version)
License:        MIT
URL:            https://github.com/SDL-Hercules-390/%{srcname}
Source0:        https://github.com/SDL-Hercules-390/%{srcname}/archive/%{commit}/%{srcname}-%{commit}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
Provides:       decnumber-devel%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-devel < 1.0.0-11
Provides:       decnumber-static%{?_isa} = %{version}-%{release}
Obsoletes:      decnumber-static < 1.0.0-11
%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Provides:       decnumber-doc = %{version}-%{release}
Obsoletes:      decnumber-doc < 1.0.0-11
%description    doc
The %{name}-doc package contains documentation and examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}
sed -i extra.txt -e 's:DESTINATION .:DESTINATION share/doc/%{name}-doc:g'

%build

%cmake
%cmake_build
%install
%cmake_install
mv %{buildroot}%{_docdir}/%{name}-doc/decnumber.ICU-license.html .
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sdl-decnumber-devel -f %{oreon_filedir}/sdl-decnumber-devel.list
%files -n sdl-decnumber-doc -f %{oreon_filedir}/sdl-decnumber-doc.list

%changelog

%autochangelog

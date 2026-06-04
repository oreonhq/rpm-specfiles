%global source0_hash f05b24d2368becab9144873878655bb718910631550d4f786262378c16ab94a7

%bcond_without mingw

Name:           liblerc
Version:        4.1.0
Release:        1%{?dist}
Summary:        Library for Limited Error Raster Compression

License:        Apache-2.0
URL:            https://github.com/Esri/lerc
Source0:        https://github.com/Esri/lerc/archive/refs/tags/v%{version}/lerc-%{version}.tar.gz
# Add version suffix to mingw dll
Patch0:         lerc-dllver.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-devel

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
%endif

%description
LERC is an open-source image or raster format which supports rapid encoding and
decoding for any pixel type (not just RGB or Byte). Users set the maximum
compression error per pixel while encoding, so the precision of the original
input image is preserved (within user defined error bounds).


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
%{summary}.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
%{summary}.
%endif


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n lerc-%{version}

# Fix line endings
sed -i 's/\r$//' NOTICE README.md doc/MORE.md


%build
# Native build
%cmake
%cmake_build

%if %{with mingw}
# MinGW build
%mingw_cmake
%mingw_make_build
%endif


%install
%cmake_install
%if %{with mingw}
%mingw_make_install
%endif


%files
%license LICENSE
%doc README.md CHANGELOG.md NOTICE
%{_libdir}/libLerc.so.4

%files devel
%doc doc/*
%{_includedir}/Lerc_c_api.h
%{_includedir}/Lerc_types.h
%{_libdir}/libLerc.so
%{_libdir}/pkgconfig/Lerc.pc

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/libLerc-4.dll
%{mingw32_includedir}/Lerc_c_api.h
%{mingw32_includedir}/Lerc_types.h
%{mingw32_libdir}/libLerc.dll.a
%{mingw32_libdir}/pkgconfig/Lerc.pc

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/libLerc-4.dll
%{mingw64_includedir}/Lerc_c_api.h
%{mingw64_includedir}/Lerc_types.h
%{mingw64_libdir}/libLerc.dll.a
%{mingw64_libdir}/pkgconfig/Lerc.pc
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.0-1
- Prepare for Oreon 11 (RP1)

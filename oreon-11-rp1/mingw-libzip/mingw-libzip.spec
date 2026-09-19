%global source0_hash 8a247f57d1e3e6f6d11413b12a6f28a9d388de110adc0ec608d893180ed7097b

%{?mingw_package_header}

%global pkgname libzip

Name:           mingw-%{pkgname}
Version:        1.11.4
Release:        3%{?dist}
Summary:        C library for reading, creating, and modifying zip archives

License:        BSD-3-Clause
BuildArch:      noarch
URL:            http://www.nih.at/libzip/index.html
Source0:        http://www.nih.at/libzip/%{pkgname}-%{version}.tar.xz
# Add soversion suffix, as was the case previously with autotools build
Patch0:         libzip_cmake.patch

BuildRequires:  ninja-build
BuildRequires:  cmake
#BuildRequires: perl
#BuildRequires: libzip-tools

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-zlib >= 1.1.2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-zlib >= 1.1.2

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n mingw32-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw32-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%package -n mingw64-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw64-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
%mingw_cmake -G Ninja
%mingw_ninja

%install
%mingw_ninja_install

# Remove unused files
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}

%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/zipcmp.exe
%{mingw32_bindir}/zipmerge.exe
%{mingw32_bindir}/ziptool.exe
%{mingw32_bindir}/libzip-5.dll
%{mingw32_libdir}/libzip.dll.a
%{mingw32_libdir}/pkgconfig/libzip.pc
%{mingw32_libdir}/cmake/libzip/
%{mingw32_includedir}/zip.h
%{mingw32_includedir}/zipconf.h

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/zipcmp.exe
%{mingw64_bindir}/zipmerge.exe
%{mingw64_bindir}/ziptool.exe
%{mingw64_bindir}/libzip-5.dll
%{mingw64_libdir}/libzip.dll.a
%{mingw64_libdir}/pkgconfig/libzip.pc
%{mingw64_libdir}/cmake/libzip/
%{mingw64_includedir}/zip.h
%{mingw64_includedir}/zipconf.h

%changelog
%autochangelog

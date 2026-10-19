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
Source0:        http://www.nih.at/%{pkgname}/%{pkgname}-%{version}.tar.xz
Patch0:         libzip_cmake.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-zlib
BuildRequires:  ninja-build
# /oreon:deps
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
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libzip -f %{oreon_filedir}/mingw32-libzip.list
%files -n mingw64-libzip -f %{oreon_filedir}/mingw64-libzip.list

%changelog

%autochangelog

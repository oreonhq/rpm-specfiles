%global source0_hash d7a0654783a4da529d1bb793b7ad9c3318020af77667bcae35f95d0e42a792f3
%global mingw_build_ucrt64 1
%{?mingw_package_header}
Name:           mingw-zlib
Version:        1.3.2
Release:        1%{?dist}
Summary:        MinGW Windows zlib compression library
License:        Zlib
URL:            https://www.zlib.net/
Source0:        https://www.zlib.net/zlib-%{version}.tar.xz
Patch0:         mingw-zlib-cmake.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc
# /oreon:deps
%description
MinGW Windows zlib compression library.

# Win32
%package -n mingw32-zlib
Summary:        MinGW Windows zlib compression library for the win32 target
%description -n mingw32-zlib
MinGW Windows zlib compression library for the win32 target.

%package -n mingw32-zlib-static
Summary:        Static libraries for mingw32-zlib development.
Requires:       mingw32-zlib = %{version}-%{release}
%description -n mingw32-zlib-static
The mingw32-zlib-static package contains static library for mingw32-zlib development.

# Win64
%package -n mingw64-zlib
Summary:        MinGW Windows zlib compression library for the win64 target
%description -n mingw64-zlib
MinGW Windows zlib compression library for the win64 target.

%package -n mingw64-zlib-static
Summary:        Static libraries for mingw64-zlib development
Requires:       mingw64-zlib = %{version}-%{release}
%description -n mingw64-zlib-static
The mingw64-zlib-static package contains static library for mingw64-zlib development.

# UCRT64
%package -n ucrt64-zlib
Summary:        MinGW Windows zlib compression library for the ucrt64 target
%description -n ucrt64-zlib
MinGW Windows zlib compression library for the ucrt64 target.

%package -n ucrt64-zlib-static
Summary:        Static libraries for ucrt64-zlib development
Requires:       ucrt64-zlib = %{version}-%{release}
%description -n ucrt64-zlib-static
The ucrt64-zlib-static package contains static library for ucrt64-zlib development.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir zlib-%{version}
%oreon_prep
%build

MINGW32_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{mingw32_libdir}/pkgconfig \
MINGW64_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{mingw64_libdir}/pkgconfig \
UCRT64_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{ucrt64_libdir}/pkgconfig \
%mingw_cmake
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{ucrt64_docdir}
%oreon_autofiles mingw32-zlib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-zlib-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-zlib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-zlib-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-zlib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-zlib-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-zlib -f %{oreon_filedir}/mingw32-zlib.list
%files -n mingw32-zlib-static -f %{oreon_filedir}/mingw32-zlib-static.list
%files -n mingw64-zlib -f %{oreon_filedir}/mingw64-zlib.list
%files -n mingw64-zlib-static -f %{oreon_filedir}/mingw64-zlib-static.list
%files -n ucrt64-zlib -f %{oreon_filedir}/ucrt64-zlib.list
%files -n ucrt64-zlib-static -f %{oreon_filedir}/ucrt64-zlib-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)

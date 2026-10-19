%global source0_hash 73bc2f51b90d2a780e6d266d43e487b3dbd78945dd0b04b14ca5980fe28d2f53
%{?mingw_package_header}
Name:           mingw-gsl
Version:        1.16
Release:        1%{?dist}
Summary:        MinGW Windows port of the GNU Scientific Library
License:        GPL-3.0-only AND LicenseRef-Callaway-GFDL AND LicenseRef-Callaway-BSD
URL:            http://www.gnu.org/software/gsl/
Source0:        https://ftp.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
Patch0:         gsl-1.15-lib64.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

# Mingw32
%package -n mingw32-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win32 target
%description -n mingw32-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw32-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw32-gsl = %{version}-%{release}
%description -n mingw32-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

# Mingw64
%package -n mingw64-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win64 target
%description -n mingw64-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw64-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw64-gsl = %{version}-%{release}
%description -n mingw64-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gsl-%{version}
%patch -P0 -p1 -b .lib64
iconv -f windows-1252 -t utf-8 THANKS > THANKS.aux
touch -r THANKS THANKS.aux
mv THANKS.aux THANKS

%build

%mingw_configure
%mingw_make %{?_smp_mflags}
%install
%mingw_make install "DESTDIR=$RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}
%oreon_autofiles mingw32-gsl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-gsl-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gsl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gsl-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gsl -f %{oreon_filedir}/mingw32-gsl.list
%files -n mingw32-gsl-static -f %{oreon_filedir}/mingw32-gsl-static.list
%files -n mingw64-gsl -f %{oreon_filedir}/mingw64-gsl.list
%files -n mingw64-gsl-static -f %{oreon_filedir}/mingw64-gsl-static.list

%changelog

%autochangelog

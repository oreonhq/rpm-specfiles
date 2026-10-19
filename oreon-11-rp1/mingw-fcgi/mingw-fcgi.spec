%global source0_hash e41ddc3a473b555bdc0cbd80703dcb1f4610c1a7700d3b9d3d0c14a416e1074b
%{?mingw_package_header}
%global pkgname fcgi
Name:           mingw-%{pkgname}
Version:        2.4.7
Release:        2%{?dist}
Summary:        MinGW Windows fcgi library
BuildArch:      noarch
License:        OML
URL:            https://fastcgi-archives.github.io/
Source0:        https://github.com/FastCGI-Archives/%{pkgname}2/archive/%{version}/%{pkgname}-%{version}.tar.gz
Patch0:         fcgi-incompat-pointer-types.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}2-%{version}
# remove DOS End Of Line Encoding
sed -i 's/\r//' doc/fastcgi-prog-guide/ch2c.htm
# fix file permissions
chmod a-x include/fcgios.h libfcgi/os_unix.c

%build

autoreconf -ifv
%mingw_configure --disable-static
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-fcgi -f %{oreon_filedir}/mingw32-fcgi.list
%files -n mingw64-fcgi -f %{oreon_filedir}/mingw64-fcgi.list

%changelog

%autochangelog

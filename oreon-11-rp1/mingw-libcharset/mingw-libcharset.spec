%global source0_hash 88dd96a8c0464eca144fc791ae60cd31cd8ee78321e67397e25fc095c4a19aa6
%{?mingw_package_header}
%global pkgname libcharset
Name:          mingw-%{pkgname}
Version:       1.19
Summary:        MinGW Windows libcharset library
Release:        1%{?dist}
BuildArch:     noarch
License:       LGPL-2.0-or-later
URL:           http://www.haible.de/bruno/packages-libcharset.html
Source0:        https://ftp.gnu.org/pub/gnu/libiconv/libiconv-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
MinGW Windows libcharset library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows libcharset library
%description -n mingw32-%{pkgname}
MinGW Windows libcharset library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows libcharset library
%description -n mingw64-%{pkgname}
MinGW Windows libcharset library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libiconv-%{version}
%oreon_prep
%build

(
cd libcharset
%mingw_configure --disable-static
%mingw_make_build
)
%install
(
cd libcharset
%mingw_make_install
)
find %{buildroot} -name *.la -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libcharset -f %{oreon_filedir}/mingw32-libcharset.list
%files -n mingw64-libcharset -f %{oreon_filedir}/mingw64-libcharset.list

%changelog

%autochangelog
